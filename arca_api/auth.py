import datetime
import base64
import os
import xml.etree.ElementTree as ET
import time
import dateutil.parser
from zeep import Client
import pickle
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.serialization import pkcs7
from .settings import CERT_PATH, PRIVATE_KEY_PATH, WSDL_WSAA_HOM, WSDL_WSAA_PROD, PROD, TA_FILES_PATH
from typing import Tuple

TOKEN_EXPIRATION_OFFSET = -600
WSDL_WSAA = WSDL_WSAA_HOM if not PROD else WSDL_WSAA_PROD

class LoginTicket:
    """
    Maneja los datos del Ticket de Acceso.
    
    Esta clase gestiona los datos de los tickets de autenticación (TA) para los servicios web de AFIP.
    
    Atributos:
        xml: Cadena XML que contiene los datos del TA
        tree: Árbol XML parseado del TA
        expires_str: Tiempo de expiración del TA en formato string
        expires: Tiempo de expiración del TA en formato timestamp Unix
        token: Token del TA
        sign: Firma del TA
    """
    
    def __init__(self, xml_response: str) -> None:
        self.xml: str = xml_response
        self.tree: ET.ElementTree = ET.ElementTree(ET.fromstring(xml_response))
        self.expires_str: str = self.tree.find(".//expirationTime").text
        self.expires: float = dateutil.parser.parse(self.expires_str).timestamp() + TOKEN_EXPIRATION_OFFSET
        self.token: str = self.tree.find(".//token").text
        self.sign: str = self.tree.find(".//sign").text
    
    @property
    def is_expired(self) -> bool:
        """Verifica si el ticket ha expirado."""
        return time.time() >= self.expires

    def get_token_sign(self) -> Tuple[str, str]:
        """Obtiene los valores del token y la firma."""
        return self.token, self.sign


class ArcaAuth:
    """
    Maneja la autenticación para los servicios web de ARCA.
    
    Esta clase maneja la creación, firma y gestión de 
    tickets de autenticación (TA) para los servicios web de ARCA.
    
    Atributos:
        service (str): Nombre del servicio web de ARCA a autenticar
        ta_data (LoginTicket): Datos actuales del ticket de autenticación
    """

    def __init__(self, service):
        self.service = service
        self.ta_data = None
        self.ta_data = self.load_ta()

    def create_tra(self, expiration_time):
        """Genera el XML para el Ticket Request Access (TRA)."""
        
        now = datetime.datetime.now()
        return f"""<?xml version="1.0" encoding="UTF-8"?>
        <loginTicketRequest version="1.0">
            <header>
                <uniqueId>{int(now.timestamp())}</uniqueId>
                <generationTime>{now.strftime("%Y-%m-%dT%H:%M:%S")}</generationTime>
                <expirationTime>{expiration_time.strftime("%Y-%m-%dT%H:%M:%S")}</expirationTime>
            </header>
            <service>{self.service}</service>
        </loginTicketRequest>""".encode("utf-8")

    def sign_tra(self, tra_xml):
        """
        Firma el TRA (Ticket Request Access) usando PKCS#7.
        
        Args:
            tra_xml (str): Cadena XML que contiene el TRA a firmar
            
        Returns:
            str: TRA firmado y codificado en Base64 en formato DER
        """
        # Cargar la clave privada para firmar
        with open(PRIVATE_KEY_PATH, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None
            )
        
        # Cargar el certificado
        with open(CERT_PATH, 'rb') as cert_file:
            cert = x509.load_pem_x509_certificate(cert_file.read())

        # Crear la firma PKCS#7 en formato DER
        signed_data = pkcs7.PKCS7SignatureBuilder().set_data(
            tra_xml
        ).add_signer(
            cert,
            private_key,
            hashes.SHA256()
        ).sign(
            serialization.Encoding.DER,  
            [pkcs7.PKCS7Options.NoCapabilities] 
        )
        
        return base64.b64encode(signed_data).decode('utf-8')
    
    def request_new_ta(self):
        """
        Solicita un nuevo ticket de autenticación (TA) a ARCA.
        
        Crea un TRA válido por 12 horas, lo firma, lo envía al servicio WSAA,
        y almacena la respuesta localmente.
        
        Raises:
            WSError: Si la solicitud SOAP falla
            AuthError: Si la respuesta de autenticación es inválida
        """
        expiration_time = datetime.datetime.now() + datetime.timedelta(hours=12)
        tra = self.create_tra(expiration_time)  # Crear solicitud de ticket
        signed_cms = self.sign_tra(tra)  # Firmar la solicitud

        # Enviar solicitud al servicio WSAA
        client = Client(WSDL_WSAA)
        response = client.service.loginCms(signed_cms)
        
        # Almacenar el ticket de autenticación
        self.ta_data = LoginTicket(response)
        
        # Persistir el ticket en el sistema de archivos
        with open(TA_FILES_PATH + self.service + ".pkl", "wb") as f:
            pickle.dump(LoginTicket(response), f)

    def load_ta(self):
        """Carga el TA almacenado, si es válido."""
        
        if os.path.exists(TA_FILES_PATH + self.service + ".pkl"):
            with open(TA_FILES_PATH + self.service + ".pkl", "rb") as f:
                self.ta_data = pickle.load(f)
                
        if self.ta_data is None or self.ta_data.is_expired:
            self.request_new_ta()
        return self.ta_data

    def get_token_sign(self):
        """Devuelve el token y sign vigentes."""
        
        return self.ta_data.token, self.ta_data.sign

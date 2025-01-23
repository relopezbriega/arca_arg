from zeep import Client
from .auth import ArcaAuth
from typing import Any, Dict
from .settings import CUIT

class ArcaWebService:
    """
    Clase base para los servicios web de AFIP (Administración Federal de Ingresos Públicos).
    
    Esta clase proporciona la funcionalidad principal para interactuar con los servicios web de AFIP,
    manejando la autenticación y las llamadas a métodos SOAP.
    
    Atributos:
        client: Instancia del cliente SOAP para la comunicación con el servicio web
        auth: Manejador de autenticación para los servicios de AFIP
        token: Token de autenticación actual
        sign: Firma de autenticación actual
    """
    
    def __init__(self, wsdl_url: str, service_name: str) -> None:
        """
        Inicializa el servicio web con la URL del WSDL y el nombre del servicio.

        Args:
            wsdl_url: URL del archivo de definición WSDL
            service_name: Nombre del servicio de AFIP al que se conecta
        """
        self.client = Client(wsdl_url)
        self.auth = ArcaAuth(service_name)
        self.token, self.sign = self.auth.get_token_sign()

    def call_method(self, method_name: str, **kwargs: Dict[str, Any]) -> Any:
        """
        Llama a un método del servicio web con parámetros de autenticación.

        Args:
            method_name: Nombre del método SOAP a llamar
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            La respuesta del método del servicio web

        Ejemplo:
            >>> service.call_method('getPersona', cuit='20123456789')
        """
        return getattr(self.client.service, method_name)(
            token=self.token, 
            sign=self.sign, 
            cuitRepresentada=CUIT,
            **kwargs
        )

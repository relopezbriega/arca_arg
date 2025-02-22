import logging
from zeep import Client, exceptions
from .auth import ArcaAuth
from typing import Any, Dict, List, Optional
from .settings import CUIT
from zeep.xsd.types.complex import ComplexType
from lxml import etree

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        cuit: CUIT del contribuyente
        wsdl_url: URL del archivo de definición WSDL
        service_name: Nombre del servicio de AFIP al que se conecta
        complex_types: Lista de tipos complejos disponibles en el servicio web
    """
    
    def __init__(self, wsdl_url: str, service_name: str, enable_logging: bool = True) -> None:
        """
        Inicializa el servicio web con la URL del WSDL y el nombre del servicio.

        Args:
            wsdl_url: URL del archivo de definición WSDL
            service_name: Nombre del servicio de AFIP al que se conecta
            enable_logging: Habilita o deshabilita el logging (opcional, por defecto True)
        """
        self.client = Client(wsdl_url)
        self.auth = ArcaAuth(service_name)
        self.token, self.sign = self.auth.get_token_sign()
        self.cuit = CUIT
        self.wsdl_url = wsdl_url
        self.service_name = service_name
        self._complex_types = self._get_complex_types()
        self.enable_logging = enable_logging

        if self.enable_logging:
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = None

    def send_request(self, method_name: str, data: Dict[str, Any], response_type: str = None, **kwargs: Dict[str, Any]) -> Any:
        """
        Llama a un método del servicio web con parámetros de autenticación.

        Args:
            method_name: Nombre del método SOAP a llamar
            data: Diccionario con los datos a enviar al método SOAP
            response_type: Tipo de respuesta esperada (opcional)
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            La respuesta del método del servicio web

        Raises:
            exceptions.Error: Si ocurre un error en la llamada al servicio web

        Ejemplo:
            >>> service.send_request('getPersona', data, response_type='Persona')
        """
        try:
            if self.logger:
                self.logger.info(f"Llamando al método {method_name} con datos: {data}")
            response = getattr(self.client.service, method_name)(**data, **kwargs)
            if response_type:
                return self.client.get_type(response_type)(response)
            return response
        except exceptions.Error as e:
            if self.logger:
                self.logger.error(f"Error al llamar al método {method_name}: {e}")
            raise
    
    def list_methods(self) -> List[str]:
        """
        Lista los métodos disponibles del servicios web disponibles en ARCA.

        Returns:
            Lista de los nombres de los servicios web disponibles
        """
        methods = []
        for service in self.client.wsdl.services.values():
            for port in service.ports.values():
                methods.extend([operation.name for operation in port.binding._operations.values()])
        return methods
            
    def method_help(self, method_name: str) -> str:
        """
        Muestra la documentación de un método del servicio web.

        Args:
            method_name: Nombre del método SOAP a consultar

        Returns:
            La documentación del método del servicio web
        """
        return self.client.service.__getattr__(method_name).__doc__
    
    def create_message(self, method_name: str, data: Dict[str, Any]) -> str:
        """_summary_

        Args:
            method_name: Nombre del método SOAP a llamar
            data: Diccionario con los datos a enviar al método SOAP

        Returns:
            str: el xml con el mensaje que se va a enviar al método.
        """
        xml = self.client.create_message(self.client.service, method_name, **data)
        pretty_xml = etree.tostring(xml, pretty_print=True, encoding="utf-8").decode("utf-8")
        
        return pretty_xml

    
    def dump_wsdl(self) -> str:
        """
        Muestra el contenido del archivo WSDL del servicio web.

        Returns:
            El contenido del archivo WSDL del servicio web
        """
        return self.client.wsdl.dump()

    def _linked_complex_types(self) -> Dict[str, Any]:
        """
        Obtiene la lista de tipos complejos disponibles en el servicio web.

        Returns:
            Lista de tipos complejos disponibles en el servicio web
        """
        linked_complex_types_dict = {}

        for element in self.client.wsdl.types.types:
            if isinstance(element, ComplexType):
                linked_complex_types_dict[element.name] = element

        return linked_complex_types_dict
    
    
    def _get_complex_types(self) -> Dict[str, Any]:
        """
        Obtiene la lista de tipos complejos disponibles en el servicio web.

        Returns:
            Lista de tipos complejos disponibles en el servicio web
        """
        complex_types_dict = {}

        for element in self.client.wsdl.types.types:
            if isinstance(element, ComplexType):
                try:
                    element_values = element()
                except:
                    pass
                complex_types_dict[element.name] = element_values

        linked_types = self._linked_complex_types()

        for key, value in linked_types.items():
            if value is not None:
                for name, type_ in value.elements:
                    if isinstance(type_.type, ComplexType):
                        complex_types_dict[key][name] = linked_types[type_.type.name].name

        del(linked_types)

        return complex_types_dict

    def get_type(self, type_name : str) -> Dict[str, Any]:
        """
        Devuelve el diccionario del tipo complejo especificado.

        Args:
            type_name: nombre del tipo complejo. 

        Returns:
            Diccionario del tipo complejo.
        """
        copy_types = dict(self._complex_types)

        return copy_types[type_name]

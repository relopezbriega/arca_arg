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
        self.cuit = CUIT

    def sendRequest(self, method_name: str, data: Dict[str, Any], **kwargs: Dict[str, Any]) -> Any:
        """
        Llama a un método del servicio web con parámetros de autenticación.

        Args:
            method_name: Nombre del método SOAP a llamar
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            La respuesta del método del servicio web

        Ejemplo:
            >>> service.sendRequest('getPersona', **data)
        """
        return getattr(self.client.service, method_name)(**data, **kwargs)
    
    def listMethods(self) -> list:
        """
        Lista los métodos disponibles del servicios web disponibles en ARCA.

        Returns:
            Lista de los nombres de los servicios web disponibles
        """
        for service in self.client.wsdl.services.values():
            for port in service.ports.values():
                return [operation.name for operation in port.binding._operations.values()]
            
    def methodHelp(self, method_name: str) -> str:
        """
        Muestra la documentación de un método del servicio web.

        Args:
            method_name: Nombre del método SOAP a consultar

        Returns:
            La documentación del método del servicio web
        """
        return self.client.service.__getattr__(method_name).__doc__

    def elementDetails(self, element: str) -> list:
        """
        Muestra los parámetros de entrada de un método del servicio web.

        Args:
            element: Nombre del elemento SOAP a consultar

        Returns:
            Los parámetros del elemento del servicio web
        """
        data = self.client.get_type(element).elements
        salida = { }
        for name, type in data:
            salida[name] = str(type.type)

        return salida
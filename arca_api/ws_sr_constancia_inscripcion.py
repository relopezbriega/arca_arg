from .ws_service import ArcaWebService
from .settings import PROD, WSDL_CONSTANCIA_HOM, WSDL_CONSTANCIA_PROD
from typing import Any, Dict

WSDL_CONSTANCIA = WSDL_CONSTANCIA_HOM if not PROD else WSDL_CONSTANCIA_PROD
SERVICE_NAME = "ws_sr_constancia_inscripcion"

class ConstanciaService(ArcaWebService):
    """
    Servicio para consultar el estado de inscripción de contribuyentes en ARCA.
    
    Esta clase proporciona métodos para verificar el estado de inscripción y la validez
    de los números de identificación de contribuyentes (CUIT) en el sistema tributario de Argentina.
    
    Hereda de:
        ArcaWebService: Clase base para interacciones con servicios web de ARCA
    """

    def __init__(self) -> None:
        """Inicializa el servicio de estado de inscripción."""
        super().__init__(WSDL_CONSTANCIA, SERVICE_NAME)

    def consultar_cuit(self, cuit: str) -> Dict[str, Any]:
        """
        Consulta el estado de inscripción para un ID de contribuyente dado.

        Args:
            cuit: El ID del contribuyente a consultar

        Returns:
            Dict que contiene la información de inscripción del contribuyente

        Ejemplo:
            >>> service = ConstanciaService()
            >>> info = service.consultar_cuit("20123456789", "")
        """
        return self.call_method("getPersona_v2", idPersona=cuit)
    
    def consultar_lista_cuits(self, cuits: list) -> Dict[str, Any]:
        """
        Consulta el estado de inscripción para una lista de IDs de contribuyentes.

        Args:
            cuits: Lista de IDs de contribuyentes a consultar

        Returns:
            Dict que contiene la información de inscripción de todos los contribuyentes

        Ejemplo:
            >>> service = ConstanciaService()
            >>> info = service.consultar_lista_cuits(["20123456789", "20123456790"], "")
        """
        return self.call_method("getPersonaList_v2", idPersona=cuits)
    
    def server_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del servidor de ARCA.

        Returns:
            Dict que contiene información del estado del servidor incluyendo
            servidor de aplicaciones, servidor de base de datos y estado de autenticación
        """
        return self.client.service.dummy()
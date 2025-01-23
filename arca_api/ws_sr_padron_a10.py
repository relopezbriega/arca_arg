from .ws_service import ArcaWebService
from .settings import PROD, WSDL_PADRON_A10_HOM, WSDL_PADRON_A10_PROD
from typing import Any, Dict

WSDL_PADRON_A10 = WSDL_PADRON_A10_HOM if not PROD else WSDL_PADRON_A10_PROD
SERVICE_NAME = "ws_sr_padron_a10"

class PadronA10Service(ArcaWebService):
    """
    Servicio para consultar el estado de inscripción de contribuyentes en ARCA.
    
    Esta clase proporciona métodos para verificar el estado de inscripción y la validez
    de los números de identificación de contribuyentes (CUIT) en el sistema tributario de Argentina.
    
    Hereda de:
        ArcaWebService: Clase base para interacciones con servicios web de ARCA
    """
    
    def __init__(self) -> None:
        """Inicializa el servicio de estado de inscripción."""
        super().__init__(WSDL_PADRON_A10, SERVICE_NAME)
    
    def server_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del servidor de ARCA.

        Returns:
            Dict que contiene información del estado del servidor incluyendo
            servidor de aplicaciones, servidor de base de datos y estado de autenticación
        """
        return self.client.service.dummy()
    
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
        return self.call_method("getPersona", idPersona=cuit)
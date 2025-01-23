from .ws_service import ArcaWebService
from .settings import PROD, WSDL_LPG_HOM, WSDL_LPG_PROD, CUIT
from typing import Any, Dict

WSDL_LPG = WSDL_LPG_HOM if not PROD else WSDL_LPG_PROD
SERVICE_NAME = "wslpg"

class LPGService(ArcaWebService):
    """
    Servicio para manejar las Liquidaciones Primarias de Granos (LPG) de ARCA.
    
    Esta clase proporciona métodos para trabajar con las Liquidaciones Primarias de Granos
    en el sistema tributario de Argentina.
    
    Hereda de:
        ArcaWebService: Clase base para interacciones con servicios web de ARCA
    """
    
    def __init__(self) -> None:
        """Inicializa el servicio de estado de inscripción."""
        super().__init__(WSDL_LPG, SERVICE_NAME)
    
    def server_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del servidor de ARCA.

        Returns:
            Dict que contiene información del estado del servidor incluyendo
            servidor de aplicaciones, servidor de base de datos y estado de autenticación
        """
        return self.client.service.dummy()
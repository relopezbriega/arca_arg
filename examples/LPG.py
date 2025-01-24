import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_arg.wsService import ArcaWebService 
from arca_arg.settings import WSDL_LPG_HOM, WS_LIST

if __name__ == "__main__":
    arca_service = ArcaWebService(ArcaWebService, 'wslpg') # Instancia del servicio web

    print(arca_service.server_status()) # Check server status

    
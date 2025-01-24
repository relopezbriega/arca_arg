import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_arg.wsService import ArcaWebService 
from arca_arg.settings import WSDL_CPE_HOM, WS_LIST


if __name__ == "__main__":
    
    
    #print(WS_LIST) # Lista de servicios
    
    arca_service = ArcaWebService(WSDL_CPE_HOM, 'wscpe') # Instancia del servicio web
    #print(arca_service.listMethods()) # Lista de métodos del servicio inicializado
    print(arca_service.methodHelp('aceptarEmisionDestinoDG')) # Ayuda con el método consultarProvincias del servicio web
    print(arca_service.elementDetails('ns0:AceptarEmisionDestinoDGSolicitud'))
  
    
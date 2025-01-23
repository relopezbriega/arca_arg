import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_api.ws_sr_constancia_inscripcion import ConstanciaService

if __name__ == "__main__":
    arca_service = ConstanciaService()
    cuit_a_consultar = "20201731594"
    cuits = ["20224107030", "27015942210", "12345678901"]
    
    print(arca_service.server_status()) # Check server status
    print(f"Consultando CUIT: {cuit_a_consultar}...")
    #respuesta = arca_service.consultar_cuit(cuit_a_consultar)
    #print("Respuesta AFIP:", respuesta)
    
    print(f"Consultando lista de CUITs: {cuits}...")
    respuesta = arca_service.consultar_lista_cuits(cuits)
    print("Respuesta AFIP:", respuesta)
    
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_api.ws_sr_padron_a10 import PadronA10Service

if __name__ == "__main__":
    arca_service = PadronA10Service()
    cuit_a_consultar = "20201731594"

    print(arca_service.server_status()) # Check server status
    print(f"Consultando CUIT: {cuit_a_consultar}...")
    respuesta = arca_service.consultar_cuit(cuit_a_consultar)
    print("Respuesta AFIP:", respuesta)
    
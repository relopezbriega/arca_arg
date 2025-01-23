import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_api.wsfev1 import FEV1Service, FeCabReq, FECAEDetail, AlicIva, FERequest

if __name__ == "__main__":
    arca_service = FEV1Service()

    #print(arca_service.server_status()) # Check server status
    #print(arca_service.consultar_actividades())
    #print(arca_service.consultar_tipos_documentos())
    #print(arca_service.consultar_tipos_cbte())
    #print(arca_service.consultar_puntos_venta())
    #print(arca_service.consultar_tipos_iva())
    #print(arca_service.consultar_tipos_tributos())
    #print(arca_service.consultar_tipos_opcionales())
    #print(arca_service.consultar_tipos_moneda())
    #print(arca_service.consultar_tipos_conceptos())
    #print(arca_service.consultar_max_request())
    #print(arca_service.consultar_cotizacion_moneda("DOL"))
    data_cbte = { 
                 'PtoVta': 1,
                'CbteTipo': 1,
                'CbteNro': 13,
    }  
    #print(arca_service.consultar_CAE(data_cbte))          
    #print(arca_service.consultar_CAEA(202501, 2))  
    print(arca_service.consultar_ultimo_cbte(1, 1))
    #print(arca_service.consultar_caea_sin_movimiento("11111111111111", 1))
    #print(arca_service.informar_caea_sin_movimiento("11111111111111", 1))
    
    # Crear un comprobante
    cabecera = FeCabReq(
        CantReg=1,
        PtoVta=1,
        CbteTipo=1
    )
    
    iva = AlicIva(Id=5, BaseImp=100, Importe=21)
    
    detalle = FECAEDetail(
        Concepto=1,
        DocTipo=80,
        DocNro=27293188217,
        CbteDesde=3,
        CbteHasta=3,
        CbteFch="20250121",
        ImpTotal=121,
        ImpTotConc=0,
        ImpNeto=100,
        ImpOpEx=0,
        ImpIVA=21,
        ImpTrib=0,
        MonId="PES",
        MonCotiz=1,
        Iva=iva,
    )
    
    request = FERequest(cabecera, detalle)
    
    #print(request)
    
    print(arca_service.solicitar_CAE(request))
    #print(arca_service.solicitar_CAEA(202501, 2))
    
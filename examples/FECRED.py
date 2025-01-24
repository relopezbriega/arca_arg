import sys
import os
from dataclasses import asdict

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_api.wsfecred import FECREDService, idComprobante, FECredActeptar, idCtaCte, motivoRechazo

if __name__ == "__main__":
    arca_service = FECREDService()

    #print(arca_service.server_status()) # Check server status

    #print(arca_service.consultarMontoObligadoRecepcion("30506792165", "2025-01-25")) 
    #print(arca_service.consultarTiposRetenciones())
    #print(arca_service.consultarTiposMotivosRechazo())
    #print(arca_service.consultarTiposFormasCancelacion())
    #print(arca_service.consultarTiposAjustesOperacion())
    #print(arca_service.modificarOpcionTransferencia(1, 'ADC'))
    #print(arca_service.consultarComprobantes("Emisor"))
    #print(arca_service.consultarCtaCte(idCtaCte=1))
    #print(arca_service.consultarCtasCtes("Receptor"))
    #print(arca_service.consultarCuentasEnAgtDptoCltv())
    #print(arca_service.consultarFacturasAgtDptoCltv(idCtaCte=1))
    
    cpbte= asdict(idComprobante(
        CUITEmisor="30506792165",
        codTipoCmp=1,
        ptoVta=1,
        nroCmp=1
    ))
    #print(cpbte)
    #print(arca_service.consultarHistorialEstadosComprobante(cpbte))
    #print(arca_service.consultarHistorialEstadosCtaCte(1))
    ctacte = idCtaCte(codCtaCte=1)
    data = asdict(FECredActeptar(
        idCtaCte=ctacte,
        saldoAceptado=1000,
        codMoneda='PES',
        cotizacionMonedaUlt=1,
    ))        
    #print(arca_service.aceptarFECred(**data)) ## revisar
    rechazo = asdict(motivoRechazo(
        codMotivo=6,
        descMotivo="Falta de entrega de la mercadería o prestación del servicio",
        justificacion="Justificacion"
    ))
    
    #print(arca_service.rechazarFECred(1, rechazo)) 
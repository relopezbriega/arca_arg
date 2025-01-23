from .ws_service import ArcaWebService
from .settings import PROD, WSDL_FEV1_HOM, WSDL_FEV1_PROD, CUIT
from typing import Any, Dict
from dataclasses import dataclass, asdict

WSDL_FEV1 = WSDL_FEV1_HOM if not PROD else WSDL_FEV1_PROD
SERVICE_NAME = "wsfe"

"""A continuación se presentan las clases y métodos para trabajar con la Factura Electrónica de ARCA."""
@dataclass
class CbtesAsocs:
    Tipo: int
    PtoVta: int
    Nro: int
    Cuit: str = None # Opcional
    CbteFch: str = None # Opcional

@dataclass 
class Tributo:
    Id: int
    BaseImp: float
    Alic: float
    Importe: float
    Desc: str = None # Opcional

@dataclass
class AlicIva:
    Id: int
    BaseImp: float
    Importe: float
    
@dataclass
class Opcional:
    Id: int
    Valor: str

@dataclass
class Comprador:
    DocTipo: int
    DocNro: int
    Porcentaje: float

@dataclass
class PeriodoAsocs:
    FchDesde: str
    FchHasta: str

@dataclass
class Actividad:
    Id: int
    
@dataclass
class FeCabReq:
    CantReg: int
    PtoVta: int
    CbteTipo: int

@dataclass
class FECAEDetail:
    """
    Maneja los datos de una factura electrónica.
    
    Esta clase maneja los datos de una factura electrónica para el sistema tributario de Argentina.
    
    Atributos:
        data (Dict): Datos de la factura electrónica
    """
    Concepto: int
    DocTipo: int
    DocNro: int
    CbteDesde: int
    CbteHasta: int
    ImpTotal: float
    ImpTotConc: float
    ImpNeto: float
    ImpOpEx: float
    ImpTrib: float
    ImpIVA: float
    MonId: str
    MonCotiz: float
    CbteFch: str = None # Opcional
    FchServDesde: str = None # Opcional
    FchServHasta: str = None # Opcional
    FchVtoPago: str = None # Opcional
    CanMisMonExt: str = None # Opcional
    CondicionIVAReceptorId: int = None # Opcional
    CbtesAsoc: CbtesAsocs = None # Opcional
    Tributos: Tributo = None # Opcional
    Iva: AlicIva = None # Opcional
    Opcionales: Opcional = None # Opcional
    Compradores: Comprador = None # Opcional
    PeriodoAsoc: PeriodoAsocs = None # Opcional
    Actividades: Actividad = None # Opcional

@dataclass
class FECAEDetRequest:
    FECAEDetRequest: FECAEDetail
    
@dataclass
class FeCAEReq:
    FeCabReq: FeCabReq
    FeDetReq: FECAEDetRequest
    
def FERequest(cabecera: FeCabReq, detalle: FECAEDetail) -> Dict[str, Any]:
    """
    Crea un request para una factura electrónica.

    Args:
        cabecera (FeCabReq): dataclass con la cabecera
        detalle (FECAEDetail): dataclass con el detalle

    Returns:
        Dict[str, Any]: Dict con los datos para el request de la factura electrónica
    """
    if detalle.Iva is not None:
        detalle.Iva = {'AlicIva':detalle.Iva}
    
    if detalle.Tributos is not None:
        detalle.Tributos = {'Tributo':detalle.Tributos}
        
    if detalle.Opcionales is not None:
        detalle.Opcionales = {'Opcional':detalle.Opcionales}
    
    if detalle.Compradores is not None:
        detalle.Compradores = {'Comprador':detalle.Compradores}
    
    if detalle.Actividades is not None:
        detalle.Actividades = {'Actividad':detalle.Actividades}
        
    if detalle.CbtesAsoc is not None:
        detalle.CbtesAsoc = {'CbtesAsoc':detalle.CbtesAsoc}
        
    
    return asdict(FeCAEReq(
        FeCabReq=cabecera,
        FeDetReq={'FECAEDetRequest': detalle}
    ))

class FEV1Service(ArcaWebService):
    """
    Servicio para manejar el servicio de Factura Electrónica de ARCA.
    
    Esta clase proporciona métodos para trabajar con facturas electrónicas en el sistema tributario de Argentina.
    
    Hereda de:
        ArcaWebService: Clase base para interacciones con servicios web de ARCA
    """
    
    def __init__(self) -> None:
        """Inicializa el servicio de estado de inscripción."""
        super().__init__(WSDL_FEV1, SERVICE_NAME)
        self.cuit = CUIT
    
    def call_method(self, method_name, **kwargs):
        """
        Llama a un método del servicio web con parámetros de autenticación.

        Args:
            method_name: Nombre del método SOAP a llamar
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            La respuesta del método del servicio web
        """
        auth_data = {
            'Token': self.token,
            'Sign': self.sign,
            'Cuit': self.cuit
        }
        return getattr(self.client.service, method_name)(Auth=auth_data, **kwargs)
    
    def server_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del servidor de ARCA.

        Returns:
            Dict que contiene información del estado del servidor incluyendo
            servidor de aplicaciones, servidor de base de datos y estado de autenticación
        """
        return self.client.service.FEDummy()
    
    def solicitar_CAE(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Solicita un CAE para una factura.

        Args:
            data: Dict que contiene los datos de la factura

        Returns:
            Dict que contiene los datos del CAE
        """
        return self.call_method("FECAESolicitar", FeCAEReq=data)
    
    def solicitar_CAEA(self, periodo: int, orden: int) -> Dict[str, Any]:
        """
        Solicita un CAEA Código de Autorización electrónico anticipado para un período.

        Args:
            data: Dict que contiene los datos del período

        Returns:
            Dict que contiene los datos del CAEA
        """
        return self.call_method("FECAEASolicitar", Periodo=periodo, Orden=orden)
    
    def consultar_CAE(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Consulta el estado de un CAE.

        Args:
            data: Dict que contiene los datos del CAE

        Returns:
            Dict que contiene el estado del CAE
        """
        return self.call_method("FECompConsultar", FeCompConsReq=data)
    
    def consultar_CAEA(self, periodo: int, orden: int) -> Dict[str, Any]:
        """
        Consulta el estado de un CAEA.

        Args:
            data: Dict que contiene los datos del CAEA

        Returns:
            Dict que contiene el estado del CAEA
        """
        return self.call_method("FECAEAConsultar", Periodo=periodo, Orden=orden)
    
    def consultar_tipos_cbte(self) -> Dict[str, Any]:
        """
        Consulta los tipos de comprobantes disponibles.

        Returns:
            Dict que contiene los tipos de comprobantes disponibles
        """
        return self.call_method("FEParamGetTiposCbte")
    
    def consultar_tipos_conceptos(self) -> Dict[str, Any]:
        """
        Consulta los conceptos disponibles.

        Returns:
            Dict que contiene los conceptos disponibles
        """
        return self.call_method("FEParamGetTiposConcepto")
    
    def consultar_tipos_documentos(self) -> Dict[str, Any]:
        """
        Consulta los tipos de documentos disponibles.

        Returns:
            Dict que contiene los tipos de documentos disponibles
        """
        return self.call_method("FEParamGetTiposDoc")
    
    def consultar_tipos_iva(self) -> Dict[str, Any]:    
        """
        Consulta los tipos de IVA disponibles.

        Returns:
            Dict que contiene los tipos de IVA disponibles
        """
        return self.call_method("FEParamGetTiposIva")
    
    def consultar_tipos_moneda(self) -> Dict[str, Any]:
        """
        Consulta los tipos de moneda disponibles.

        Returns:
            Dict que contiene los tipos de moneda disponibles
        """
        return self.call_method("FEParamGetTiposMonedas")
    
    def consultar_tipos_opcionales(self) -> Dict[str, Any]:
        """
        Consulta los tipos opcionales disponibles.

        Returns:
            Dict que contiene los tipos opcionales disponibles
        """
        return self.call_method("FEParamGetTiposOpcional")
    
    def consultar_tipos_tributos(self) -> Dict[str, Any]:
        """
        Consulta los tipos de tributos disponibles.

        Returns:
            Dict que contiene los tipos de tributos disponibles
        """
        return self.call_method("FEParamGetTiposTributos")
    
    def consultar_puntos_venta(self) -> Dict[str, Any]:
        """
        Consulta los puntos de venta disponibles.

        Returns:
            Dict que contiene los puntos de venta disponibles
        """
        return self.call_method("FEParamGetPtosVenta")
    
    def consultar_cotizacion_moneda(self, moneda: str) -> Dict[str, Any]:
        """
        Consulta la cotización de una moneda.

        Args:
            moneda: Código de la moneda

        Returns:
            Dict que contiene la cotización de la moneda
        """
        return self.call_method("FEParamGetCotizacion", MonId=moneda)
    
    def consultar_actividades(self) -> Dict[str, Any]:
        """
        Consulta las actividades disponibles.

        Returns:
            Dict que contiene las actividades disponibles
        """
        return self.call_method("FEParamGetActividades")
    
    def consultar_ultimo_cbte(self, pto_venta: int, cbte_tipo: int) -> Dict[str, Any]:
        """
        Consulta el último número de comprobante.

        Args:
            pto_venta: Punto de venta
            cbte_tipo: Tipo de comprobante

        Returns:
            Dict que contiene el último número de comprobante
        """
        return self.call_method("FECompUltimoAutorizado", PtoVta=pto_venta, CbteTipo=cbte_tipo)
    
    def consultar_caea_sin_movimiento(self, CAEA: str, pto_venta: int) -> Dict[str, Any]:
        """
        Consulta el CAEA sin movimiento.

        Args:
            data: Dict que contiene los datos del CAEA

        Returns:
            Dict que contiene los datos del CAEA
        """
        return self.call_method("FECAEASinMovimientoConsultar", CAEA=CAEA, PtoVta=pto_venta)
    
    def informar_caea_sin_movimiento(self, CAEA: str, pto_venta: int) -> Dict[str, Any]:
        """
        Informa el CAEA sin movimiento.

        Args:
            data: Dict que contiene los datos del CAEA

        Returns:
            Dict que contiene los datos del CAEA
        """
        return self.call_method("FECAEASinMovimientoInformar", CAEA=CAEA, PtoVta=pto_venta)
    
    def informar_comprobantes_CAEA(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Este método permite informar para cada CAEA otorgado, la totalidad de los comprobantes 
        emitidos y asociados a cada CAEA

        Args:
            data: Dict que contiene los datos del comprobante

        Returns:
            Dict que contiene los datos del comprobante
        """
        return self.call_method("FECAEARegInformativo", data)
    
    def consultar_max_request(self) -> Dict[str, Any]:
        """
        Consultar la cantidad máxima de registros que se podrá incluir en un request
        al método FECAESolicitar / FECAEARegInformativo.

        Returns:
            Dict que contiene el máximo de request
        """
        return self.call_method("FECompTotXRequest")
from .ws_service import ArcaWebService
from .settings import PROD, WSDL_FECRED_HOM, WSDL_FECRED_PROD, CUIT
from typing import Any, Dict
from dataclasses import dataclass

WSDL_FECRED = WSDL_FECRED_HOM if not PROD else WSDL_FECRED_PROD
SERVICE_NAME = "wsfecred"

@dataclass
class idComprobante:
    """
    Clase para manejar el ID de un comprobante de Factura de Crédito Electrónica MiPyME.
    
    Esta clase proporciona un objeto para manejar el ID de un comprobante de Factura de Crédito Electrónica
    en el sistema tributario de Argentina.
    
    Atributos:
        CUITEmisor: Cuit del emisor del comprobante
        codTipoCmp: codigo del tipo de comprobante
        ptoVta: Punto de venta del comprobante
        nroCmp: Número del comprobante
    """
    CUITEmisor: str
    codTipoCmp: int
    ptoVta: int
    nroCmp: int
    
@dataclass
class FECredActeptar:
    """
    Clase para manejar la aceptación de una Factura de Crédito Electrónica MiPyME.
    """
    idCtaCte: int
    saldoAceptado: int
    codMoneda: str
    cotizacionMonedaUlt: int
    
@dataclass
class motivoRechazo:
    """
    Clase para manejar un motivo de rechazo de una Factura de Crédito Electrónica MiPyME.
    """
    codMotivo: int
    descMotivo: str
    justificacion: str

class FECREDService(ArcaWebService):
    """
    Servicio para manejar el servicio de Factura de Crédito Electrónica MiPyME de ARCA.
    
    Esta clase proporciona métodos para trabajar con la Factura de Crédito Electrónica MiPyME
    en el sistema tributario de Argentina.
    
    Hereda de:
        ArcaWebService: Clase base para interacciones con servicios web de ARCA
    """
    
    def __init__(self) -> None:
        """Inicializa el servicio de estado de inscripción."""
        super().__init__(WSDL_FECRED, SERVICE_NAME)
    
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
            'token': self.token,
            'sign': self.sign,
            'cuitRepresentada': CUIT
        }
        return getattr(self.client.service, method_name)(authRequest=auth_data, **kwargs)
    
    def server_status(self) -> Dict[str, Any]:
        """
        Verifica el estado del servidor de ARCA.

        Returns:
            Dict que contiene información del estado del servidor incluyendo
            servidor de aplicaciones, servidor de base de datos y estado de autenticación
        """
        return self.client.service.dummy()
    
    def aceptarFECred(self, data, **kwargs) -> Dict[str, Any]:
        """
        Acepta una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la aceptación de la Factura de Crédito Electrónica
        """
        return self.call_method("aceptarFECred",
                                data,
                                **kwargs)
    
    def rechazarFECred(self, idCtaCte: int, arrayMotivosRechazo: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Consulta una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            idCtaCte: ID de la cuenta corriente
            arrayMotivosRechazo: Array de motivos de rechazo

        Returns:
            Dict que contiene la respuesta de la consulta de la Factura de Crédito Electrónica
        """
        return self.call_method("rechazarFECred", 
                                idCtaCte={'codCtaCte':idCtaCte},
                                arrayMotivosRechazo = {'motivoRechazo': arrayMotivosRechazo},
                                **kwargs)
    
    def rechazarNotaDC(self, **kwargs) -> Dict[str, Any]:
        """
        Rechaza una Nota de Débito/Crédito.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta del rechazo de la Nota de Débito/Crédito
        """
        return self.call_method("rechazarNotaDC", **kwargs)
    
    def informarFacturaAgtDptoCltv(self, **kwargs) -> Dict[str, Any]:
        """
        Informa una Factura de Agente de Depósito de Clientes.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la información de la Factura de Agente de Depósito de Clientes
        """
        return self.call_method("informarFacturaAgtDptoCltv", **kwargs)
    
    def informarCancelacionTotalFECred(self, **kwargs) -> Dict[str, Any]:
        """
        Informa la cancelación total de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la cancelación total de la Factura de Crédito Electrónica
        """
        return self.call_method("informarCancelacionTotalFECred", **kwargs)
    
    def modificarOpcionTransferencia(self, idCtaCte: int, opcionTransferencia: str, **kwargs) -> Dict[str, Any]:
        """
        Modifica la opción de transferencia de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            idCtaCte: ID de la cuenta corriente
            opcionTransferencia: 'ADC' o 'SCA'

        Returns:
            Dict que contiene la respuesta de la modificación de la opción de transferencia
        """
        return self.call_method("modificarOpcionTransferencia", 
                                idCtaCte={'codCtaCte':idCtaCte}, 
                                opcionTransferencia=opcionTransferencia,
                                **kwargs)
    
    def consultarComprobantes(self, rolCUITRepresentada: str, **kwargs) -> Dict[str, Any]:
        """
        Consulta los comprobantes de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            rolCUITRepresentada: CUIT del rol representado "Emisor" o "Receptor"

        Returns:
            Dict que contiene la respuesta de la consulta de los comprobantes
        """
        return self.call_method("consultarComprobantes",
                                rolCUITRepresentada=rolCUITRepresentada,
                                **kwargs)
    
    def consultarCtasCtes(self, rolCUITRepresentada: str, **kwargs) -> Dict[str, Any]:
        """
        Consulta las cuentas corrientes de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            rolCUITRepresentada: CUIT del rol representado "Emisor" o "Receptor"

        Returns:
            Dict que contiene la respuesta de la consulta de las cuentas corrientes
        """
        return self.call_method("consultarCtasCtes",
                                rolCUITRepresentada=rolCUITRepresentada,
                                **kwargs)
    
    def consultarCtaCte(self, idCtaCte: int, **kwargs) -> Dict[str, Any]:
        """
        Consulta la cuenta corriente de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            idCtaCte: ID de la cuenta corriente

        Returns:
            Dict que contiene la respuesta de la consulta de la cuenta corriente
        """
        return self.call_method("consultarCtaCte", 
                                 idCtaCte={'codCtaCte':idCtaCte},
                                 **kwargs)
    
    def consultarCuentasEnAgtDptoCltv(self, **kwargs) -> Dict[str, Any]:
        """
        Consulta las cuentas en Agente de Depósito de Clientes.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta de las cuentas en Agente de Depósito de Clientes
        """
        return self.call_method("consultarCuentasEnAgtDptoCltv", **kwargs)
    
    def consultarMontoObligadoRecepcion(self, cuitConsultada: str, fechaEmision: str, **kwargs) -> Dict[str, Any]:
        """
        Consulta el monto obligado de recepción de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            cuitConsultada: CUIT a consultar
            fechaEmision: Fecha de emisión de la factura

        Returns:
            Dict que contiene la respuesta de la consulta del monto obligado de recepción
        """
        return self.call_method("consultarMontoObligadoRecepcion", 
                                cuitConsultada=cuitConsultada, fechaEmision=fechaEmision, **kwargs)
    
    def consultarTiposRetenciones(self, **kwargs) -> Dict[str, Any]:
        """
        Consulta los tipos de retenciones de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta de los tipos de retenciones
        """
        return self.call_method("consultarTiposRetenciones", **kwargs)
    
    def consultarTiposMotivosRechazo(self, **kwargs) -> Dict[str, Any]:
        """
        Consulta los tipos de motivos de rechazo de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta de los tipos de motivos de rechazo
        """
        return self.call_method("consultarTiposMotivosRechazo", **kwargs)
    
    def consultarFacturasAgtDptoCltv(self, idCtaCte: int, **kwargs) -> Dict[str, Any]:
        """
        Consulta las facturas de Agente de Depósito de Clientes.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            idCtaCte: ID de la cuenta corriente

        Returns:
            Dict que contiene la respuesta de la consulta de las facturas de Agente de Depósito de Clientes
        """
        return self.call_method("consultarFacturasAgtDptoCltv", 
                                idCtaCte={'codCtaCte':idCtaCte},
                                **kwargs)
    
    def consultarTiposFormasCancelacion(self, **kwargs) -> Dict[str, Any]:
        """
        Consulta los tipos de formas de cancelación de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta de los tipos de formas de cancelación
        """
        return self.call_method("consultarTiposFormasCancelacion", **kwargs)
    
    def obtenerRemitos(self, **kwargs) -> Dict[str, Any]:
        """
        Obtiene los remitos de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la obtención de los remitos
        """
        return self.call_method("obtenerRemitos", **kwargs)
    
    def consultarHistorialEstadosComprobante(self, idComprobante: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Consulta el historial de estados de un comprobante de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta del historial de estados del comprobante
        """
        return self.call_method("consultarHistorialEstadosComprobante",
                                idComprobante=idComprobante,
                                **kwargs)
    
    def consultarHistorialEstadosCtaCte(self, idCtaCte: int, **kwargs) -> Dict[str, Any]:
        """
        Consulta el historial de estados de una cuenta corriente de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP
            idCtaCte: ID de la cuenta corriente

        Returns:
            Dict que contiene la respuesta de la consulta del historial de estados de la cuenta corriente
        """
        return self.call_method("consultarHistorialEstadosCtaCte",
                                idCtaCte={'codCtaCte': idCtaCte},
                                **kwargs)
    
    def consultarTiposAjustesOperacion(self, **kwargs) -> Dict[str, Any]:
        """
        Consulta los tipos de ajustes de operación de una Factura de Crédito Electrónica MiPyME.

        Args:
            **kwargs: Parámetros adicionales para el método SOAP

        Returns:
            Dict que contiene la respuesta de la consulta de los tipos de ajustes de operación
        """
        return self.call_method("consultarTiposAjustesOperacion", **kwargs)
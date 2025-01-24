# ARCA_ARG Settings
CERT_PATH = "data/arcaTestCert.pem" # Carpeta con el path al certificado
PRIVATE_KEY_PATH = "data/raulotest.key" # Carpeta con el path a la clave privada
TA_FILES_PATH = "data/"  # Carpeta con el path a los archivos TA
CUIT = "20293188204"  # Reemplazar con el CUIT del contribuyente
PROD = False  # Cambiar a True para producción

# Lista de los servicios disponibles en ARCA
WS_LIST =['ws_sr_constancia_inscripcion', 'ws_sr_padron_a10', 'wsfecred', 'wsfe', 'wslpg', 'wscpe']

# WSAA
WSDL_WSAA_HOM = "https://wsaahomo.afip.gov.ar/ws/services/LoginCms?wsdl" 
WSDL_WSAA_PROD = "https://wsaa.afip.gov.ar/ws/services/LoginCms?WSDL"

# WS_SR_CONSTANCIA_INSCRIPCION
WSDL_CONSTANCIA_HOM ="https://awshomo.afip.gov.ar/sr-padron/webservices/personaServiceA5?wsdl" 
WSDL_CONSTANCIA_PROD ="https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA5?wsdl" 

# WS_SR_PADRON_A10
WSDL_PADRON_A10_HOM = "https://awshomo.afip.gov.ar/sr-padron/webservices/personaServiceA10?wsdl"
WSDL_PADRON_A10_PROD = "https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA10?wsdl"

# WSFEv1 Factura Electronica
WSDL_FEV1_HOM = "https://wswhomo.afip.gov.ar/wsfev1/service.asmx?WSDL"
WSDL_FEV1_PROD = "https://servicios1.afip.gov.ar/wsfev1/service.asmx?WSDL"

# WSFECRED 
WSDL_FECRED_HOM = "https://fwshomo.afip.gov.ar/wsfecred/FECredService?wsdl"
WSDL_FECRED_PROD = "https://serviciosjava.afip.gob.ar/wsfecred/FECredService?wsdl"

# WSLPG Liquidacion Primaria de Granos
WSDL_LPG_HOM = "https://fwshomo.afip.gov.ar/wslpg/LpgService?wsdl"
WSDL_LPG_PROD = "https://serviciosjava.afip.gob.ar/wslpg/LpgService?wsdl"

# WSCPE Carta de Porte Electronica
WSDL_CPE_HOM = "https://cpea-ws-qaext.afip.gob.ar/wscpe/services/soap?wsdl"
WSDL_CPE_PROD = "https://cpea-ws.afip.gob.ar/wscpe/services/soap?wsdl"
# ARCA API Settings
CERT_PATH = "data/arcaTestCert.pem"
PRIVATE_KEY_PATH = "data/raulotest.key"
TA_FILES_PATH = "data/"  # Authorization Token storage path
CUIT = "20293188204"  # Replace with your taxpayer ID
PROD = False  # Change to True for production environment

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
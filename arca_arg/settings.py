# ARCA_ARG Settings
CERT_PATH = "data/arcaTestCert.pem" # Carpeta con el path al certificado
PRIVATE_KEY_PATH = "data/raulotest.key" # Carpeta con el path a la clave privada
TA_FILES_PATH = "data/"  # Carpeta con el path a los archivos TA
CUIT = "20293188204"  # Reemplazar con el CUIT del contribuyente
PROD = False  # Cambiar a True para producción

DOCS_URL = 'https://www.afip.gob.ar/ws/documentacion/arquitectura-general.asp'

# Lista de los servicios disponibles en ARCA
WS_LIST =['ws_sr_constancia_inscripcion'
          ,'ws_sr_padron_a10'
          ,'ws_sr_padron_a13'
          ,'wsfecred'
          ,'wsfe'
          ,'wsfex'
          ,'wslpg'
          ,'wscpe'
          ,'wsapoc'
          ,'wsagr'
          ,'wsrgiva'
          ,'wsct'
          ,'sire-ws'
          ,'wsremharina'
          ,'wsremazucar'
          ,'wsremcarne'
          ,'wsmtxca'
          ]

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

# WS_SR_PADRON_A13
WSDL_PADRON_A13_HOM = "https://awshomo.afip.gov.ar/sr-padron/webservices/personaServiceA13?WSDL"
WSDL_PADRON_A13_PROD = "https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA13?WSDL"

# WSAPOC
WSDL_APOC_HOM = "https://eapoc-ws-qaext.afip.gob.ar/Service.asmx?WSDL"
WSDL_APOC_PROD = "https://eapoc-ws.afip.gob.ar/service.asmx"

# WSFEXV1
WSDL_FEXV1_HOM = "https://wswhomo.afip.gov.ar/wsfexv1/service.asmx?WSDL"
WSDL_FEXV1_PROD = "https://servicios1.afip.gov.ar/wsfexv1/service.asmx?WSDL"

# WSAGR
WSDL_AGR_HOM = "https://wswhomo.afip.gov.ar/wsagr/wsagr.asmx?WSDL"
WSDL_AGR_PROD = "https://servicios1.afip.gov.ar/wsagr/wsagr.asmx?WSDL"

# WSRGIVA
WSDL_RGIVA_HOM = "https://fwshomo.afip.gov.ar/wsrgiva/services/RegimenPercepcionIVAService?wsdl"
WSDL_RGIVA_PROD = "https://servicios1.afip.gov.ar/wsrgiva/wsrgiva.asmx?WSDL"

# WSCT
WSDL_CT_HOM = "https://fwshomo.afip.gov.ar/wsct/CTService?wsdl"
WSDL_CT_PROD = "https://serviciosjava.afip.gob.ar/wsct/CTService?wsdl"

# SIRE-WS
WSDL_SIRE_HOM = "https://ws-aplicativos-reca.homo.afip.gob.ar/sire/ws/v1/c2005/2005?wsdl"
WSDL_SIRE_PROD = "https://ws-aplicativos-reca.afip.gob.ar/sire/ws/v1/c2005/2005?wsdl"

# WSREMHARINA
WSDL_REMHARINA_HOM ="https://fwshomo.afip.gov.ar/wsremharina/RemHarinaService?wsdl"
WSDL_REMHARINA_PROD = "https://serviciosjava.afip.gob.ar/wsremharina/RemHarinaService?wsdl"

# WSREMAZUCAR
WSDL_REMAZUCAR_HOM = "https://fwshomo.afip.gov.ar/wsremazucar/RemAzucarService?wsdl"
WSDL_REMHARINA_PROD = "https://serviciosjava.afip.gob.ar/wsremazucar/RemAzucarService"

# WSREMCARNE
WSDL_REMCARNE_HOM = "https://fwshomo.afip.gov.ar/wsremcarne/RemCarneService?"
WSDL_REMCARNE_PROD = "https://serviciosjava.afip.gob.ar/wsremcarne/RemCarneService?wsdl"

# WSMTXCA
WSDL_MTXCA_HOM = "https://fwshomo.afip.gov.ar/wsmtxca/services/MTXCAService?wsdl" 
WSDL_MTXCA_PROD = "https://serviciosjava.afip.gob.ar/wsmtxca/services/MTXCAService?wsdl"


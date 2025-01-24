# Cliente de Servicios Web de ARCA

Cliente en Python para acceder a los servicios web de ARCA (Administración Federal de Ingresos Públicos de Argentina). Maneja la autenticación y la comunicación con los servicios SOAP de ARCA.

# Características

- Gestión de tokens de autenticación
- Integración con servicios SOAP de ARCA
- Consultas de metodos y elementos
- Soporte para entornos de producción y prueba

## Requisitos

- Python 3.8+
- cryptography
- zeep
- python-dateutil
- Certificados de ARCA (prueba o producción)

## Instalación

```bash
pip install arca_arg
```
## Configuración


1. Configurar los ajustes en `settings.py`:
```
CUIT = "TU_CUIT_AQUI"
PROD = False  # True para producción
CERT_PATH = "carpeta con el certificado de arca"
PRIVATE_KEY_PATH = "Carpeta con el la clave privada"
TA_FILES_PATH="donde se guardaran temporalmente los token de acceso"
```
## Uso

```python
import arca_arg.settings as confg

confg.PRIVATE_KEY_PATH = 'key/test.key'
confg.CERT_PATH = 'cert/TestCert.pem'
confg.TA_FILES_PATH = '/ta/'
confg.CUIT = '20293188204'

from arca_arg.wsService import ArcaWebService 
from arca_arg.settings import WSDL_FEV1_HOM, WS_LIST

arca_service = ArcaWebService(WSDL_FEV1_HOM, 'wsfe')  # Instancia del servicio web
print(arca_service.listMethods()) # Lista de métodos del servicio inicializado
print(arca_service.methodHelp('FECAESolicitar')) # Ayuda con el método consultarProvincias del servicio web
print(arca_service.elementDetails('ns0:FECAEDetRequest')) # Ayuda de composición del elemento a enviar.

auth = {'Token': arca_service.token, 'Sign': arca_service.sign, 'Cuit': arca_service.cuit,}
cabecera = { 'CantReg': 1, 'PtoVta': 1, 'CbteTipo':1}
detalle = {
        'Concepto' : 1,
        'DocTipo' : 80,
        'DocNro': 27293188217,
        'CbteDesde': 4,
        'CbteHasta': 4,
        'CbteFch': "20250124",
        'ImpTotal':121,
        'ImpTotConc': 0,
        'ImpNeto': 100,
        'ImpOpEx': 0,
        'ImpIVA': 21,
        'ImpTrib': 0,
        'MonId': "PES",
        'MonCotiz':1,
        'Iva': {'AlicIva': {'Id': 5, 'BaseImp': 100, 'Importe': 21}}
}
# preparando los datos a enviar al ws
data = {'Auth': auth, 
        'FeCAEReq': { 'FeCabReq': cabecera, 'FeDetReq': {'FECAEDetRequest': detalle}}
       }

# envio del request
arca_service.sendRequest('FECAESolicitar', data)
  
```

## Estructura del Proyecto
```
arca_arg/
├── arca_arg/
│   ├── auth.py
│   ├── settings.py
│   ├── wsService.py
└── README.md
```
## Contribuir

### Cómo Contribuir

1. Hacer un fork del [repositorio](https://github.com/relopezbriega/arca_arg)
2. Crear una rama para tu funcionalidad  (`git checkout -b feature/amazing-feature`)
3. Confirmar tus cambios (`git commit -m 'Add some amazing feature'`)
4. Subir a la rama(`git push origin feature/amazing-feature`)
5. Abrir un Pull Request

### Directrices de Desarrollo

- Seguir la guía de estilo PEP 8
- Añadir pruebas unitarias para nuevas funcionalidades
- Actualizar la documentación según sea necesario
- Usar anotaciones de tipo para el nuevo código

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Soporte

### Reporte de Problemas

Por favor, incluye la siguiente información al reportar problemas:

- Descripción detallada del problema
- Pasos para reproducir
- Comportamiento esperado vs comportamiento actual
- Versión de Python y detalles del entorno

### Contacto

- GitHub Issues: [Crear nuevo issue](https://github.com/relopezbriega/arca_arg/issues)
- Email: relopezbriega@gmail.com

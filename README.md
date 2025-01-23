# Cliente de Servicios Web de ARCA

Cliente en Python para acceder a los servicios web de ARCA (Administración Federal de Ingresos Públicos de Argentina). Maneja la autenticación y la comunicación con los servicios SOAP de ARCA.

# Características

- Gestión de tokens de autenticación
- Integración con servicios SOAP de ARCA
- Consultas de estado de inscripción de contribuyentes
- Soporte para entornos de producción y prueba

## Requisitos

- Python 3.8+
- cryptography
- Certificados de ARCA (prueba o producción)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/afip-client.git
cd afip-client

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```
## Configuración

1. Colocar los certificados en el directorio `data/`:

```
data/
├── arcaTestCert.pem  # Certificado de ARCA
└── arcaKeytest.key   # Clave privada
```

2. Configurar los ajustes en `settings.py`:
```
CUIT = "TU_CUIT_AQUI"
PROD = False  # True para producción
```
## Uso

```python
from arca_api.ws_sr_constancia_inscripcion import ConstanciaService

# Inicializar el servicio
service = ConstanciaService()

# Consultar el estado de inscripción de un contribuyente
result = service.consultar_cuit(
    cuit="20123456789",
    cuitRepresentada=""
)

# Verificar el estado del servidor
status = service.server_status()
```

## Estructura del Proyecto
```
arca_arg/
├── arca_api/
│   ├── auth.py
│   ├── settings.py
│   ├── ws_service.py
│   └── ws_sr_constancia_inscripcion.py
├── data/
├── examples/
├── tests/
├── requirements.txt
└── README.md
```
## Contribuir

### Cómo Contribuir

1. Hacer un fork del repositorio
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

### Documentación

- [Documentación de la API](docs/api.md)
- [Guía de Configuración](docs/configuration.md)
- [Ejemplos](examples/)
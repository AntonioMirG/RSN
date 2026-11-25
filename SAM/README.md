# Hello World SAM - Hora España y Temperatura Zaragoza

Función Lambda serverless que devuelve un saludo, la hora actual en España y la temperatura en Zaragoza.

## Descripción

Esta aplicación utiliza AWS SAM (Serverless Application Model) para desplegar una función Lambda en Python 3.12 que:

- Devuelve el mensaje "Hola Mundo"
- Muestra la hora actual en España (zona horaria Europe/Madrid)
- Obtiene la temperatura actual en Zaragoza usando la API pública [Open-Meteo](https://open-meteo.com/) (sin API key)

## Prerrequisitos

- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [AWS CLI](https://aws.amazon.com/cli/) configurado con credenciales
- Python 3.12
- Docker (para pruebas locales con `sam local`)

## Estructura del proyecto

```
.
├── template.yaml              # Plantilla SAM (infraestructura)
├── hello_world/
│   ├── app.py                 # Código de la función Lambda
│   └── requirements.txt       # Dependencias Python
├── events/
│   └── event.json             # Evento de prueba API Gateway
└── README.md                  # Este archivo
```

## Comandos

### Build

```bash
cd /home/isard/RSN
sam build
```

### Prueba local (invoke)

```bash
sam local invoke HelloWorldFunction --event events/event.json
```

### Prueba local con API Gateway

```bash
sam local start-api
# En otro terminal:
curl http://localhost:3000/hello
```

### Despliegue en AWS

```bash
# Primera vez (configuración interactiva)
sam deploy --guided

# Despliegues posteriores
sam deploy
```

## Ejemplo de respuesta JSON

```json
{
  "message": "Hola Mundo",
  "hora_espana": "2024-01-15 14:30:22 CET",
  "temperatura_zaragoza": 12.5,
  "unidad_temperatura": "°C"
}
```

## API

| Método | Ruta     | Descripción                          |
|--------|----------|--------------------------------------|
| GET    | /hello   | Devuelve saludo, hora y temperatura  |

## Fuentes de datos

- **Hora**: Calculada localmente con `pytz` usando la zona horaria `Europe/Madrid`
- **Temperatura**: [Open-Meteo API](https://api.open-meteo.com/v1/forecast?latitude=41.6561&longitude=-0.8773&current_weather=true) (gratuita, sin API key)

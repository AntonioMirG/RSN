import json
import datetime
import pytz
import urllib.request


def lambda_handler(event, context):
    """Lambda handler que devuelve Hola Mundo, hora en España y temperatura en Zaragoza."""

    # Obtener hora actual en España (zona horaria Europe/Madrid)
    zona_madrid = pytz.timezone('Europe/Madrid')
    ahora_madrid = datetime.datetime.now(zona_madrid)
    hora_espana = ahora_madrid.strftime('%Y-%m-%d %H:%M:%S %Z')

    # Obtener temperatura actual en Zaragoza desde Open-Meteo API
    temperatura_zaragoza = None
    unidad_temperatura = None
    try:
        url = (
            'https://api.open-meteo.com/v1/forecast'
            '?latitude=41.6561&longitude=-0.8773&current_weather=true'
        )
        with urllib.request.urlopen(url, timeout=5) as respuesta:
            datos = json.loads(respuesta.read().decode('utf-8'))
            temperatura_zaragoza = datos['current_weather']['temperature']
            unidad_temperatura = datos.get('current_weather_units', {}).get(
                'temperature', '°C'
            )
    except Exception as e:
        temperatura_zaragoza = f'Error al obtener temperatura: {str(e)}'
        unidad_temperatura = 'N/A'

    response_body = {
        'message': 'Hola Mundo',
        'hora_espana': hora_espana,
        'temperatura_zaragoza': temperatura_zaragoza,
        'unidad_temperatura': unidad_temperatura,
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(response_body, ensure_ascii=False),
    }

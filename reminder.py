"""
Este módulo envía recordatorios y consejos al usuario sobre el ahorro de energía.
El usuario recibirá notificaciones a través de la API de Pushover, 
preguntando si ha apagado las luces.
Si responde que no, recibirá un consejo para mejorar sus hábitos de ahorro energético.
"""
import time
import requests


def send_push_notification(message):
    """
    Envía una notificación push al usuario a través de la API de Pushover.
    
    Argumentos:
    message (str): El mensaje que se enviará en la notificación push.

    """
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": "asuhc5qfc3kdg1zfgt9k2pmm4q6meu",  # Sustituye con tu API Token
        "user": "ukzht9z7e6x32m97wuokjf767zsmv3",    # Sustituye con tu User Key
        "message": message
    }

    response = requests.post(url, data=data, timeout=10)
    if response.status_code == 200:
        print("Notificación enviada exitosamente!")
    else:
        print("Error al enviar la notificación:", response.status_code)

def ask_question():
    """
    Pregunta al usuario si apagó la luz del baño.
    Si responde que no, ofrece un consejo de ahorro de energía.
    """
    # Enviar la notificación inicial
    send_push_notification("¿Apagaste la luz del baño?")
    # Espera una respuesta del usuario (en este caso, por consola)
    respuesta = input("Responde con 'si' o 'no': ").strip().lower()

    # Evaluar la respuesta
    if respuesta == 'no':
        # Si la respuesta es no, envia un consejo
        send_push_notification("¡Recuerda siempre apagar las luces cuando no las necesites para ahorrar energía!")
    elif respuesta == 'si':
        send_push_notification("¡Buen trabajo! Seguir apagando las luces cuando no las uses ayuda a conservar energía.")
    else:
        send_push_notification("Respuesta no válida. Asegúrate de responder 'sí' o 'no'.")
    time.sleep(10)  # Espera de 10 segundos entre notificaciones

def start_reminder():
    """
    Inicia un bucle que pregunta al usuario si apagó la luz y le envía un consejo si es necesario.
    """
    while True:
        ask_question()
        time.sleep(10)  # Pregunta cada 1 hora

if __name__ == "__main__":
    start_reminder()

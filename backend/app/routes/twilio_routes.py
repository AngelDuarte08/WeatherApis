from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from services.chat_service import procesar_mensaje_sms

twilio_bp = Blueprint("twilio", __name__)

@twilio_bp.route("/sms", methods=['POST'])
def sms_reply():
    # 1. Obtener el mensaje que tú enviaste 
    numero_origen = request.form.get('From')
    cuerpo_mensaje = request.form.get('Body')

    print(f"--- Nuevo Mensaje de {numero_origen}: {cuerpo_mensaje} ---")

    # 2. Procesar la respuesta usando el chatbot_service
    respuesta_texto = procesar_mensaje_sms(cuerpo_mensaje)

    # 3. Responder automáticamente usando MessagingResponse (TwiML)
    resp = MessagingResponse()
    resp.message(respuesta_texto)

    return str(resp), 200, {'Content-Type': 'application/xml'}
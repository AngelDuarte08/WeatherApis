import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Validación opcional (muy recomendable)
if not Config.GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY no está configurada en el entorno")

if not Config.TWILIO_ACCOUNT_SID:
    raise ValueError("TWILIO_ACCOUNT_SID no está configurado")

if not Config.TWILIO_AUTH_TOKEN:
    raise ValueError("TWILIO_AUTH_TOKEN no está configurado")

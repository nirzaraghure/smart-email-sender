from flask import Flask, request, jsonify
import time
import smtplib
from email.message import EmailMessage
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Smart Email Sender!"

@app.route('/send', methods=['POST'])
def send_email():
    data = request.get_json()
    to = data['to']
    subject = data['subject']
    message = data['message']

    # Simulate human typing delay
    time.sleep(3)

    try:
        email = EmailMessage()
        email['From'] = os.getenv('EMAIL_USER')
        email['To'] = to
        email['Subject'] = subject
        email.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            smtp.send_message(email)

        return jsonify({'status': 'sent'})
    except Exception as e:
        return jsonify({'status': 'fail', 'error': str(e)})

if __name__ == '__main__':
    app.run()

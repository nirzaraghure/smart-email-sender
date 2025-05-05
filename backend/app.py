from flask import Flask, request, jsonify
import time
import smtplib
from email.message import EmailMessage
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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
        # Create email message
        email = EmailMessage()
        email['From'] = os.getenv('EMAIL_USER')  # Fetch email user from environment variables
        email['To'] = to
        email['Subject'] = subject
        email.set_content(message)

        # Send email using Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))  # Fetch email password from environment variables
            smtp.send_message(email)

        return jsonify({'status': 'sent'})
    except Exception as e:
        return jsonify({'status': 'fail', 'error': str(e)})

if __name__ == '__main__':
    # Bind to correct port and host
    port = int(os.getenv("PORT", 5000))  # Get the PORT from environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)  # Run app on all interfaces (important for cloud deployments)

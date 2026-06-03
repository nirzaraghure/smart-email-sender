# tests/test_app.py

import unittest
from unittest.mock import patch, MagicMock
from backend.app import app

class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Welcome to the Smart Email Sender!")

    def test_home_route_not_found(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)

class TestSendEmailRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('backend.app.smtplib')
    def test_send_email_route_success(self, mock_smtp):
        mock_smtp.SMTP_SSL.return_value.login.return_value = None
        mock_smtp.SMTP_SSL.return_value.send_message.return_value = None

        data = {'to': 'test@example.com', 'subject': 'Test Email', 'message': 'This is a test email'}
        response = self.app.post('/send', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'sent'})

    @patch('backend.app.smtplib')
    def test_send_email_route_failure(self, mock_smtp):
        mock_smtp.SMTP_SSL.return_value.login.side_effect = Exception('Mocked exception')

        data = {'to': 'test@example.com', 'subject': 'Test Email', 'message': 'This is a test email'}
        response = self.app.post('/send', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'fail', 'error': 'Mocked exception'})

if __name__ == '__main__':
    unittest.main()
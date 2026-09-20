# Abstraction
# Reducing complexity by hiding unnecessary details

class EmailService:
    def _connect(self):
        print("Connecting to server....")

    def _authenticate(self):
        print("Authentication....")

    def send_email(self, content):
        self._connect()
        self._authenticate()
        print("Sending email.....")
        self._disconnect()

    def _disconnect(self):
        print("Message sent, disconnecting......")

email = EmailService()
email.send_email("Hello!")

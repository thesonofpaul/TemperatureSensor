import smtplib, ssl, re
from setting import Setting

class Email:

    def __init__(self):
        self.port = 465
        self.smtp_server = 'smtp.gmail.com'
        self.sender_email = 'weather.powered.email.test@gmail.com'
        self.message = """\
Subject: Temperature ALERT

Hello {} {},
The current temperature is {}. This exceeds the thresholds set between {} and {} degrees Fahrenheit.

Best,
TemperatureSensor"""

    def send_alert(self, account_list, current_temp, settings):
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            password = ''
            server.login(self.sender_email, password)
            print("Sending email...")
            self._send_email(server, account_list, current_temp, settings)

    def _send_email(self, server, account_list, current_temp, settings):
        try:
            for account in account_list:
                print("Sending email to {}".format(account))
                if self._validate_email(account.email_address):
                    message_to_send = self.message.format(account.first_name, account.last_name, current_temp, settings.min_temp, settings.max_temp)
                    server.sendmail(self.sender_email, account.email_address, message_to_send)
        except Exception as e:
            print(e)

    def _validate_email(self, email_address):
        email_regex = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
        return re.search(email_regex, email_address) is not None

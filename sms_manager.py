from twilio.rest import Client

class SMS:
    def __init__(self):
        self.account_sid = 'ACf233e286344d8981d9a92908aa5bd9de'
        self.auth_token = 'e20900566df288ba4b002ebeb50e21bf'

    def _create_client(self):
        return Client(self.account_sid, self.auth_token)

    def send_sms(self, recipient):
        client = self._create_client()
        message = client.messages.create(
            to=recipient, 
            from_="+13342265224",
            body="Hi Bearington G! I sent this through twilio!")
        print(message.sid)

if __name__ == '__main__':
    sms = SMS()
    sms.send_sms('+16037699678')

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(mensaje):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC397af4f6fe6ff9f617bf4370f48d9688'
    auth_token = '1886df1685950ccf3fdae939b8848aa1'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=mensaje,
                        from_='+12058609510',
                        to='+56944437204'
                    )

    print(message.sid)

#send('Funciona')
from Message import SMS, Email

#message = Message()
#message.content = 'Hallo Welt'
#message.send()

# Objekt Instanzierung
'''
sms = SMS(sender = 'Mark')

sms.content = 'Hallo alte SMS Welt'

## sms.content = 'Hallo alte SMS Welt'
sms.recipient = 'Alice'
print("Sender: ", sms.sender)
sms.send()
'''
user = User(id = 123)
user.read()

user.send_message(content = 'bla')

if user.preferred_message == 'email':
    email = Email(recipient = user.email)

email.content = 'bla'

email.send()
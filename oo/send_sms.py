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

email = Email(sender = 'Mark')

email.content = 'bla'
print(email.content)
email.send()
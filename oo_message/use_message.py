from Message import Message, SMS

message = Message()
message.content = 'Hallo Welt'
message.send()

# Objekt Instanzierung
sms = SMS(sender = 'Mark')
sms.content = 'Hallo SMS Welt'
sms.recipient = 'Bla'
print(sms.sender)
sms.send()



import Message

class SMS(Message):

    def __init__(self, sender):
        super(SMS, self).__init__()
        print('init')
        self.sender = sender

    @Message.content.setter
    def content(self, content):
        if (len(content) > 10):
            print("content zu gross")
        self.__content = content
        
    def send(self):
        # Message.send(self)
        super(SMS, self).send()
        print("sending sms:", self.recipient, self.__content)

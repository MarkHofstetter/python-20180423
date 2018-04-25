from abc import ABC, abstractmethod

class Message(ABC):

    recipient = None
    sender = None    
    __content = None
    
    @abstractmethod
    def __init__(self, sender = 'None'):
        print('init from parent')
        self.__content = None
        self.sender = sender
    
    @property
    def content(self):
        return self.__content
        
    @content.setter
    def content(self, content):
        self.__content = '*** ' + content
        
    def send(self):
        print("logging from class:",
          self.__class__.__name__)

class SMS(Message):

    def __init__(self, sender):
        super(SMS, self).__init__()
        # Message.__init__(self)
        print('init')
        

    @Message.content.setter
    def content(self, content):
        if (len(content) > 10):
            print("content zu gross")
        self.__content = content
        
    def send(self):
        # Message.send(self)
        super(SMS, self).send()
        print("sending sms:", self.recipient, self.__content)

class Email(Message):

    __content = None

    def __init__(self, sender):
        super(Email, self).__init__()
        
    def send(self):
        super(Email, self).send()
        print("sending email:", self.recipient, self.__content)

        
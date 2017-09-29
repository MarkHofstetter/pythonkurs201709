class Message:

    recipient = None
    sender = None    
            
    @property
    def content(self):
        return self.__content
        
    @content.setter
    def content(self, content):
        self.__content = content
        
    def send(self, channel = None):
        print("logging:", channel)

        
class SMS(Message):

    def __init__(self, sender):
        print('init')
        self.sender = sender

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        if (len(content) > 10):
            print("content zu gross")
        self.__content = content
        
    def send(self):
        Message.send(self, 'SMS')
        print("sending:", self.recipient, self.content)

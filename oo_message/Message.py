class Message:

    recipient = None
    sender = None    
    __content = None

    def __init__(self):
        print('init parent')
        self.__content = None
    
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
        super(SMS, self).__init__()
        print('init')
        self.sender = sender

    @Message.content.setter
    def content(self, content):
        if (len(content) > 10):
            print("content zu gross")
        self.__content = content
        
    def send(self):
        Message.send(self, 'SMS')
        print("sending:", self.recipient, self.content)
        
    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

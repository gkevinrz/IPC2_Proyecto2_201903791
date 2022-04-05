from telnetlib import XASCII


class NodoCamino:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.siguiente=None
        self.anterior=None

from nodocamino import NodoCamino
class Camino:
    def __init__(self):
        self.inicio=None
        self.size=0

    def actualizar(self):
        self.inicio=None
        self.size=0
    def agregarInicio(self,x,y):
        self.size+=1
        nuevaCasilla=NodoCamino(x,y)
        if self.inicio is None:
            self.inicio=nuevaCasilla
        else:
            nuevaCasilla.siguiente=self.inicio
            self.inicio.anterior=nuevaCasilla
            self.inicio=nuevaCasilla
    def buscar(self,x,y):
        actual=self.inicio
        while actual!=None:
            if actual.x==x and actual.y==y:
                return actual
            actual=actual.siguiente
        return None
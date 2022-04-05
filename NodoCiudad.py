#from ListaPatrones import ListaPatrones
from matriz import Matriz

from listacamino import Camino
class Ciudad():
    def __init__(self,nombre,filas,columnas):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.Matriz=Matriz()
        self.Camino=Camino()
        self.siguiente=None
        
    
        
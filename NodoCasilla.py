class NodoCasilla():
    def __init__(self,fila,columna,estado):
        self.Fila=fila
        self.Columna=columna
        self.Estado=estado
        self.capacidad=0
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None
        self.Visitado=False
        self.Nodo=None
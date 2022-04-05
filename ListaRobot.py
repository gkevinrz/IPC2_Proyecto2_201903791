from NodoRobot import Robot
class ListaRobot():
    def __init__(self):
        self.Inicio=None
        self.size=0
        self.robotsF=0
        self.robotsR=0
    def insetarRobot(self,nombre,tipo):
        nuevoRobot=Robot(nombre,tipo)
        self.size+=1
        if self.Inicio is None:
            self.Inicio=nuevoRobot
        else:
            temp=self.Inicio
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevoRobot

    def getRobot(self,nombrer):
        temp=self.Inicio
        while temp is not None:
            if temp.nombre==nombrer:
                return temp
            temp=temp.siguiente
        return None
    def mostrarRobots(self):
        temp=self.Inicio
        print('|        Robots Disponibles          |')
        print('......................................')
        while temp is not None:
            if temp.tipo=='ChapinFighter':
                print(temp.tipo+' | '+temp.nombre+' | '+'Capacidad: '+f'{temp.capacidad}')
            else:
                print(temp.tipo+' | '+temp.nombre)
            temp=temp.siguiente
        print('')
    def mostrarRescues(self):
        temp=self.Inicio
        print('|        Robots Disponibles          |')
        print('......................................')
        while temp is not None:
            if temp.tipo=='ChapinRescue':
                print(temp.tipo+' | '+temp.nombre+' | ')
            temp=temp.siguiente
    def mostrarFig(self):
        temp=self.Inicio
        print('|        Robots Disponibles          |')
        print('......................................')
        while temp is not None:
            if temp.tipo=='ChapinFighter':
                print(temp.tipo+' | '+temp.nombre+' | '+'Capacidad: '+f'{temp.capacidad}')
            temp=temp.siguiente
    
    def unicoResc(self):
        temp=self.Inicio
        while temp is not None:
            if temp.tipo=='ChapinRescue':
                return temp                
            temp=temp.siguiente
    def unicoF(self):
        temp=self.Inicio
        while temp is not None:
            if temp.tipo=='ChapinFighter':
                return temp                
            temp=temp.siguiente

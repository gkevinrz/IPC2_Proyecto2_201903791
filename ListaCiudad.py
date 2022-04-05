from NodoCiudad import Ciudad
class ListaCiudad():
    def __init__(self):
        self.Inicio=None
        self.size=0

    def insertarCiudad(self,nombre,filas,columnas):
        nuevaCiudad=Ciudad(nombre,filas,columnas)
        self.size+=1
        if self.Inicio is None:
            self.Inicio=nuevaCiudad
        else:
            temp=self.Inicio
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevaCiudad
    def getCiudad(self,nombrec):
        temp=self.Inicio
        while temp is not None:
            if temp.nombre==nombrec:
                return temp
            temp=temp.siguiente
        return None
    def mostrarCiudades(self):
        print('\n')
        temp=self.Inicio
        print('     |Ciudades Disponibles|')
        print('     ......................')
        while temp is not None:
            print('     Nombre: ',temp.nombre)
            temp=temp.siguiente
        print('')


  
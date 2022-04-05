from ast import NodeTransformer
from ctypes import cast
from email.headerregistry import UniqueAddressHeader
from msilib.schema import RemoveIniFile
from pickle import TRUE
#from subprocess import _TXT
from tkinter import Tk
from tkinter.messagebox import showerror, showinfo
from os import startfile, system
from turtle import rt
from ListaCiudad import ListaCiudad
from ListaRobot import ListaRobot
import time
from NodoCiudad import Ciudad
from nodo import Nodo
    #messagebox.showinfo(message="Mensaje", title="Título")
import xml.etree.ElementTree as ET
class Main():
    def __init__(self):
        #pass
        self.t=Tk()
        self.t.iconify()
        self.listaCiudad=ListaCiudad()
        self.listaRobot=ListaRobot()
        
    
    def Menu(self):
        Opcion=''
        while Opcion!='4':
            print(' ___________________________________________________')
            print('|-------------- Sistema de Control     -------------|')
            print('|   1. Cargar archivo de configuracion              |')
            print('|   2. Ejecutar mision de rescate                   |')# verificar si hay robots rescue
            print('|   3. Ejecutar mision de extraccion de recursos    |')# verificar si hay robots ataque
            print('|   4. Salir                                        |')
            print('|---------------------------------------------------|')
            Opcion=input('Seleccione una opción:\n> ')
            if Opcion=='1':
                ruta_archivo=input('Ruta del Archivo: \n > ')
                self.CargarAchivo(ruta_archivo)  
                showinfo(message="Archivo cargado", title="XML")
                self.t.iconify()
            elif Opcion=='2':
                system('cls')
                robottmp=None
                ciudadtmp=None
                CasillaInicial=None
                CasillaFinal=None
                self.listaCiudad.mostrarCiudades()
                print('Selecciona una ciudad:')
                OpcionCiudad=input('> ')
                ciudadtmp=self.listaCiudad.getCiudad(OpcionCiudad)
                print('')

                if ciudadtmp.Matriz.ucivil>1:
                    print('Punto de entrada: ')
                    print('-----------------')
                    ciudadtmp.Matriz.verEntradas()
                    print('-----------------')
                    OpcionEntradaX=input('Escriba coordenada en X: ')
                    OpcionEntradaY=input('Escriba coordenada en Y: ')
                    print('|----------------------------|')
                    print('Escoja una unidad civil:')
                    print('..........................')
                    ciudadtmp.Matriz.verCiviles()
                    print('..........................')
                    OpcionCivilX=input('Escriba coordenada en X: ')
                    OpcionCivilY=input('Escriba coordenada en Y: ')
                    print('')
                    #self.t.d|eiconify()
                    showinfo(message=f"{OpcionCiudad} seleccionado. Unidad civil encontrada ({OpcionCivilX},{OpcionCivilY}).", title="Mision de rescate")
                    self.t.iconify()
                    if self.listaRobot.robotsR>1:
                        print('Seleccione un robot:')
                        self.listaRobot.mostrarRescues()
                        OpcionRobot=input('> ')
                        showinfo(message=f"{OpcionRobot} seleccionado", title="Mision de rescate")
                        self.t.iconify()
                        robottmp=self.listaRobot.getRobot(OpcionRobot)
                    elif self.listaRobot.robotsR==1:
                        showinfo(message=f"{self.listaRobot.unicoResc().nombre} seleccionado", title="Mision de rescate")
                        self.t.iconify()
                        robottmp=self.listaRobot.unicoResc()
                    else:
                        showinfo(message="NO hay robots rescue disponibles", title="Mision de rescate")
                        self.t.iconify()
                    CasillaInicial=ciudadtmp.Matriz.getNodo(int(OpcionEntradaX),int(OpcionEntradaY))
                    CasillaFinal=ciudadtmp.Matriz.getNodo(int(OpcionCivilX),int(OpcionCivilY))
                    self.Ejecutar_Rescate(ciudadtmp,CasillaInicial,CasillaFinal,robottmp)
                    print('|------------------------------|')
                elif ciudadtmp.Matriz.ucivil==1:
                    print('Punto de entrada: ')
                    print('-----------------')
                    ciudadtmp.Matriz.verEntradas()
                    print('-----------------')
                    OpcionEntradaX=input('Escriba coordenada en X: ')
                    OpcionEntradaY=input('Escriba coordenada en Y: ')
                    print('|----------------------------|')
                    unidadcivilunica=ciudadtmp.Matriz.unidadCivil()
                    showinfo(message=f"{OpcionCiudad} seleccionado. Unidad civil encontrada ({unidadcivilunica.Fila},{unidadcivilunica.Columna}).", title="Mision de rescate")
                    if self.listaRobot.robotsR>1:
                        print('Seleccione un robot:')
                        self.listaRobot.mostrarRescues()
                        OpcionRobot=input('> ')
                        showinfo(message=f"{OpcionRobot} seleccionado", title="Mision de rescate")
                        self.t.iconify()
                        robottmp=self.listaRobot.getRobot(OpcionRobot)
                    elif self.listaRobot.robotsR==1:
                        showinfo(message=f"{self.listaRobot.unicoResc().nombre} seleccionado", title="Mision de rescate")
                        self.t.iconify()
                        robottmp=self.listaRobot.unicoResc()
                    else:
                        showinfo(message="NO hay robots rescue disponibles", title="Mision de rescate")
                        self.t.iconify()   
                    CasillaInicial=ciudadtmp.Matriz.getNodo(int(OpcionEntradaX),int(OpcionEntradaY))
                    CasillaFinal=ciudadtmp.Matriz.getNodo(unidadcivilunica.Fila,unidadcivilunica.Columna)
                    self.Ejecutar_Rescate(ciudadtmp,CasillaInicial,CasillaFinal,robottmp)
                    print('|------------------------------|')
                else:
                    #self.t.iconify()
                    showinfo(message="Esta ciudad NO tiene unidades civiles", title="Mision de rescate")
                    self.t.iconify()
                                                
            elif Opcion=='3':
                system('cls')
                robotFtmp=None
                ciudadFtmp=None
                self.listaCiudad.mostrarCiudades()
                print('Selecciona una ciudad:')
                OpcionCiudad=input('> ')
                ciudadFtmp=self.listaCiudad.getCiudad(OpcionCiudad)
                print('')
                if ciudadFtmp.Matriz.recursos>1:
                    print('Punto de entrada: ')
                    print('-----------------')
                    ciudadFtmp.Matriz.verEntradas()
                    print('-----------------')
                    OpcionEntradaFX=input('Escriba coordenada en X: ')
                    OpcionEntradaFY=input('Escriba coordenada en Y: ')
                    print('|----------------------------|')
                    print('Escoja un recurso:')
                    print('..........................')
                    ciudadFtmp.Matriz.verRecursos()
                    print('..........................')
                    OpcionRX=input('Escriba coordenada en X: ')
                    OpcionRY=input('Escriba coordenada en Y: ')
                    print('')
                    showinfo(message=f"{OpcionCiudad} seleccionado. Recurso encontrado ({OpcionRX},{OpcionRY}).", title="Mision de extraccion")
                    self.t.iconify()
                    if self.listaRobot.robotsF>1:
                        print('Seleccione un robot:')
                        self.listaRobot.mostrarFig()
                        OpcionRobot=input('> ')
                        showinfo(message=f"{OpcionRobot} seleccionado", title="Mision de extraccion")
                        self.t.iconify()
                        robotFtmp=self.listaRobot.getRobot(OpcionRobot)
                    elif self.listaRobot.robotsF==1:
                        showinfo(message=f"{self.listaRobot.unicoF().nombre} seleccionado", title="Mision de extraccion")
                        self.t.iconify()
                        robotFtmp=self.listaRobot.unicoF()
                    else:
                        showinfo(message="NO hay robots fighters disponibles", title="Mision de extraccion")
                        self.t.iconify()
                    CasillaInicial=ciudadFtmp.Matriz.getNodo(int(OpcionEntradaFX),int(OpcionEntradaFY))
                    CasillaFinal=ciudadFtmp.Matriz.getNodo(int(OpcionRX),int(OpcionRY))
                    self.Ejecutar_Extraccion(ciudadFtmp,CasillaInicial,CasillaFinal,robotFtmp)
                    print('|------------------------------|')
                elif ciudadFtmp.Matriz.recursos==1:
                    print('Punto de entrada: ')
                    print('-----------------')
                    ciudadFtmp.Matriz.verEntradas()
                    print('-----------------')
                    OpcionEntradaFX=input('Escriba coordenada en X: ')
                    OpcionEntradaFY=input('Escriba coordenada en Y: ')
                    print('|----------------------------|')
                    unidadexunica=ciudadFtmp.Matriz.recurso()
                    showinfo(message=f"{OpcionCiudad} seleccionado. Recurso encontrada ({unidadexunica.Fila},{unidadexunica.Columna}).", title="Mision de extraccion")
                    if self.listaRobot.robotsF>1:
                        print('Seleccione un robot:')
                        self.listaRobot.mostrarFig()
                        OpcionRobot=input('> ')
                        showinfo(message=f"{OpcionRobot} seleccionado", title="Mision de extraccion")
                        self.t.iconify()
                        robotFtmp=self.listaRobot.getRobot(OpcionRobot)
                    elif self.listaRobot.robotsR==1:
                        showinfo(message=f"{self.listaRobot.unicoF().nombre} seleccionado", title="Mision de extraccion")
                        self.t.iconify()
                        robotFtmp=self.listaRobot.unicoF()
                    else:
                        showinfo(message="NO hay robots fighters disponibles", title="Mision de extraccion")
                        self.t.iconify()
                    CasillaInicial=ciudadFtmp.Matriz.getNodo(int(OpcionEntradaFX),int(OpcionEntradaFY))
                    CasillaFinal=ciudadFtmp.Matriz.getNodo(unidadexunica.Fila,unidadexunica.Columna)
                    self.Ejecutar_Extraccion(ciudadFtmp,CasillaInicial,CasillaFinal,robotFtmp)
                else:
                    #self.t.iconify()
                    showinfo(message="Esta ciudad NO tiene recursos", title="Mision de extraccion")
                    self.t.iconify()
                                                   
                  

    
    def CargarAchivo(self,Ruta):
        tree=ET.parse(Ruta)
        root=tree.getroot()
        #---------------------------------------Espacio para Ciudades ---------------------------------------------#
        for ciudad in root[0]:
            if self.listaCiudad.getCiudad(str(ciudad[0].text).strip()) is None:
                self.listaCiudad.insertarCiudad(str(ciudad[0].text).strip(),int(ciudad[0].attrib['filas']),int(ciudad[0].attrib['columnas']))
                ciudadtemp=self.listaCiudad.getCiudad(str(ciudad[0].text).strip())
                for i in range(ciudadtemp.filas):
                    for j in range(ciudadtemp.columnas):
                        ciudadtemp.Matriz.insertarCasilla(i,j,0)
                for nombre in ciudad:
                    if nombre.tag=='fila':
                        ciudadtemp.Matriz.recorrerFilas(int(nombre.attrib['numero']),str(nombre.text).strip())
                for militar in ciudad:
                    if militar.tag=='unidadMilitar':
                        nodotemp=ciudadtemp.Matriz.getNodo(int(militar.attrib['fila']),int(militar.attrib['columna']))
                        nodotemp.Estado=4
                        nodotemp.capacidad=int(militar.text)
                        ciudadtemp.Matriz.umilitar+=1
            else:
                ctmp=self.listaCiudad.getCiudad(str(ciudad[0].text).strip())
                ctmp.filas=int(ciudad[0].attrib['filas'])
                ctmp.columnas=int(ciudad[0].attrib['columnas'])
                ctmp.Matriz.actualizarMatriz()
                #ctmp=self.listaCiudad.getCiudad(str(ciudad[0].text).strip())
                for i in range(ctmp.filas):
                    for j in range(ctmp.columnas):
                        ctmp.Matriz.insertarCasilla(i,j,0)
                for nombre in ciudad:
                    if nombre.tag=='fila':
                        ctmp.Matriz.recorrerFilas(int(nombre.attrib['numero']),str(nombre.text).strip())
                for militar in ciudad:
                    if militar.tag=='unidadMilitar':
                        nodotemp1=ctmp.Matriz.getNodo(int(militar.attrib['fila']),int(militar.attrib['columna']))
                        nodotemp1.Estado=4
                        nodotemp1.capacidad=int(militar.text)
                        ctmp.Matriz.umilitar+=1
        #----------------------------------------Espacio para Robots------------------------------#
        for robot in root[1]:
            for nombres in robot:
                if self.listaRobot.getRobot(str(nombres.text).strip()) is None:
                    if str(nombres.attrib['tipo']).strip()=='ChapinFighter':
                        self.listaRobot.insetarRobot(str(nombres.text).strip(),'ChapinFighter')
                        self.listaRobot.getRobot(str(nombres.text).strip()).capacidad=int(nombres.attrib['capacidad'])
                        self.listaRobot.robotsF+=1
                    else:
                        self.listaRobot.insetarRobot(str(nombres.text).strip(),'ChapinRescue')
                        self.listaRobot.robotsR+=1
                else:
                    rtmp=self.listaRobot.getRobot(str(nombres.text).strip())
                    if rtmp.tipo=='ChapinFighter' and str(nombres.attrib['tipo']).strip()=='ChapinFighter':
                        rtmp.capacidad=int(nombres.attrib['capacidad'])
                    elif rtmp.tipo=='ChapinFighter' and str(nombres.attrib['tipo']).strip()=='ChapinRescue':
                        rtmp.capacidad=0
                        rtmp.tipo='ChapinRescue'
                    elif rtmp.tipo=='ChapinRescue' and str(nombres.attrib['tipo']).strip()=='ChapinFighter':
                        rtmp.tipo='ChapinFighter'
                        rtmp.capacidad=int(nombres.attrib['capacidad'])
                    elif rtmp.tipo=='ChapinRescue' and str(nombres.attrib['tipo']).strip()=='ChapinRescue':
                        pass


    def Ejecutar_Extraccion(self,ciudad,CasInicial,CasFinal,Robot):
        ciudad.Camino.actualizar()
        txtt='''
            digraph H {
            node [ shape=plaintext fontname=Helvetica fontsize=12]
            struct1 [label=<<table border='1' cellpadding="9" cellspacing="0" align="center">
            <tr cellborder='0'>
            <td align="center"><b>Tipo de mision: Rescate</b></td>
            <td   align="center"><b> Recurso: '''
        txtt+=f'''{CasFinal.Fila,CasFinal.Columna}</b></td>
            <td align="center"><b>Robot utilizado: </b>{Robot.nombre}</td>
            </tr>
            <tr>'''
        txtt+='''      
            <td ><table color='black' border='0' cellborder="0" width='145' cellpadding="4" cellspacing="0">  
            <tr>
            <td bgcolor="black" height='30' width='30'></td>
            <td align="Left">Intransitable</td>
            </tr>
            <tr>
            <td bgcolor="#27ae60" height='30' width='30'></td> 
            <td align="Left">Punto de entrada</td>
            </tr>
            <tr>
            <td bgcolor="#fdfefe" height='30' width='30'></td>
            <td align="Left">Camino</td>
            </tr>
            <tr>
            <td  bgcolor="#fa2626" height='30' width='30'></td>
            <td align="Left">Unidad Militar</td>
            </tr>
            <tr>
            <td bgcolor="#2e86c1" height='30' width='30'></td>
            <td align="Left">Unidad civil</td>
            </tr>
            <tr>
            <td bgcolor="#99a3a4" height='30' width='30'></td>
            <td align="Left">Recurso</td>
            </tr>'''
        txtt+='''
            </table>
            </td>
            <td colspan='3'><table color='white' border='1' cellborder="0" cellpadding="5" cellspacing="2">
            <tr>
            <td border='0'></td>'''        
        for cols in range(ciudad.columnas):
            txtt+=f'''<td border='0'>{cols}</td>'''
        txtt+='''
            </tr>'''
        for i in range(ciudad.filas):
            txtt+=f'''<tr><td border='0'>{i}</td>'''
            for j in range(ciudad.columnas):
                if ciudad.Matriz.getNodo(i,j).Estado==1: #Entrada
                    txtt+=f'''<td bgcolor='#27ae60'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==2:#Civil
                    txtt+=f'''<td bgcolor='#2e86c1'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==3:#Recurso
                    txtt+=f'''<td bgcolor='#99a3a4'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==4:#Militar
                    txtt+=f'''<td bgcolor='#fa2626'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==5:#Intr
                    txtt+=f'''<td bgcolor='black'></td>'''  
                elif ciudad.Matriz.getNodo(i,j).Estado==0:
                    txtt+=f'''<td bgcolor='white'></td>'''    
            txtt+='''</tr>'''
        txtt+='''   
        </table>
        </td>
        </tr>
        </table>>];
        }
        '''
        texto2=txtt
        miarchivo2=open('Mision_extraccion_Inicio.dot','w')
        miarchivo2.write(texto2)
        miarchivo2.close()
        system('dot -Tpng Mision_extraccion_Inicio.dot -o Mision_extraccion_Inicio.png')
        system('cd ./Mision_extraccion_Inicio.png')
        CiudadA=ciudad
        time.sleep(0.5)
        print('Ejecutando mision...')
        time.sleep(1)
        print('...')
        casillaActual=CasInicial
        casillaActual.Visitado=True
        casillaFinal=CasFinal
        #---------------------------------#
        it=0
        cont=0
        casillaActual.Nodo=Nodo(None,it)

        while casillaFinal.Visitado is False:
            cont+=1
            if casillaActual.arriba is not None:
                if casillaActual.arriba.Estado==0 or casillaActual.arriba.Estado==2 or casillaActual.arriba.Estado==1 or casillaActual.arriba.Estado==4 or casillaActual.arriba.Estado==3:
                    if casillaActual.arriba.capacidad<Robot.capacidad:
                        if casillaActual.arriba.Visitado is False:
                            if casillaActual.arriba.Nodo is None:
                                Robot.capacidad=Robot.capacidad-casillaActual.arriba.capacidad
                                casillaActual.arriba.Nodo=Nodo(casillaActual,it+1)
                                casillaActual.arriba.capacidad=0
            #Verifico abajo
            if casillaActual.abajo is not None:
                if casillaActual.abajo.Estado==0 or casillaActual.abajo.Estado==2 or casillaActual.abajo.Estado==1 or casillaActual.abajo.Estado==4 or casillaActual.abajo.Estado==3:
                    if casillaActual.abajo.capacidad<Robot.capacidad:
                        if casillaActual.abajo.Visitado is False:
                            if casillaActual.abajo.Nodo is None:
                                Robot.capacidad=Robot.capacidad-casillaActual.abajo.capacidad
                                casillaActual.abajo.Nodo=Nodo(casillaActual,it+1)
                                casillaActual.abajo.capacidad=0
            #verifico izquierda
            if casillaActual.izquierda is not None:
                if casillaActual.izquierda.Estado==0 or casillaActual.izquierda.Estado==2 or casillaActual.izquierda.Estado==1  or casillaActual.izquierda.Estado==4 or casillaActual.izquierda.Estado==3:
                    if casillaActual.izquierda.capacidad<Robot.capacidad:
                        if casillaActual.izquierda.Visitado is False:
                            if casillaActual.izquierda.Nodo is None:
                                Robot.capacidad=Robot.capacidad-casillaActual.izquierda.capacidad
                                casillaActual.izquierda.Nodo=Nodo(casillaActual,it+1)
                                casillaActual.izquierda.capacidad=0

            #verifico derecha
            if casillaActual.derecha is not None:
                if casillaActual.derecha.Estado==0 or casillaActual.derecha.Estado==2 or casillaActual.derecha.Estado==1 or casillaActual.derecha.Estado==4 or casillaActual.derecha.Estado==3:
                    if casillaActual.derecha.capacidad<Robot.capacidad:
                        if casillaActual.derecha.Visitado is False:
                            if casillaActual.derecha.Nodo is None:
                                Robot.capacidad=Robot.capacidad-casillaActual.derecha.capacidad
                                casillaActual.derecha.Nodo=Nodo(casillaActual,it+1)
                                casillaActual.derecha.capacidad=0


            '''if casillaActual.derecha is not None and casillaActual.arriba is not None and casillaActual.abajo is not None and casillaActual.izquierda is not None:
                if casillaActual.Visitado==True:
                    if casillaActual.derecha.Estado==3 or casillaActual.derecha.Estado==4 or casillaActual.derecha.Estado==5 or casillaActual.derecha.Visitado==True:
                        if casillaActual.izquierda.Estado==3 or casillaActual.izquierda.Estado==4 or casillaActual.izquierda.Estado==5 or casillaActual.izquierda.Visitado==True:
                            if casillaActual.arriba.Estado==3 or casillaActual.arriba.Estado==4 or casillaActual.arriba.Estado==5 or casillaActual.arriba.Visitado==True:
                                if casillaActual.abajo.Estado==3 or casillaActual.abajo.Estado==4 or casillaActual.abajo.Estado==5 or casillaActual.abajo.Visitado==True:
                                    showerror(message="Mision Imposible", title="Mision de rescate")
                                    break'''

            for i in range(CiudadA.filas):
                for j in range(CiudadA.columnas):
                    nodotemporal=CiudadA.Matriz.getNodo(i,j)
                    if casillaActual.Visitado is True:
                        if nodotemporal.Visitado is not True:          
                            if nodotemporal.Nodo is not None:
                                casillaActual=nodotemporal
                                break
                    else:
                        if nodotemporal.Visitado is not True:
                            if nodotemporal.Nodo is not None:
                                casillaActual=nodotemporal
                                break

            it=casillaActual.Nodo.iteracion
            casillaActual.Visitado=True
        nodorastro=casillaActual
        while nodorastro is not None:
            CiudadA.Camino.agregarInicio(nodorastro.Fila,nodorastro.Columna)
            nodorastro=nodorastro.Nodo.node           
        txt='''
            digraph H {
            node [ shape=plaintext fontname=Helvetica fontsize=12]
            struct1 [label=<<table border='1' cellpadding="9" cellspacing="0" align="center">
            <tr cellborder='0'>
            <td align="center"><b>Tipo de mision: Extraccion</b></td>
            <td   align="center"><b> Recurso :'''
        txt+=f'''{CasFinal.Fila,CasFinal.Columna}</b></td>
            <td align="center"><b>Robot utilizado: </b> <b>{Robot.nombre}</b> <b>Capacidad Final:{Robot.capacidad}</b></td>
            </tr>
            <tr>'''
        txt+='''      
            <td ><table color='black' border='0' cellborder="0" width='145' cellpadding="4" cellspacing="0">  
            <tr>
            <td bgcolor="black" height='30' width='30'></td>
            <td align="Left">Intransitable</td>
            </tr>
            <tr>
            <td bgcolor="#27ae60" height='30' width='30'></td> 
            <td align="Left">Punto de entrada</td>
            </tr>
            <tr>
            <td bgcolor="#fdfefe" height='30' width='30'></td>
            <td align="Left">Camino</td>
            </tr>
            <tr>
            <td  bgcolor="#fa2626" height='30' width='30'></td>
            <td align="Left">Unidad Militar</td>
            </tr>
            <tr>
            <td bgcolor="#2e86c1" height='30' width='30'></td>
            <td align="Left">Unidad civil</td>
            </tr>
            <tr>
            <td bgcolor="#99a3a4" height='30' width='30'></td>
            <td align="Left">Recurso</td>
            </tr>'''
        txt+='''
            </table>
            </td>
            
            <td colspan='3'><table color='white' border='1' cellborder="0" cellpadding="5" cellspacing="2">
            <tr>
            <td border='0'></td>'''        
        for cols in range(ciudad.columnas):
            txt+=f'''<td border='0'>{cols}</td>'''
        txt+='''
            </tr>'''
        #f0b27a 
        for i in range(ciudad.filas):
            txt+=f'''<tr><td border='0'>{i}</td>'''
            for j in range(ciudad.columnas):
                if ciudad.Matriz.getNodo(i,j).Estado==1: #Entrada
                    txt+=f'''<td bgcolor='#27ae60'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==2:#Civil
                    txt+=f'''<td bgcolor='#2e86c1'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==3:#Recurso
                    txt+=f'''<td bgcolor='#99a3a4'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==4:#Militar
                    txt+=f'''<td bgcolor='#fa2626'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==5:#Intr
                    txt+=f'''<td bgcolor='black'></td>'''  
                elif ciudad.Matriz.getNodo(i,j).Estado==0:
                    if ciudad.Camino.buscar(i,j) is not None:
                        if (ciudad.Matriz.getNodo(i,j).Fila==ciudad.Camino.buscar(i,j).x) and (ciudad.Matriz.getNodo(i,j).Columna==ciudad.Camino.buscar(i,j).y):
                            txt+=f'''<td bgcolor='#f0b27a'></td>'''
                    else:
                        txt+=f'''<td bgcolor='white'></td>'''    
            txt+='''</tr>'''
        txt+='''   
        </table>
        </td>
        </tr>
        </table>>];
        }
        '''
        texto=txt
        miarchivo=open('Mision_extraccion.dot','w')
        miarchivo.write(texto)
        miarchivo.close()
        system('dot -Tpng Mision_extraccion.dot -o Mision_extraccion.png')
        system('cd ./Mision_extraccion.png')
        startfile('Mision_extraccion.png')
    #----------------------------------------------------------------------------------------------------------#

    def Ejecutar_Rescate(self,ciudad,CasInicial,CasFinal,Robot):
        ciudad.Camino.actualizar()
        txtt='''
            digraph H {
            node [ shape=plaintext fontname=Helvetica fontsize=12]
            struct1 [label=<<table border='1' cellpadding="9" cellspacing="0" align="center">
            <tr cellborder='0'>
            <td align="center"><b>Tipo de mision: Rescate</b></td>
            <td   align="center"><b>Unidad Civil:'''
        txtt+=f'''{CasFinal.Fila,CasFinal.Columna}</b></td>
            <td align="center"><b>Robot utilizado: </b>{Robot.nombre}</td>
            </tr>
            <tr>'''
        txtt+='''      
            <td ><table color='black' border='0' cellborder="0" width='145' cellpadding="4" cellspacing="0">  
            <tr>
            <td bgcolor="black" height='30' width='30'></td>
            <td align="Left">Intransitable</td>
            </tr>
            <tr>
            <td bgcolor="#27ae60" height='30' width='30'></td> 
            <td align="Left">Punto de entrada</td>
            </tr>
            <tr>
            <td bgcolor="#fdfefe" height='30' width='30'></td>
            <td align="Left">Camino</td>
            </tr>
            <tr>
            <td  bgcolor="#fa2626" height='30' width='30'></td>
            <td align="Left">Unidad Militar</td>
            </tr>
            <tr>
            <td bgcolor="#2e86c1" height='30' width='30'></td>
            <td align="Left">Unidad civil</td>
            </tr>
            <tr>
            <td bgcolor="#99a3a4" height='30' width='30'></td>
            <td align="Left">Recurso</td>
            </tr>'''
        txtt+='''
            </table>
            </td>
            
            <td colspan='3'><table color='white' border='1' cellborder="0" cellpadding="5" cellspacing="2">
            <tr>
            <td border='0'></td>'''        
        for cols in range(ciudad.columnas):
            txtt+=f'''<td border='0'>{cols}</td>'''
        txtt+='''
            </tr>'''
        #f0b27a 
        for i in range(ciudad.filas):
            txtt+=f'''<tr><td border='0'>{i}</td>'''
            for j in range(ciudad.columnas):
                if ciudad.Matriz.getNodo(i,j).Estado==1: #Entrada
                    txtt+=f'''<td bgcolor='#27ae60'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==2:#Civil
                    txtt+=f'''<td bgcolor='#2e86c1'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==3:#Recurso
                    txtt+=f'''<td bgcolor='#99a3a4'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==4:#Militar
                    txtt+=f'''<td bgcolor='#fa2626'></td>'''
                elif ciudad.Matriz.getNodo(i,j).Estado==5:#Intr
                    txtt+=f'''<td bgcolor='black'></td>'''  
                elif ciudad.Matriz.getNodo(i,j).Estado==0:
                    txtt+=f'''<td bgcolor='white'></td>'''    
            txtt+='''</tr>'''
        txtt+='''   
        </table>
        </td>
        </tr>
        </table>>];
        }
        '''
        texto2=txtt
        miarchivo2=open('Mision_rescate_Inicio.dot','w')
        miarchivo2.write(texto2)
        miarchivo2.close()
        system('dot -Tpng Mision_rescate_Inicio.dot -o Mision_rescate_Inicio.png')
        system('cd ./Mision_rescate_Inicio.png')

        CiudadA=ciudad
        time.sleep(0.5)
        print('Ejecutando mision...')
        time.sleep(1)
        print('...')
        casillaActual=CasInicial
        casillaActual.Visitado=True
        casillaFinal=CasFinal
        #---------------------------------#
        it=0
        cont=0
        casillaActual.Nodo=Nodo(None,it)

        while casillaFinal.Visitado is False:
            cont+=1
            if casillaActual.arriba is not None:
                if casillaActual.arriba.Estado==0 or casillaActual.arriba.Estado==2 or casillaActual.arriba.Estado==1:
                    if casillaActual.arriba.Visitado is False:
                        if casillaActual.arriba.Nodo is None:
                            casillaActual.arriba.Nodo=Nodo(casillaActual,it+1)
            #Verifico abajo
            if casillaActual.abajo is not None:
                if casillaActual.abajo.Estado==0 or casillaActual.abajo.Estado==2 or casillaActual.abajo.Estado==1:
                    if casillaActual.abajo.Visitado is False:
                        if casillaActual.abajo.Nodo is None:
                            casillaActual.abajo.Nodo=Nodo(casillaActual,it+1)
            #verifico izquierda
            if casillaActual.izquierda is not None:
                if casillaActual.izquierda.Estado==0 or casillaActual.izquierda.Estado==2 or casillaActual.izquierda.Estado==1:
                    if casillaActual.izquierda.Visitado is False:
                        if casillaActual.izquierda.Nodo is None:
                            casillaActual.izquierda.Nodo=Nodo(casillaActual,it+1)
            #verifico derecha
            if casillaActual.derecha is not None:
                if casillaActual.derecha.Estado==0 or casillaActual.derecha.Estado==2 or casillaActual.derecha.Estado==1:
                    if casillaActual.derecha.Visitado is False:
                        if casillaActual.derecha.Nodo is None:
                            casillaActual.derecha.Nodo=Nodo(casillaActual,it+1)

            if casillaActual.derecha is not None and casillaActual.arriba is not None and casillaActual.abajo is not None and casillaActual.izquierda is not None:
                if casillaActual.Visitado==True:
                    if casillaActual.derecha.Estado==3 or casillaActual.derecha.Estado==4 or casillaActual.derecha.Estado==5 or casillaActual.derecha.Visitado==True:
                        if casillaActual.izquierda.Estado==3 or casillaActual.izquierda.Estado==4 or casillaActual.izquierda.Estado==5 or casillaActual.izquierda.Visitado==True:
                            if casillaActual.arriba.Estado==3 or casillaActual.arriba.Estado==4 or casillaActual.arriba.Estado==5 or casillaActual.arriba.Visitado==True:
                                if casillaActual.abajo.Estado==3 or casillaActual.abajo.Estado==4 or casillaActual.abajo.Estado==5 or casillaActual.abajo.Visitado==True:
                                    showerror(message="Mision Imposible", title="Mision de rescate")
                                    break


            for i in range(CiudadA.filas):
                for j in range(CiudadA.columnas):
                    nodotemporal=CiudadA.Matriz.getNodo(i,j)
                    if casillaActual.Visitado is True:
                        if nodotemporal.Visitado is not True:          
                            if nodotemporal.Nodo is not None:
                                casillaActual=nodotemporal
                                break
                    else:
                        if nodotemporal.Visitado is not True:
                            if nodotemporal.Nodo is not None:
                                casillaActual=nodotemporal
                                break

            it=casillaActual.Nodo.iteracion
            casillaActual.Visitado=True
        nodorastro=casillaActual
        while nodorastro is not None:
            CiudadA.Camino.agregarInicio(nodorastro.Fila,nodorastro.Columna)
            nodorastro=nodorastro.Nodo.node

        txt='''
            digraph H {
            node [ shape=plaintext fontname=Helvetica fontsize=12]
            struct1 [label=<<table border='1' cellpadding="9" cellspacing="0" align="center">
            <tr cellborder='0'>
            <td align="center"><b>Tipo de mision: Rescate</b></td>
            <td   align="center"><b>Unidad Civil:'''
        txt+=f'''{CasFinal.Fila,CasFinal.Columna}</b></td>
            <td align="center"><b>Robot utilizado: </b>{Robot.nombre}</td>
            </tr>
            <tr>'''
        txt+='''      
            <td ><table color='black' border='0' cellborder="0" width='145' cellpadding="4" cellspacing="0">  
            <tr>
            <td bgcolor="black" height='30' width='30'></td>
            <td align="Left">Intransitable</td>
            </tr>
            <tr>
            <td bgcolor="#27ae60" height='30' width='30'></td> 
            <td align="Left">Punto de entrada</td>
            </tr>
            <tr>
            <td bgcolor="#fdfefe" height='30' width='30'></td>
            <td align="Left">Camino</td>
            </tr>
            <tr>
            <td  bgcolor="#fa2626" height='30' width='30'></td>
            <td align="Left">Unidad Militar</td>
            </tr>
            <tr>
            <td bgcolor="#2e86c1" height='30' width='30'></td>
            <td align="Left">Unidad civil</td>
            </tr>
            <tr>
            <td bgcolor="#99a3a4" height='30' width='30'></td>
            <td align="Left">Recurso</td>
            </tr>'''
        txt+='''
            </table>
            </td>
            
            <td colspan='3'><table color='white' border='1' cellborder="0" cellpadding="5" cellspacing="2">
            <tr>
            <td border='0'></td>'''        
        for cols in range(CiudadA.columnas):
            txt+=f'''<td border='0'>{cols}</td>'''
        txt+='''
            </tr>'''
        #f0b27a 
        for i in range(CiudadA.filas):
            txt+=f'''<tr><td border='0'>{i}</td>'''
            for j in range(CiudadA.columnas):
                if CiudadA.Matriz.getNodo(i,j).Estado==1: #Entrada
                    txt+=f'''<td bgcolor='#27ae60'></td>'''
                elif CiudadA.Matriz.getNodo(i,j).Estado==2:#Civil
                    txt+=f'''<td bgcolor='#2e86c1'></td>'''
                elif CiudadA.Matriz.getNodo(i,j).Estado==3:#Recurso
                    txt+=f'''<td bgcolor='#99a3a4'></td>'''
                elif CiudadA.Matriz.getNodo(i,j).Estado==4:#Militar
                    txt+=f'''<td bgcolor='#fa2626'></td>'''
                elif CiudadA.Matriz.getNodo(i,j).Estado==5:#Intr
                    txt+=f'''<td bgcolor='black'></td>'''  
                elif CiudadA.Matriz.getNodo(i,j).Estado==0:
                    if CiudadA.Camino.buscar(i,j) is not None:
                        if (CiudadA.Matriz.getNodo(i,j).Fila==CiudadA.Camino.buscar(i,j).x) and (CiudadA.Matriz.getNodo(i,j).Columna==CiudadA.Camino.buscar(i,j).y):
                            txt+=f'''<td bgcolor='#f0b27a'></td>'''
                    else:
                        txt+=f'''<td bgcolor='white'></td>'''    
            txt+='''</tr>'''
        txt+='''   
        </table>
        </td>
        </tr>
        </table>>];
        }
        '''
        texto=txt
        miarchivo=open('Mision_rescate.dot','w')
        miarchivo.write(texto)
        miarchivo.close()
        system('dot -Tpng Mision_rescate.dot -o Mision_rescate.png')
        system('cd ./Mision_rescate.png')
        startfile('Mision_rescate.png')
            
principal=Main()
principal.Menu()
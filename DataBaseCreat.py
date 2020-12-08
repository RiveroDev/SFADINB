
#Verifica si la base de datos existe
# en dado cado que no creara una nueva base de datos en blanco si 
# seleccionamos que si 

import os.path as path
import sqlite3 as sq3


class CreadorBD():
    
    def __init__(self):
        self.nameDataBase = ""
        self.estado = False

    def renameDB(self):
        print("Desea crear una Nueva Base de datos: S/N")
        estado = input("ingrese respuesta: ")
        if estado.upper() == "S":
            nuevoNombre = (input("Escriba el Nombre de la BD: ")+".db")
            self.nameDataBase = nuevoNombre
        else:
            print("por defecto se asigna MovieMarket.db ")
            self.nameDataBase = "MovieMarket.db"  # nombre de la base de datos 

    def existeBaseDatos(self):
        if path.exists(self.nameDataBase) != True:
            return False
        else:
            self.estado = True
            return True

    def  crearBaseDatos(self):
        if self.estado == True:
            print("La Base de datos existe")
        else:
            print("La Base de datos no Existe desea crrear una: S/N")
            opcion = input("ingrese respuesta: ")
            if opcion.upper() == "S":
                db = sq3.connect(self.nameDataBase)
                db.close()
            else:
                print("Acuerdese no tiene base de dato activa")

    


   
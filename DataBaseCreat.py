
#Verifica si la base de datos existe
# en dado cado que no creara una nueva base de datos en blanco si 
# seleccionamos que si 

import os.path as path
import sqlite3 as sq3


class CreadorBD():

    def __init__(self):
        nameDataBase = "MovieMarket.db"  # nombre de la base de datos 

    def existeBaseDatos(self):
        if path.exists(nameDataBase) != True:
            return False
        else:
            return True

    def  crearBaseDatos(self,estado):
        existe = estado
        if existe == True:
            print("La Base de datos existe")
        else:
            print("La Base de datos no Existe desea crrear una: S/N")
            opcion = input()
            if opcion.upper() == "S":
                db = sq3.connect(nameDataBase)
                db.close()
            else:
                print("Acuerdese no tiene base de dato activa")


estado = existeBaseDatos()
crearBaseDatos(estado)
    


   
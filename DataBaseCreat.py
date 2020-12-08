
#Verifica si la base de datos existe 

import os.path as path
import sqlite3 as sq3

nameDataBase = "MovieMarket.db"  # nombre de la base de datos 

def existeBaseDatos():
    if path.exists(nameDataBase) != True:
        return False
    else:
        return True

def  crearBaseDatos():
    existe = existeBaseDatos()
    if existe != True:
        print("La Base de datos existe")
    else:
        print("La Base de datos no Existe desea crrear una: S/N")
        opcion = input()
        if opcion.upper() == "S":
            db = sq3.connect(nameDataBase)
            db.close()
        else:
            print("Acuerdese no tiene base de dato activa")
             


    


   
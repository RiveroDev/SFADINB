
#Verifica si la base de datos existe 

import os.path as path
import sqlite3 as sq3

nameDataBase = "MovieMarket.db"  # nombre de la base de datos 

def existeBaseDatos():
    if path.exists(nameDataBase) != True:
        db = sq3.connect(nameDataBase)
        db.close()
    else:
        print("La Base de Datos ya esxiste")

    


   
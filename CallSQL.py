
import sqlite3 as DB
from DataBaseCreat import *


class Conexines(CreadorBD):
    """crear un objeto que se conecta a la base de datos """

    #def __init__(self):
    #    self.Name_DB = ""

    def conexionSQL(self):

        """Recive un str con el nombre de la base de datos 
        o en su defecto la direccion completa con el nombre de la
        base de datos, y retorna la conexcion """

        self.conexion = DB.connect(self.nameDataBase)
        return self.conexion

    def peticionbd(self):

        """ Recive un objetos con la conexion a la Base de datos
         y regresa un puntero que crea la conexion 
        donde se podran dar las ordenes SQL"""

        self.puntero = self.conexion.cursor()
        return self.puntero

    def consultabd(self):

        self.puntero.execute("SELECT * FROM self.nameDataBase")
        

    def ingresarbd(self):
        pass

    def modificarbd(self):
        pass

    def borrarbd(self):
        pass






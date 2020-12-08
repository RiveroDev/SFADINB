
import sqlite3 as DB

class Conexines():
    """crear un objeto que se conexta a la base de datos """

    def __init__(self):
        self.Name_DB = 

    def conexionSQL(Name_DB):
        """recive un str con el nombre de la base de datos 
        o en su defecto la direccion completa con el nombre de la
        base de datos, y retorna la conexcion
        ejemplo :
            Name_DB = "basedeDatos.bd"    
            Name_DB = "C:\Users\Movie Market\Documents\Proyecto invetario Python\SFADINB\basedeDatos.bd """"
        conexion = DB.connect(Name_DB)
        return conexion

    def peticionbd(conexion_BD):
        """ Recive un objetos con la conexion a la 
        Base de datos y regresa un puntero que crea la conexion 
        donde se podran dar las ordenes SQL"""
        return puntero = conexion_BD.cursor()
        
    def consultabd():
        SELECT * FROM 

    def ingresarbd():
        pass

    def modificarbd():
        pass

    def borrarbd():
        pass






#
# este es un archivo para realizar pruebas en las diferentes clases y objetos 
#

# pureba de la clase DataBaseCreat  
#import DataBaseCreat as DTBS
#
#basedatos = DTBS.CreadorBD()
#basedatos.renameDB()
#print(basedatos.existeBaseDatos())
#basedatos.crearBaseDatos()

# la pruab fue existosa

datos = """CREATE TABLE "maam" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nombre" VARCHAR(60) NOT NULL,
	"Nombre2" VARCHAR(60) NOT NULL,
    "Fecha"   DATE ,
    "formato" VARCHAR(10),
    "posicion" VARCHAR(10),
	FOREIGN KEY("formato") REFERENCES "Formato"("idF"),
	FOREIGN KEY("posicion") REFERENCES "Posicion"("idP")
)"""

#----------------------------------------------------------------------------

from CallSQL import *

def ejecutar_Conexion():
    nuevConexion = Conexines()
    nuevConexion.conexionSQL()
    nuevConexion.peticionbd()
    nuevConexion.puntero.execute(datos)

ejecutar_Conexion()


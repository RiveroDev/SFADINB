#
# este es un archivo para realizar pruebas en las diferentes clases y objetos 
#

import DataBaseCreat as DTBS

basedatos = DTBS.CreadorBD()

basedatos.renameDB()
print(basedatos.existeBaseDatos())
basedatos.crearBaseDatos()

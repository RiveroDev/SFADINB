import sqlite3 as BD

la_conexion = BD.connect("Movie.db")

puntero = la_conexion.cursor()


# crear tabla Posicion
puntero.execute( 'CREATE TABLE "Posicion" ("idP" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,"Ubicacion" VARCHAR(10) NOT NULL)')
# crear tabla 

puntero.close()
la_conexion.close() 
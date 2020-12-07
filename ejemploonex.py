import sqlite3 as BD

la_conexion = BD.connect("Movie.db")

puntero = la_conexion.cursor()

puntero.execute( 'CREATE TABLE "Posicion" ("idP" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,"Ubicacion" VARCHAR(10) NOT NULL)')

puntero.close()
la_conexion.close() 
import sqlite3 as BD

la_conexion = BD.connect("Movie.db")

puntero = la_conexion.cursor()


# crear tabla Posicion
# puntero.execute( 'CREATE TABLE "Posicion" ("idP" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,"Ubicacion" VARCHAR(10) NOT NULL)')
# crear tabla 
# puntero.execute('CREATE TABLE "Formato" ("idF"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"tipo"	VARCHAR(10) NOT NULL)')
puntero.execute(
"""CREATE TABLE Pelicula (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nombre VARCHAR(60) NOT NULL,
	Nombre2 VARCHAR(60) NOT NULL,
    Fecha   DATE ,
    formato VARCHAR(10),
    posicion VARCHAR(10),
	FOREIGN KEY(formato) REFERENCES Formato(idF),
	FOREIGN KEY(posicion) REFERENCES Posicion(idP)
)""")
puntero.close()
la_conexion.close() 
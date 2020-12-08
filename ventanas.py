from os import system
import time

def inicio():
    system("cls")  # limpia completamente la pantalla de terminal 
    
    print("""
Listado de Peliculas Movie Market
        Bienvenidos
""")
    time.sleep(5)  # da una pausa de 5 seg

def menu():
    system("cls")
    print("""
 ----- Opciones ----------
  Selecione 1 opcion de Peliculas
  1. Buscar 
  2. Ingresar 
  3. Modificar 
  4. Eliminar 
  5. Salir 
  ------------------------
    """)

class PeliculaNueva():
    """clase se tienes los atributos para crear un objeto pelicula"""

    def __init__(self):
        self.nombreMovie = input('Nombre de la Pelicula: ')
        self.tipoformato = input("Ingrese el tipo de formato del disco, 1.DVD 2.BlueRay:  ")
        self.ubicacion_disco = input("Ubicacino del disco o Pelicula: ")

    def buscarBd():
        returnc

    def tipoFormato():
        return b

    def ubicacionBd():
        return a


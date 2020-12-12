
import tkinter as tk

from os import system
import time

ventana = tk.Tk()

ventana.title(" Movie Market.. Sistema de Registros y Adminstracion") # titulo del programa 
ventana.geometry('500x400') # dimencion de la ventana 
# estas son las etiquetas 
etiqueta_nombre = tk.Label(ventana, text="Nombre").pack()
etiqueta_nombre2 = tk.Label(ventana, text ="Nombre2").pack()
etiqueta_Ubicacion = tk.Label(ventana, text = "Ubicacion").pack()



ventana.mainloop()


class PeliculaNueva():
    """clase se tienes los atributos para crear un objeto pelicula"""

    def __init__(self):
        self.nombreMovie = input('Nombre de la Pelicula: ')
        self.tipoformato = input("Ingrese el tipo de formato del disco, 1.DVD 2.BlueRay:  ")
        self.ubicacion_disco = input("Ubicacino del disco o Pelicula: ")

    def buscarBd(self):
        pass

    def tipoFormato(self):
        return b

    def ubicacionBd(self):
        return a
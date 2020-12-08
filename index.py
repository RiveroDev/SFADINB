

# 
# Nota quedasmos en el minuto 36 del video de fazt

from tkinter import ttk      # llamamos a la liberia 'tkinter' ttK
from tkinter import *       ## llamamos a la liberia 'tkinter'  todos los modulos

import sqlite3              # importamos sqlite3 para hacer la base de datos

class Product:                  # creamos una clase productos donde se crear las ventanas
    """clase que crea la ventana mas sus objetos internos"""
    db_name = 'database.db'

    def __init__(self,window):   # este es el metodo contructor y recive un argumento  ventana con las propiedades de tk
        self.wind = window
        self.wind.title('Productos Aplicacion') 
        # creamos un  frame 
        frame = LabelFrame(self.wind, text = 'Register a New Product')
        frame.grid( row = 0, column = 0, columnspan = 3, pady = 20 )

        #Name input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Price input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Button add Producto
        ttk.Button(frame, text = 'save Product').grid(row = 3, columnspan = 2 , sticky = W + E )

        # table
        self.tree = ttk.Treeview(height = 10, column = 2)
        self.tree.grid(row = 4, column = 0 , columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)

        #self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        query = 'SELECT * FROM product ORDEN BY name DESC'
        db_rows  = self.run_query(query)
        print(db_rows)

if __name__ == '__main__':    # 
    window = Tk()
    application = Product(window)
    window.mainloop()



from cgitb import text
from math import prod
from tkinter import ttk
from tkinter import *
from database import *

class Product:

    db = Database()

    def __init__(self, window):
        self.window = window
        self.window.title("Products Application")

        #Craeting a frame container
        frame = LabelFrame(self.window, text="Register a new product")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #Name input
        Label(frame, text="Name: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        #Price input
        Label(frame, text="Price: ").grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        #Add button to save product
        ttk.Button(frame, text="Save Product", command= self.addProduct).grid(row=3, columnspan=2, sticky=W + E)

        #Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)
        self.getAllProducts()

    def validate(self):
        return len(self.name.get()) > 0 and len(self.price.get()) > 0
    
    def addProduct(self):
        if self.validate():
            self.db.addProduct(self.name.get(), self.price.get())
            self.getAllProducts()
            self.db.connections()
        else:
            print("Name and price are required")
        return

    def getAllProducts(self):
        prodsInTable = self.tree.get_children()
        for product in prodsInTable:
            self.tree.delete(product)

        products = self.db.getAllProducts()
        
        for product in products:
            self.tree.insert('', 0, text=product[1], values=product[2])
        
        return


if __name__ == '__main__':
    window = Tk()
    app = Product(window)
    window.mainloop()
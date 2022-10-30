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

        #Output messages
        self.messages = Label(text="", fg="red")
        self.messages.grid(row=3, column=0, columnspan=2, sticky=W + E)

        #Table
        self.tree = ttk.Treeview(height=10, columns=[1,2])
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='id', anchor=CENTER)
        self.tree.heading('#1', text='Name', anchor=CENTER)
        self.tree.heading('#2', text='Price', anchor=CENTER)
        self.getAllProducts()

        #Buttons
        ttk.Button(text='DELETE', command=self.deleteProduct).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='UPDATE', command=self.updateProduct).grid(row=5, column=1, sticky=W + E)

    def message(self, text, coolor):
        self.messages['fg'] = coolor
        self.messages['text'] = text
        return

    def cleanEntry(self):
        self.name.delete(0, END)
        self.price.delete(0, END)
        return

    def validate(self):
        return len(self.name.get()) > 0 and len(self.price.get()) > 0
    
    def addProduct(self):
        if self.validate():
            self.db.addProduct(self.name.get(), self.price.get())
            self.getAllProducts()
            self.message('Product {} added successfully.'.format(self.name.get()), 'green')
            self.cleanEntry()
        else:
            self.message('Name and price are required', 'red')
        return
    
    def deleteProduct(self):
        selectedProduct = self.tree.item(self.tree.selection())
        selectedProductId = selectedProduct['text']
        if (selectedProductId):
            self.db.deleteProduct(selectedProductId)
            self.getAllProducts()
            self.message('Product with id: {} deleted'.format(selectedProductId), 'green')
        else:
            self.message('Select the product you want to delete', 'red')
        return
    
    def updateProduct(self):
        selectedProduct = self.tree.item(self.tree.selection())
        selectedProductId = selectedProduct['text']
        if (selectedProductId):
            oldName = selectedProduct['values'][0]
            oldPrice = selectedProduct['values'][1]
            newName = self.name.get() if self.name.get() else oldName
            newPrice = self.price.get() if self.price.get() else oldPrice
            self.db.updateProduct(selectedProductId, newName, newPrice)
            self.getAllProducts()
            self.message('Product with id: {} updated'.format(selectedProductId), 'green')
        else:
            self.message('Select the product you want to update', 'red')
        return

    def getAllProducts(self):
        prodsInTable = self.tree.get_children()
        for product in prodsInTable:
            self.tree.delete(product)

        products = self.db.getAllProducts()
        
        for product in products:
            self.tree.insert('', 0, text=product[0],values=(product[1],product[2]))
        
        return
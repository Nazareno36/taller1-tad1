from itertools import product
from typing import Tuple


class Supermarket:

    def __init__(self):
        ##Declaracion de las listas con los productos.
        self.dairy_products = []
        self.grooming_products = []
        self.grain_products = []

    def add(self, item, stock, category):
        ##Añadiendo tuplas con el producto y las existencias a la lista indicada.
        if category == 'dairy': self.validate(item,stock,self.dairy_products)
        if category == 'grooming': self.validate(item,stock,self.groomig_products)
        if category == 'grain': self.validate(item,stock,self.grain_products)

    def input_add(self):
        ##Recibiendo datos por consola
        print('\t Bienvenido al gestor de inventario \t')
        category = ''

        while category != 'dairy' and category != 'grooming' and category != 'grain':
            category = input('Ingrese la categoria del producto\ndairy -> productos lacteos\ngrooming -> productos de aseo\ngrain -> productos de grano\n')
        
        item = input('Ingrese el nombre del producto -> ')
        stock = 0
        while True:
            try:
                stock = int(input('Ingrese la cantidad del producto -> '))
                break
            except:
                print('El valor ingresado no es valido')
        
        self.add(item,stock,category)

    def validate(self, item, stock, list):
        ##Valida si el producto se encuentra ya en el inventario
        # añade el stock o lo adiciona al inventario si no estaba 
        found = False
        i = 0
        while i < len(list) and not found:
            if list[i][0] == item:
                new_stock = list[i][1] + stock 
                list[i] = (item,new_stock)
                found = True
            i+=1        
        if not found: list.append((item,stock))    
    
    ##Mostrando el inventario.
    def show_inventary(self):
        print('\tInventario\t')
        print(f"Productos lacteos: {self.dairy_products}")
        print(f"Productos de aseo: {self.grooming_products}")
        print(f"Productos de grano: {self.grain_products}")

from itertools import product


class Supermarket:

    def __init__(self):
        ##Declaracion de las listas con los productos.
        self.dairy_products = []
        self.groomig_products = []
        self.grain_products = []

    def add(self, item, stock, category):
        ##Añadiendo tuplas con el producto y las existencias a la lista indicada.
        if category == 'dairy': self.dairy_products.append((item,stock))
        if category == 'grooming': self.grooming_products.append((item,stock))
        if category == 'grain': self.grain_products.append((item,stock))


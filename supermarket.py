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


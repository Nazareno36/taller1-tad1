'''
    Taller1-tad
    Author: Carlos Andrés Páez
    Date: 07/09/2022
    Version: 1.0
'''

from supermarket import Supermarket

supermarket = Supermarket()

##Punto B.
supermarket.add('Yogourt', 10, 'dairy')

##Punto C.
supermarket.input_add()
print(supermarket.dairy_products)

##Punto D.
supermarket.add('Yogourt',20,'dairy')


##Punto E.
supermarket.show_inventary()
print(supermarket.dairy_products)

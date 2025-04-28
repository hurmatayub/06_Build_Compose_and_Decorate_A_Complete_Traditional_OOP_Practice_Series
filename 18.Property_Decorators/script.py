class Product:
    def __init__(self, price):
        self._price = price
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value
            
    @price.deleter
    def price(self):
        print("Price has been deleted")
        del self._price

product = Product(100)

print(product.price)

product.price = 150
print(product.price)

product.price = -50

del product.price

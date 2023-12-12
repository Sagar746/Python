# Single Level Inheritance

# class Parent:
#     def __init__(self):
#         self.num = 100

# class Child(Parent):
#     def __init__(self):
#         super().__init__()

#         self.val =200
        
    
#     def show(self):
#         print(self.num)
#         print(self.val)

# c = Child()
# c.show()




# Multi Level Inheritance

# class Product:
#     def review(self):
#         print('Product customer view')

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class SmartPhone(Phone):
#     pass


# s = SmartPhone(20000, 'Apple',12)
# s.buy()
# s.review()


# HIERARCHICAL INHERITANCE


# class Phone:
#     def __init__(self, price, brand, camera):
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class SmartPhone(Phone):
#     pass

# class FeaturPhone(Phone):
#     pass

# s = SmartPhone(20000, 'Apple',12)
# s.buy()



# Multiple Inheritance

class Product:
    def review(self):
        print('Product customer view')

    def buy(self):
        print('Product buy method')

class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a Phone')

class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, 'Apple',12)
s.buy()



# Polymorphism ==> Method over riding  
                   # Method Overloading, Operator Overloading

# class User:
#     def login(self):
#         print('Login')
    
#     def register(self):
#         print('Register')

# class Student(User):

#     def enroll(self):
#         print("Enroll")

#     def review(self):
#         print('Review')

# std = Student()
# std.enroll()
# std.login()


# -------------------- SUPER -----------------------------*

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside the constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         super().__init__(price, brand, camera)  # common attribute use of Parent atrribute
#         self.os = os
#         self.ram = ram
#         print('Inside smartphone Constructor')


# s = SmartPhone(20000, 'Samsung',12,'Android',2)

# print(s.os)
# print(s.brand)

# -----------------------------------------------------------------------------
# Single Inheritance
class Parent:
    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()

        self.val =200
        
    
    def show(self):
        print(self.num)
        print(self.val)


c = Child()
c.show()
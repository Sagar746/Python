# class Geek:
#     def __init__(self, age=0):
#         self._age = age


#     # getter method
    
#     def get_age(self):
#         print('getting method called')
#         return self._age
    
#     # setter method

#     def set_age(self,x):
#         print('setting method called')
#         self._age = x

#     def del_age(self):
#         del self._age

#     age = property(get_age, set_age, del_age)
    
# marks = Geek()
# marks.age = 25
# print(marks.age)
# print(marks.get_age())


# ---------------------------------------------------------------
'''
The main purpose of any decorator is to change your class methods or attributes in such a way 
so that the user of your class no need to make any change in their code.
'''


# class Geeks:
#     def __init__(self, age=0):
#         self._age = age

#     @property
#     def age(self):
#         print('getter method called')
#         return self._age
    

#     @age.setter
#     def age(self, a):
#         print('setter method called')
#         self._age = a


# marks = Geeks()
# marks.age = 24
# print(marks.age)




class Geometry:
    def area(self, l,b=0):
        if b==0:
            print('Circle: ', 3.14*l*l)
        else:
            print('Rect: ', l*b)


obj = Geometry()
obj.area(4)
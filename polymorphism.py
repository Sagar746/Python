# Polymorphism
# 1. Method Overriding
# 2. Method Overloading -> input given and different behaviour


class Geometry:

    def area(self,l,b=0):
        if b==0:
            print('Circle: ', 3.14 *l*l)
        else:
            print('Rect: ', l*b)
    
obj = Geometry()
obj.area(4) 



# 3. Operator Overloading
# --> using + to add does mathematical addition but use + for different purpose called operator overloading




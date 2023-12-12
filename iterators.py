# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a+=1
#         return x
    
# myclass = MyNumber()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))


# --------------------------------------------------

# To prevent the iteration from going on forever, we can use the StopIteration statement.

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <20:
#             x = self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
        
# myclass = MyNumber()
# myiter = iter(myclass)sss

# for i in myiter:
#     print(i)


# --------------------------------------------------

# --------------------------------------------------


# --------------------------------------------------
# --------------------------------------------------

# --------------------------------------------------
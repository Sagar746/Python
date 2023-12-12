# Generality to Specificity --> General and Specific
# Constructor is a method , whose control is not given to users
# instance variabel = > value of variable is different for differnet object


# class Atm:
#     counter = 1 # static or class variable

#     def __init__(self) -> None:
#         print(id(self))
#         self.__pin = ''
#         self.__balance = 0

#         self.sno = Atm.counter
#         Atm.__counter = Atm.__counter + 1

#         self.menu()
    
#     @staticmethod
#     def get_counter():
#         return Atm.__counter

#     @staticmethod
#     def set_counter(new):
#         return Atm.counter == new

#     def get_pin(self):
#         return self.__pin

#     def set_pin(self, new_pin):
#         self.__pin = new_pin
#         print('Pin changed')

#     def menu(self):
#         user_input = input('''
#         Hello, how would you like to proceed?
#         1. Enter 1 to create __pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to Check __Balance
#         5. Enter 5 to exit
#         '''
#     )
#         if user_input =='1':
#             self.create___pin()
#         elif user_input == '2':
#             self.deposit()
#         elif user_input == '3':
#             self.withdraw()
#         elif user_input == '4':
#             self.__check_balance()
#         else:
#             print('Bye')
    
#     def create___pin(self):
#         self.__pin = input("Enter you __pin: ")
#         print('__Pin set successfully')

#     def deposit(self):
#         temp = input('Enter you __pin: ')
#         if temp == self.__pin:
#             amount = int(input('Enter amount you want to deposit: '))
#             self.__balance = self.__balance + amount
#             print('Deposit Successfull')
#         else:
#             print('Invalid __Pin')

#     def withdraw(self):
#         temp = input('Enter you __pin: ')
#         if temp == self.__pin:
#             amount = int(input('Enter amount you want to withdraw: '))
#             if amount < self.__balance:
#                 self.__balance = self.__balance - amount
#                 print('amount withdrawn ' + amount)
#             else:
#                 print('Insufficient funds')
#         else:
#             print('Invalid __pin')

#     def __check_balance(self):
#         temp = input('Enter you __pin: ')
#         if temp == self.__pin:
#             print(self.__balance)
#         else:
#             print('Invalid __pin')

# nic = Atm()
# # gbl._Atm__create_pin()
# # nic.__check_balance()
# # nic.get_pin()
# # nic.set_pin('1111')
# # print(id(nic))
# print(nic.sno)
# # nic.__balance = 'skdjflsjdf' # it doesn't affect our main balance to affect use _Atm__balance = 'kljdsfl'





# ----------------------------------------------------



# class Fraction:
#     def __init__(self,n,d):
#         self.n = n
#         self.d = d

#     def add(self, other):
#         temp_num = self.n * other.d + other.n * self.d
#         temp_den = self.d *other.d
#         return f'{temp_num, temp_den}'
    
# frac = Fraction(3,4)
# print(frac())

# ========================================


# pass by reference

# class Customer:
#     def __init__(self, name):
#         self.name = name


# def greet(customer):
#     print(id(customer))

# cust = Customer('Sagar')
# print(id(cust))

# greet(cust)



class Customer:
    def __init__(self,name):
        if not name:
            raise ValueError('Missing Name')
        self.name = name

c = Customer()
print(c)
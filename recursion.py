

# def mul(a,b):
#     if b==1:
#         return a
#     return a + mul(a,b-1)

# --------------------------------------------------------------------------

# print(mul(3,4))

# def fact(number):
#     if number ==1:
#         return 1
#     else:
#         return number * fact(number-1)
    
# print(fact(5))

# --------------------------------------------------------------------------

# def plain(text):
#     if len(text)==1:
#         print('palindrome')
#     else:
#         if text[0] == text[-1]:
#             plain(text[1:-1])
#         else:
#             print('Not a Palindrome')

# plain('madam')

# --------------------------------------------------------------------------


# def fib(m):
#     if m==0 or m==1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)
# print(fib(12))

# --------------------------------------------------------------------------



# MEMOIZATION
# Memoization ensures that a method runs for the same input only once

# def memo(m,d):
#     if m in d:
#         return d[m]
#     else:
#         d[m]=memo(m-1,d)+memo(m-2,d)
#         return d[m]
# d = {0:1,1:1}
# print(memo(48,d))

# --------------------------------------------------------------------------
"""
Concept of decorators is used in memoization , so first understand how decorators works
"""

# memory = {}
# def memoize_factorial(f):
#     def inner(num):
#         if num not in memory:
#             memory[num]=f(num)
#             print('result in saved memory')
#         else:
#             print('returning result from saved memory')
#         return memory[num]
#     return inner


# @memoize_factorial
# def factorial(num):
#     if num ==1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(5))
# print(factorial(5))


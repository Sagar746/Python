def hello():
    print('hello my name is sagar tiwari')


# def mul(a,b):
#     if b==1:
#         return a
#     return a + mul(a,b-1)

# print(mul(3,4))

# def fact(number):
#     if number ==1:
#         return 1
#     else:
#         return number * fact(number-1)
    
# print(fact(5))


# def plain(text):
#     if len(text)==1:
#         print('palindrome')
#     else:
#         if text[0] == text[-1]:
#             plain(text[1:-1])
#         else:
#             print('Not a Palindrome')

# plain('madam')


# def fib(m):
#     if m==0 or m==1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)
# print(fib(12))



# MEMOIZATION

def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d)+memo(m-2,d)
        return d[m]
d = {0:1,1:1}
print(memo(48,d))

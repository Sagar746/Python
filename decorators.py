# def shout(text):
#     return text.upper()


# def whisper(text):
#     return text.lower()


# def greet(func):
#     greeting = func('I am a hacker')
#     print(greeting)

# greet(shout)
# greet(whisper)

# ------------------------------------------------------

# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder

# adds = create_adder(15)
# print(adds(10))

# ------------------------------------------------------


# def hello_decorator(func):

#     def inner1():
#         print('Hello, this is before execution function')

#         func()

#         print('This is after execution')
#     return inner1


# def function_to_be_used():
#     print('This is inside the function')


# function_to_be_used = hello_decorator(function_to_be_used)

# function_to_be_used()


# ------------------------------------------------------


# def outer_func(func):

#     def inner_func():
#         print('before')
#         func()
#         print('after')
#     return inner_func

# def ordinary():
#     print('I am ordinary')


# decorated_func = outer_func(ordinary)
# decorated_func()



# ------------------------------------------------------



# def outer_func(func):
#     def inner_func():
#         print('before')
#         func()
#         print('after')
#     return inner_func

# @outer_func
# def ordinary():
#     print('I am ordinary')

# ordinary()


# ------------------------------------------------------


# def outer_func(func):
#     def inner_func(*args, **kwargs):
#         print('before execution')
#         func(*args, **kwargs)
#         print('after execution')
#     return inner_func

# @outer_func
# def printer(msg):
#     print(msg)

# printer('Hello')


# ------------------------------------------------------


def factorial(x):
    if x == 1:
        return 1
    return (x * factorial(x-1))

a = factorial(6)
print(a)







# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
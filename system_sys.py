# sys module in python is used to manipulate different parts of Python runtime Environment

import sys

print(sys.version)
print(sys.platform)
#------------------------------

"""It can be used to get the input from command line directly

"""
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     print(f'Input: {line}')
# print('Exit')


# ------------------------------


# sys.stdout.write('Sagar\n')

# --------------------------------

# a_list =[]

# for line in sys.stdin:
#     if not 'q' in line.rstrip():
#         a_list.append(line)
#     else:
#         break
#     print(a_list)


# ------------------------------------

# sys.stderr represent the standard error stream

# def print_to_stderr(*a):
#     print(*a, file=sys.stderr)

# print_to_stderr()

# ----------------------------------------------------------
# sys.arg
# print(sys.argv[0])
# 1. sys.argv[0] is the name of the current Python Script

# print(len(sys.argv)) # provide the number of command line arguments

# ----------------------------------------------------------------

# n = len(sys.argv)
# print('Total argument passed:', n)
# print('\nName of Python Script: ', sys.argv[0])
# print('\nArguments passed:', end=' ')

# for i in range(1,n):
#     print(sys.argv[i], end=' ')

# Sum = 0
# for i in range(1,n):
#     Sum+= int(sys.argv[i])

# print('\n\nResult: ', Sum)


# ------------------------------------------------------------------



# sys.exit() => It exists the program with a message 

# age = 17
# if age < 18:
#     sys.exit('Age less than 18')
# else:
#     print('Age is not less than 18')



# --------------------------------------------------------------------

# sys.path 

# print(sys.path)

# ---------------------------------------------------------------------

# print(sys.modules)
# ---------------------------------------------------------------------


# sys.getrefcount --> reference count for any given object,
# number of time it is referenced by the other objects

# a = 'Sagar Tiwari'
# print(sys.getrefcount(a))




# def f():
#     print('f')

# def p():
#     print('p')

# a = sys.argv[1:]

# b = a[0]
# if b =='f':
#     f()
# elif b =='p':
#     p()
# else:
#     print('fuck....')
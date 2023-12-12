a = 4

print(id(a))

# ALIASING

a = 5
b = a

print('id of a :', id(a))
print('id of b :', id(b))


# REFERENCE COUNTING

import sys

a = 'corona'
b=a
c=b

print(id(a), id(b), id(c))

print('No of variable point...')   # -5 to 256
print(sys.getrefcount(a))


# Mutability

# Mutability refers to the ability to change or edit in its memory location

# if you append, extend, insert its id remain same but change on concatenation



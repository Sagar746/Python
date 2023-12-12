# a = 'sagar'
# print(a[-1])
# print(a[:-1])
# print(a[::-1])


# COMMON FUNCTIONS

# len 
c = 'sagar'
print(len(c))

# max
print(max(c))

# min
print(min(c))

# sorted
print(sorted(c, reverse=True))

print(c.capitalize())

a = 'my name is sagar tiwari'
print(a.title())

print(a.upper())
print(a.lower())
c = 'sagar'


x = 'sAgAr'
print(x.swapcase())

print(x.count('A'))

print(x.find('s'))

print(x.index('sA'))  # if substring not found then, gives ValueError

print(x.endswith('gAr'))
print(x.startswith('sA'))

print('my name is {fname} {lname}'.format(fname='sagar',lname='tiwari'))

print('------------------------------------------')



s = 'flat20'
print(s.isalnum())
print(s.isalpha())
print(x.isdigit())

y = '123'
print(y.isdigit())

h = 'hello_world'
print(h.isidentifier())  # _ is a identifier

d = 'my name is sagar tiwari'
print(d.split())
print(d.split("n"))

print(''.join(d))
print('-'.join(d))

print(d.replace('sagar','Sagar'))

name = '     sagar              '
print(name.strip())

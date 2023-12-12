# Arrays homogenous , List heterogenous
# Array may continous memory location stores
# Arrays are much faster


l = [1,2,3,4,5]
l.append(6)
print(l)

print()

l.extend([6,7,8])
print(l)

print()

l.insert(1,'sagar')
print(l)

print()

l.remove(1)
print(l)

print()

l.pop()
print(l)

print()

name = 'sagar@gmail.com'
print(name[:name.find('@')])

print()

L1= [1,1,2,3,4]
L=[]

for i in L1:
    if i not in L:
        L.append(i)
print(L)

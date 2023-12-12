i=1
while i< 11:
    print(i)
    i+=1


print('------------------------------')
print()


for i in range(10, 0,-1):
    print(i)

print('------------------------------')
print()


for i in reversed('kathmandu'):
    print(i)


# def make_loop():
#     num = 0
#     while True:
#         yield num
#         num+=1

# for i in make_loop():
#     print(i,end=' ')
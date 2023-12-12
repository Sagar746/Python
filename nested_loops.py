# rows = int(input('Enter the number of rows: '))


# for i in range(1, rows+1):
#     for j in range(0,i):
#         print('*', end='')
#     print()



for i in range(10):
    for j in range(i):
        print('*', end='')
    print()

print()

for i in range(11):
    if i==5:
        break
    print(i)

print()

for i in range(11):
    if i == 5:
        continue
    print(i)

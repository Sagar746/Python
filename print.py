# print('sagar','tiwari', sep='-', end='\n')

# x,y,z = input('enter a value: ').split()

# print(x,y,z)

# x = list(map(str,input('enter a name: ').split()))
# print('list of the students: ', x)


import argparse

# print(argparse.__file__)

# parser = argparse.ArgumentParser()
# parser.add_argument('square', help='show the square of the number', type=int)
# parser.add_argument('-v', '--verbosity', help = 'output the verbosity', action='store_true')
#  args = parser.parse_args()

# ans = args.square**2

# else:
# if args.verbosity:
#     print(f'The square of {args.square} is {ans}')
#     print(f'The square of {args.square} is equal to {ans}')



# ----------------------------------

import sys

a_list =[]

for line in sys.stdin:
    if not 'q' in line.rstrip():
        a_list.append(line)
    else:
        break
    print(a_list)
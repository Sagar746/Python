import sys
import argparse, string, random

# name = sys.argv[1]
# num = int(sys.argv[2])

# for _ in range(num):
#     print(f'I am sorry, {name}, I am afraid I cant do that')


# ---------------------------------------------------------------------

# TEXT = string.ascii_letters + string.digits + string.punctuation

# parser = argparse.ArgumentParser(
#     prog = 'Matrix',
#     usage = 'whoa, use: %(prog)s [option] number',
#     description = 'Prints random columns of character',
#     epilog = 'If it were green it would be like the matrix'
# )

# parser.add_argument('num', type=int)
# args = parser.parse_args()

# for _ in range(50):
#     content = [random.choice(TEXT) for _ in range(100)]
#     print(' '.join(content))



# -------------------------------------------------------------------


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('number1', help='first number')
#     parser.add_argument('number2', help='second number')
#     parser.add_argument('-o','--operation', help='operation', choices=['add','sub','mul'])

#     args = parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)


#     n1 = int(args.number1)
#     n2 = int(args.number2)
#     result = None

#     if args.operation == 'add':
#         result = n1+n2
#     elif args.operation =='sub':
#         result = n1-n2
#     elif args.operation == 'mul':
#         result = n1 * n2
    
#     print(result)


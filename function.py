# def is_even(number):
#     '''
#     This function tells if the given numbers is odd or even.
#     Input - any valid integer
#     output - odd/even
#     Created By - Sagar Tiwari
#     Last Edited - 20 Aug 2023
#     '''
#     if number%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
    

# for i in range(1,11):
#     print(is_even(i))


# print(is_even.__doc__)


def f(num):
    print(num**2)

x = f
del f
x(3)


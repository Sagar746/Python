'''Return sends a specified value to its caller whereas,
Yield can produce a sequence of values.

We should use yield when we want to iterate over a sequence, 
but don’t want to store the entire sequence in memory.
'''

# def simple():
#     yield 1
#     yield 2
#     yield 3


# for value in simple():
#     print(value)


# ----------------------------------------


# def nextSquare():
#     i = 1

#     while True:
#         yield i*i
#         i+=1    # Next execution resumes


# for num in nextSquare():
#     if num >100:
#         break
#     print(num)


# ------------------------------------------

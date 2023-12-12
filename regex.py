import re 


'''
RegEx can be used to check if a string contains the specified search pattern.
'''
# ^ = starts with
# . = any character(except new line)
# * = zero or more occurence
# $ = ends with


# txt = 'The rain in the Spain'
# x = re.search('^The.*Spain$', txt)
# print(x)




# \s => Returns a match where the string contains a white space character

# txt = 'The rain in the Spain'
# x = re.search('\s', txt)
# print(x.end())



# txt = 'The rain in the Spain'
# x = re.findall('ai',txt)
# print(x)


'''Split at each white-space character'''

# txt = 'The rain in the Spain'
# x = re.split('\s',txt)
# print(x)



'''Split the string only at the first occurrence'''

# txt = 'The rain in the Spain'
# x = re.split('\s',txt,1)
# print(x)
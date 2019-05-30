
# strings are immutable
'''
my_string = 'This is a sentence'
for i in range(len(my_string)- 1, -1, -1):
     print(my_string[i], end='')

my_string[0] = 'X'
'''
my_string = 'This is a sentence'
reversed_string = ''
for i in range(len(my_string)- 1, -1, -1):
     reversed_string += my_string[i]

print(reversed_string)



# one line to reverse a string

#print(''.join(reversed(my_string)))






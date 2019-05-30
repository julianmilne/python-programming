'''
#function the returns a result
def box(value):
    result = value * value
    return result

answer = box
print(answer)

#print(box(50))

#funtion with multiple arguments
def greetings(name, job, hobby):
    print(f'hello {name} your job {job} and you like {hobby}')

    greetings('juian', 'none', 'CJJ')
'''
'''

def reverese_list(my_list):
    #interate over list in reverese order
    for index in range(len(my_list)- 1, -1, -1):
        #add each element to a new list
        new_list.append(my_list[index])

    #return my reverese_list
    return newo_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = reverese_list(numbers)


print(result)

'''
def reverse_string(my_string):
    reversed_string = ''
    for i in range(len(my_string)- 1, -1, -1):
        reversed_string += my_string[i]
    return reverse_string

def is_palindrome(word):
    word_reversed = reverse_string(word)
    if word_reversed == word:
        return True
    return False

print(is_palindrome('level'))
    



    #return True if it is, False otherwise
'''

def is_pal(word):
    first, last = 0, len(word) - 1
    while first < last:
        if word[first] != word[last]:
            return 

'''
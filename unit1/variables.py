def main():
    first_name = 'Julian'
    last_name = 'Milne'
    full_name = first_name + ' ' + last_name

    print(full_name)

    #boolean variable
    has_child = True

    #null/none varible
    cars = None

def conditionals():
    #given a range of grades 0 - 100
    #if grade is between 80 and 100 - print 'A'
    # if grade is between 60 and 79 - print 'B'
    #if grade is 50 - 59 - print 'C'
    #0 - 40 - print 'F'
    grade = 79
    if grade >= 80:
        print('A')
    if grade >= 60:
        print('B')
    if grade >= 50:
        print('C')
    else:
        print('F') 

def fizzbuzz():
    '''
    for the numbers 1 to 50
    print 'fizz' if the number is a multiple of 3
    print 'buzz' if the number is a multiple of 5
    print 'fizzbuzz' if the number is a multiple of 15
    otherwise print the number
    '''
    for num in range(1, 51):
        if num % 15 == 0:
            print('fizzbuzz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0:
            print('fizz')
        else:
            print(num)



if __name__ == '__main__':
    fizzbuzz()
#ask user to guess your secret number

#loop as long as user input is not equal to secret number

#print message if it is equal, then end loop

#if guess is with-in 2 of the answer print almost there

#if guess is greater or less then 2 print too far

secret = 7

guess = int(input("guess my street numner: "))

while guess != secret:
    print('Not correct')
    guess = int(input("guess my secret number: "))

print("yaaah!! You got it.")


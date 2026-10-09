operator = input('(odd_num_check,perfect_square_check,vowel_check,divisibility_check,palindrominator,simple_interest)')
if operator == 'odd_num_check' :
    a = int(input('type your no her: '))
    if ((a % 2) == 1) :
        print('yes')
    else : 
        print('no')

elif operator == 'perfect_square_check' :
    b = int(input("type your no Here"))
    x = 0 
    while x * x <= b:
        if x * x == b:
            print('yes')
            break
        x += 1
    else: 
        print('no')

elif operator == 'vowel_check' :
    c = str(input("Type your word here: "))
    if any(char in "aeiouAEIOU" for char in c):
         print('yes')
    else :
         print('no')

elif operator == 'divisiblity_check' :
    d = int(input('type your no her')) 
    if ((d % 2) == 0  ) :

        if ((d % 3) == 0):
            print('divisible by 2 and 3')
        else :
            print('divisible by 2 ')

    elif ((d % 3) == 0):
        print('divisible by 3')

    else : 
        print('not divisible by 2 and 3') 

elif operator == 'palindrominator':
    e = str(input('Type a word: '))
    word = e[::-1]
    reversed_word = word[1:]
    print(e[0:]+reversed_word)
# simple intrest formulae is pxrxt
# Simple interest calculator with inputs with a higher interest rate if long term.
# Name: simple_interest
# Inputs: principal_amount:int, n_years:int (number of years)
# Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
# If the operation name is not any of the above print "Invalid Operation".
elif operator == 'simple_interest':
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10 : 
        print(int(principal_amount * 0.05 * n_years))
    else:
        print(int(principal_amount * 0.08 * n_years))
else: 
    print('invalid input')     








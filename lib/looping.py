#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i >=1:
        print(i)
        i-=1
    print('Happy New Year!')
    pass

def square_integers(int_list):
    # code goes here!
    return [list*list for list in int_list]
    pass

def fizzbuzz():
    # code goes here!
    num = 1
    while num <=100:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print( num)
        num +=1
    pass
happy_new_year()
print(square_integers([1,2,3,4,5]))
print(fizzbuzz())
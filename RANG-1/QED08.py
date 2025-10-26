# pomodoro | 
""" 

Simple multiplication
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

"""


def simple_multiplication(number) :
    if number % 2 == 0:
        number *= 8
        return number 
    else:
        number *= 9
        return number 

print(simple_multiplication(3))
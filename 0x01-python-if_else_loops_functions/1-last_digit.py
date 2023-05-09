#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = f'-{str(number)[-1]}'
    
if last_digit > 5:
    print(f'Last_digit of {number:d} is {last:d} and is greater than 5')
elif last_digit == 0:
    print(f'Last_digit of {number:d} is {last:d} and is 0')
else:
    print(f'Last_digit of {number:d} is {last:d} and is less than 6 and not 0')

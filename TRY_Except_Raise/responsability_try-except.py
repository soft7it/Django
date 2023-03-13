

import time

current_year = int(time.strftime('%Y', time.localtime()))
print(f'Now year is {current_year}')
in_value = input('Enter you birth year: ')

try:
    birth_year = int(in_value)
    age = current_year - birth_year
    print(f'You are {age} years old')
except:
    print('Error, wrong year value!!!')

# SRP - single responsability principle        
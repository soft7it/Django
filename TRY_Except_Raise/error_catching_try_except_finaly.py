data = [ 10,20,30 ]

try:
    index = int(input('Enter the index : '))
    value = data[index]
    print(f'the selected value is {value}')
except ValueError:
    print('You must supply an integer') 
except IndexError:
    print('The index must be within range')
finally:
    print('Than you for using this program!!!')       
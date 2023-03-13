# Does not take resposability!
def powerOfTwo(number):
    if type(number) != int:
        raise TypeError('The argument must be an integer')
    elif number < 0:
        raise ValueError('The argument must be positive')
    else:
        # return number * number # HW1: python operator -> exponent
        return number ** 2  # HW1: python operator -> exponent


#########################################################
while True:
    try:
        a = int(input('Enter square side= '))
        # a = 5
        try:
            area = powerOfTwo(a)
            print(f'the sq ({a}) -> area {area}')
        except ValueError:
            print('You must enter only positive values!')

    except ValueError:
        print('You must enter only integer values!!!')          

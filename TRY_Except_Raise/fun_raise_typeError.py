def powerOfTwo( number ):
    if type(number) != int:
        raise TypeError('The argument must be an integer')
    else:
        # return number * number # HW1: python operator -> exponent
        return number **2 # HW1: python operator -> exponent

#########################################################
a = int(input('Enter square side= '))
# a = 5
area = powerOfTwo(a)

print(f'the sq ({a}) -> area {area}')

#  <<<<<<<<<<<<<<<<
# [app] -> func()>^
#               v
#               v
#               v
#           print -> message -> console

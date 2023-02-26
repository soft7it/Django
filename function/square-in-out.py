# square(value)  ----> value ^ 2

# 1. classic solution (args-IN, return-OUT)

def square(value):
    result = value * value  
# HW1: find other methods of obtaining square number (ninim 2 variant). 
    return result


# 2. alternative solution (args-IN, OUT)
# def square(value):
#     value[0] = value[0] * value[0]

# 2. alternative solution (args-IN, OUT)
def square(value):
    res = value[0] * value[0]
    value.pop(0)
    value.insert(0, res)

###########################
n = [10]
square(n)
print(n)

## HW2: 
#   create a function (generalMark) which receives 3 numbers from a dictionary

#   IN{
#      'sem_1' : 9.0
#      'sem_2' : 8.0
#      'exam' : 9.0
#    }

#   OUT{
#      'sem_1' : 9.0
#      'sem_2' : 8.0
#      'exam' : 9.0
#      'gen' : 8.66
#    }
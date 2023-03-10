# dynamic
class Box:

    # default behaivor
    def __init__(self, value):
        # HW1: 
        #   modify init code, so it puts None when no argument passed
        self.value = value

        # HW2: add default <, >, ==< comparasion methods __lt__, __gt__, __eq__ ---> overloading

    # intended behavior
    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False
        
##################################
b1 = Box(25)
b2 = Box(1000)   

#---------------------------------
if b1.isEmpthy():
    print('the Box1 is emty')
if b2.isEmpthy():
    print('the Box2 is emty')

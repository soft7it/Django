# suulier
def inputInt():
    n = int( input("enter an ineger") )
    return n

# function 
def processInt(n):
    nsq = n * n
    return nsq

# consumer
def outputInt(n, nsq):
    print(f'{n}^2 = {nsq}')
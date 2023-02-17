from os import system

system('cls')

def avg (par1, par2, par3):
    s = par1 + par2 + par3
    m = s / 3
    return m

def printFormatted(par1, par2, par3, res):
    print(f'the average of {par1} {par2} {par3} is {res}')
    # return

############   Main Program ##################################

a = 10
b = 20
c = 30

    #### function frame #####
    # > call
res = avg(a,b,c)
    # < return
    ####  / function frame #####

printFormatted(a, b, c, res)

############# /Main Program ########################################

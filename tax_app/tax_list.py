from os import system

#### calculate tax_income  #############

def calculateTax(amount, interes, scopul_sumei):

    total_dict = [  ]   # create a list
     
    total_dict.append( amount )
    total_dict.append( interes )
    total_dict.append( amount * 0.12 )# 12%
    total_dict.append( scopul_sumei )
    
    return total_dict
    
    # return [amount, interes, amount * (interes / 100), scopul_sumei] # folosim ca lista

#######  clear #########################

def clear():
    system("cls")   

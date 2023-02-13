from os import system

#### calculate tax_income  #############

def calculateTax(amount):

    total_dict = [  ]   # create a list
     
    total_dict.append( amount )
    total_dict.append( amount * 0.12 )# 12%
    # total_dict["sum"] = amount

    # print(total_dict)
    return total_dict

    

#######  clear #########################

def clear():
    system("cls")  
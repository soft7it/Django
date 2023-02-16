from os import system

#### calculate tax_income  #############

def calculateTax(amount, interes, scopul_sumei):

    # # total_dict = {    } # create a dictionar
     
    # # total_dict["suma"] = amount
    # # total_dict["interes"] = interes
    # # total_dict["interes_amount"] = amount * (interes / 100) # 12%    
    # # total_dict["scopul_sum"] = scopul_sumei

    total_dict = {"suma": amount,
                  "interes": interes, 
                  "interes_amount" : amount * (interes / 100),
                  "scopul_sum": scopul_sumei}  # create a dictionar

    # print(total_dict)
    return total_dict

   # return (amount, interes, amount * (interes / 100), scopul_sumei) # folosim ca tuple

   # return [amount, interes, amount * (interes / 100), scopul_sumei] # folosim ca lista    

#######  clear #########################

def clear():
    system("cls")    

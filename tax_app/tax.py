from os import system

#### calculate tax_income  #############

def calculateTax(amount):
    #amount      # suma de bani
    interes = 0.02     # 2% dobinda procente
    comission_interes = amount * interes
    # target_borrow  # salariu , imprumut
    tax_income = 0.2 # 20%
    tax_salary = amount * tax_income
    return comission_interes, 'for rate credit. ', tax_salary, 'for income tax.'

#######  clear #########################

def clear():
    system("cls")  

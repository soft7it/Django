from os import system
import re  # import for re.match()
#### calculate tax_income  #############

def singUp(username, email, password):   #

    sing_up_dict = {    }  # dictionar rec    
    contr = '^[0-9a-zA-Z]+$'
    if 5 <= len(username) <= 12 and  re.match(contr, username): # sing_up_dict["key_password"] == password:
        sing_up_dict['key_user'] = username
        print("Good way user valid")
    
        control = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"    
        if re.match(control, email):  # controlam validarea elai daca corespunde
            sing_up_dict["key_email"] = email
            print("The entered email is valid")
            
        else:
            print("The entered email is invalid")

        if len(password) > 7:
            sing_up_dict["key_password"] = password
            return sing_up_dict
        else:
            print('Must be more 8 charaters')    

    else:
        print("Somthing went wrong")

#######  clear #########################

def clear():
    system("cls")

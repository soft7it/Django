from os import system

#### calculate tax_income  #############

def singUp(username, email, password): #

    sing_up_dict = { 
        'key_user':'avion',
        'key_email':'pl',
        'key_password':'ch',
       } # dictionar

    if 5 <= len(username) <= 12 and sing_up_dict["key_user"] == username and sing_up_dict["key_email"] == email and sing_up_dict["key_password"] == password: 
        print("Good")
    else:
        print("wrong")     
    
    
    # return 

    

#######  clear #########################

def clear():
    system("cls")  
from os import system

#### calculate tax_income  #############

def singUp(username, email, password): #

    sing_up_dict = { 
        'key_user':'avatar',
        'key_email':'play@company.com',# 
        'key_password':'cistoForsFord', # 
       } # dictionar
    
    if 5 <= len(username) <= 12 and sing_up_dict["key_user"] == username and sing_up_dict["key_email"] == email and sing_up_dict["key_password"] == password:# and len(password) > 7: 
        print("Good way")
        
        return sing_up_dict 
               
    else:
        print("Somthing went wrong")
        print(sing_up_dict["key_password"])

#######  clear #########################

def clear():
    system("cls")  

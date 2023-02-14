"""
The idea behind this homework is for you to imagine how does the SIGNUP function work in a social network
Create a function called signUp()
+ It should take 3 parameters: username, email, password
It should verify that the all 3 are strings
It should verify that the username has at least 5 and at most 12 characters and consists only of latin (a..zA..Z) letters and digits (0..9)
It should verify the validity of the email address (@, .)
It should require a password of at least 8 characters long
It should return a dictionary that contains these three values
It should raise exceptions when something does not validate
"""
from logic import *

while True:

    clear()

    username = input('Username : ')
    email = input('Email : ')
    password = input('password : ')

    singUp(username, email, password) # 

    query = input("Would you like check again (y/n) ?  ")

    if query != 'y':
        break

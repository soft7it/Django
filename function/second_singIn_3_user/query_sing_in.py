from os import system
from sing_in import *
system('cls')

while True:    

    nume = input('you user: ')

    pas = input('you password: ')

    signIn(nume, pas)

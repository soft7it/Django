"""
This example will use a class statically

1. Let's imagine that there is a class that represents the "core" of the social app

2. create module called core.py
3. create a class called App, inside it
add the attributes: name (name of the application), version (release version of the application), author (author of the app name and email), year (the year the app was first published), rating (in the 5 star scale)
4. create a separate function called appInfo() in the same module which will print the information from the class using formatted string
5. test your module by importing it and using it in the main module called main.py
"""


class App:

    name = 'Danii'
    version = '7.25'
    author = 'Joe Bezoss'
    year = '2023'
    rating = '5****'


def appInfo():
    abc = App()
    print("Hello, name application is ", abc.name, '\n Version application : ', abc.version,
          '\n Author : ', abc.author, '\n Published', abc.year, '\n Rating : ', abc.rating)

appInfo()

# clasa : proprietati, metode
# name =  - prprietati
# metode - funtiile( maninca, fuge, doarme )
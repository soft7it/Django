from posts_title_funct import *
from os import system


system('cls')

while True:

    title = input('Add a title description theme: ')

    body = input(' Insert many description about title theme: ')

    addPost(posts, title, body)

    print(posts)

    query = input('Would you like to add (y/n) ? ')

    if query != 'y':
        break

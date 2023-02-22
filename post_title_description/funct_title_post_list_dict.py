'''
Let's say you need a function that "adds posts" to a list of post in a users timeline

Imagine the next list (which is a global variable)

posts = [
  {
  "title": "About the importance of functional programming",
  "body": "Functional programming is ....." 
  },
  {
  "title": "OOP programming brings classes and objects into the code",
  "body": "OOP is  ....." 
  },
]
what is required:

create a function called "addPost()", which will take exactly 3 parameters: the list in which the post is to be added, the post title and the post body
the function will form a new dictionary formed of the last 2 parameters and add it into the first place inside the first parameter
the function will NOT return anything

'''
from os import system

system('cls')

# global 
posts = [
    {
        "title": "About the importance of functional programming",
        "body": "Functional programming is ....."
    },
    {
        "title": "OOP programming brings classes and objects into the code",
        "body": "OOP is  ....."
    },
]

def addPost(posts_list, post_title, post_body):
    # create a new dictionary for the post
    new_post = {'title': post_title, 'body': post_body}
    # insert the new post into the beginning of the posts list
    posts_list.insert(0, new_post)

# call addPost() function
addPost(posts, "A new post about Python", "Python is a powerful programming language.")
# verificam output
print(posts)

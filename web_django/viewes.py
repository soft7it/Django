
from django.http import HttpResponse
from django.template import loader

from random import *#randint
# import secrets


# aka database

users = [
    {"username": "johny", "created": "2000-01-01"},
    {"username": "Mary", "created": "2000-01-02"},
    {"username": "jonatan", "created": "2000-01-03"},
    {"username": "ala", "created": "2000-01-04"},
    {"username": "misha", "created": "2000-01-05"},
    {"username": "jorge", "created": "2000-01-06"},
    {"username": "wiska", "created": "2000-01-07"},
]

def homePage(request):
    template = loader.get_template("home.html")
    
    # HW: sort users by date descendendig list.sort()
    
    return HttpResponse( template.render({
        
    }, request) )


####  random info ########
# def homePage(request):
#     template = loader.get_template("home.html")
#     quotes = [
#         'Coding like poetry should be short and concise. ― Santosh Kalwar',
#         'It’s not a bug; it’s an undocumented feature. ― Anonymous',
#         'First, solve the problem. Then, write the code. – John Johnson'
#     ]
#     quote = quotes[randint(0,len(quotes)-1)]
#     # quote = quotes[randint(0, 2)]
#     # quote = quotes[randrange(3)]
#     # quote = quotes[secrets.randbelow(2)]
    
#     return HttpResponse( template.render({'q': quote}, request) )

def profilePage(request):
    return HttpResponse("User`s page")

def postsPage(request):
    return HttpResponse("Post`s page")

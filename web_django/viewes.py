
from django.http import HttpResponse
from django.template import loader

from random import *#randint
import secrets

def homePage(request):
    template = loader.get_template("home.html")
    quotes = [
        'Coding like poetry should be short and concise. ― Santosh Kalwar',
        'It’s not a bug; it’s an undocumented feature. ― Anonymous',
        'First, solve the problem. Then, write the code. – John Johnson'
    ]
    # quote = quotes[randint(0,len(quotes)-1)]
    # quote = quotes[randint(0, 2)]
    # quote = quotes[randrange(3)]
    quote = quotes[secrets.randbelow(2)]
    
    return HttpResponse( template.render({'q': quote}, request) )

def profilePage(request):
    return HttpResponse("User`s page")

def postsPage(request):
    return HttpResponse("Post`s page")

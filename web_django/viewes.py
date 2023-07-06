
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from random import *#randint
# import secrets

from .models import Post

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
 

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

posts = [
    { 'title': 'First title', 'created': '2001-01-01'},
    { 'title': 'Second title', 'created': '2001-01-02'},
    { 'title': 'Third title', 'created': '2001-01-03'},
    { 'title': 'Fourth title', 'created': '2001-01-04'},
    { 'title': 'Fifth title', 'created': '2001-01-05'},
]

def homePage(request):
    template = loader.get_template("home.html")
    
    # HW: sort users by date descendendig list.sort()
    #     sort posts by date 
    # ########################################     
    # def get_newest(element):
    #     return element['created']
    # users.sort(key=get_newest, reverse=True)
    ##########################################
    users.sort(key=lambda element: element['created'], reverse=True)
    
    return HttpResponse( template.render({
        
        "last_users": users[:5], # imi da numai cu bucata 5 bucati
        "last_posts": posts[:3],  # imi da numai cu bucata 5 bucati
        "user": request.user
    }, request) )

def signupPage(request):
    template = loader.get_template("signup.html")
          
    
    return HttpResponse( template.render({
        
    }, request) )

def signinPage(request):
    template = loader.get_template("signin.html")
         
    
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

# Post views:#######################################
def addPost(request):
    template = loader.get_template("add-post.html")        
    
    return HttpResponse( template.render({        
    }, request) )
#####################################################
def getPosts(request):
    template = loader.get_template("get-posts.html")  

    posts = Post.objects.all()

    print(type(Post.objects))  # Manager
    print(type(posts))  # QuerySet

    return HttpResponse( template.render({ 
        'posts' : posts       
    }, request) )

#######################################################
def updatePost(request):
    template = loader.get_template("update-post.html")        
    
    id = request.GET['id']

    # 1. find the post by id
    post = Post.objects.get(pk=id)
    print(type(post))
    return HttpResponse( template.render({ 
        'post' : post       
    }, request) )

######################################################
def changePost(request):       
    
    id = request.GET['id']
    new_title = request.GET['title']
    new_body = request.GET['body']

    # 1. find the post by id
    post = Post.objects.get(pk=id)
    # print(type(post))
    post.title = new_title
    post.body = new_body

    post.save()

    return redirect( '/get-posts' )

    # return HttpResponse( 'Post update succesfully' )                 
#######################################################

def savePost(request): # httpRequest 

    # print(request.GET['title'])  # QueryDict
    # print(type(request.GET['title']))  # double check

    title = request.GET['title']
    body = request.GET['body']

    post = Post(randint(100000,200000),title,body)
    post.save()

    return redirect( '/get-posts' )

########################################################
def deletePost(request): 
    
    id = request.GET['id']

    # 1. find the post by id
    post = Post.objects.get(pk=id)

    # 2. delete
    post.delete()

    return HttpResponse( 'Post deleted successfully' )  #   http://127.0.0.1:8000/delete-post?id=


# User views:#######################################
def registerUser(request):
    if request.method == 'GET':
        template = loader.get_template("user/register.html")        
        
        return HttpResponse( template.render({ }, request)) 
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['username']

        # User.objects.create_user(username, email, password)
        
        # # if password and confirm_password and password != confirm_password:

        # #     return redirect( '/register' )              

        # # return HttpResponse('Account created succesfully.')
        # return redirect('/')
        if password == confirm_password:
            User.objects.create_user(username, email, password)
            return redirect('/')
        else:
            return redirect( 'register' ) 
            # return HttpResponse('Passwords do not match.')

    # User login views:#######################################
def loginUser(request):
    if request.method == 'GET':
        template = loader.get_template("user/login.html")         
        return HttpResponse( template.render({ }, request))
     
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        print(type(user))
        if user is None:
            return redirect('/user/login')
        
        login(request, user)
        return redirect('/')
    
    # User login views:#######################################
def logoutUser(request):
    logout(request)
    return redirect("/")   

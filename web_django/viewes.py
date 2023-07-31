
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.shortcuts import redirect

from random import *#randint
# import secrets

from .models import Post

# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout, get_user

from django.contrib import messages
from django.contrib.sessions.models import Session

import re

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
    show_notifications = request.session.get('show_notifications', None)
    
    return HttpResponse( template.render({
        
        "last_users": users[:5], # imi da numai cu bucata 5 bucati
        "last_posts": posts[:3],  # imi da numai cu bucata 5 bucati
        "user": request.user,
        "show_notifications": show_notifications,
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

# def profilePage(request):
#     return HttpResponse("User`s page")

# def postsPage(request):
#     return HttpResponse("Post`s page")

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
# def registerUser(request):
#     if request.method == 'GET':
#         template = loader.get_template("user/register.html")        
#         return HttpResponse( template.render({ }, request)) 
    
#     elif request.method == 'POST':
#         username = request.POST['username']
        
#         email = request.POST['email']   # regex
#         pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#         if re.match(pattern, email):        
        
#             password = request.POST['password']
#             confirm_password = request.POST['password']

#             if password == confirm_password:
#                 User.objects.create_user(username, email, password)
#                 messages.success(request, 'Create account succesful.')
#                 ##  redirect to main mage after create account
                
#                 user = authenticate(username=username, password=password)
#                 login(request, user)# end
#                 return redirect('/')
#         else:
#             messages.error(request, 'Wrong credential.')
#             return redirect('/user/register')
#     else:
#         messages.error(request, 'Wrong credential.')
#         return redirect('/user/register')        
#     # *********************************

def registerUser(request):
    if request.method == 'GET':
        template = loader.get_template("user/register.html")
        return HttpResponse(template.render({}, request))
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            messages.error(request, 'Please fill in all the fields.')
            return redirect('/user/register')

        # Validate email format
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            messages.error(request, 'Invalid email format.')
            return redirect('/user/register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('/user/register')
        try:
            # Create user
            user = CustomUser.objects.create_user(username, email, password)
            messages.success(request, 'Account created successfully.')            
            # Authenticate and log in the user
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        
        except Exception as e:
            messages.error(request, f'An error occurred  {str(e)} .')
            return redirect('/user/register')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('/user/register')

    # User login views:#######################################
# def loginUser(request):
#     # req ----> FORM
#     if request.method == 'GET':
#         template = loader.get_template("user/login.html")
#         # message = request.session.get('error_message', None)         
#         # return HttpResponse( template.render({ 'message': message }, request))
#         return HttpResponse( template.render({}, request))
     
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         print(user)
#         print(type(user))
#         # req -------> AUTH
#         if user is None:
#             # request.session['error_message'] = 'Wrong credential.'
#             messages.error(request, 'Wrong credential.')
#             return redirect('/user/login')
        
#         login(request, user)
#         # request.session.pop('error_message')
#         messages.success(request, 'Login succesful.')
#         return redirect('/')
def loginUser(request):
    if request.method == 'GET':
        template = loader.get_template("user/login.html")
        return HttpResponse(template.render({}, request))
     
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            messages.error(request, 'Please provide both username and password.')
            return redirect('/user/login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Wrong credentials. Please try again.')
            return redirect('/user/login')
        
        login(request, user)

        visitingUser = CustomUser.objects.get(pk=user.id)

        # 1. load the backup data
        session_data_backup = visitingUser.session_data_backup
        session_data = json.loads(session_data_backup if session_data_backup else '{}')

        # 2. put the data in current session
        request.session.update(session_data)

        messages.success(request, 'Login successful.')
        return redirect('/')

    else:
        messages.error(request, 'Invalid request method.')
        return redirect('/user/login')
    
def toggleUserNotification(request):
    visitingUser = get_user(request)
    
    toggle = request.GET.get('toggle', None)
    # Post.get()
    if not toggle:
        request.session['show_notifications'] = False
    else:    
        request.session['show_notifications'] = True

    return redirect(f'/user/profile/{visitingUser.id}')

import json   
#     User login views:#######################################
def logoutUser(request):
    # show_notifications = request.session.get('show_notifications', None)
    visitingUser = get_user(request)
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)

    # 1. get all the current session data
    sesion = Session.objects.get(pk=request.session.session_key)
    session_data = sesion.get_decoded()

    # 2. serialize data in json
    session_data_json = json.dumps(session_data)

    # 3. save to backup column in visiting user
    visitingUser.session_data_backup = session_data_json
    visitingUser.save()
    
    logout(request)
    return redirect("/")  
    
# #     User login views:#######################################
# def logoutUser(request):
#     show_notifications = request.session.get('show_notifications', None)
#     logout(request)  # 
#     request.session.flush() # foteaza stergerea datelor
#     request.session['show_notifications'] = show_notifications
#     messages.success(request, 'Logout successful.')
#     return redirect("/")  
#  
# def logoutUser(request):
#     show_notifications = request.session.get('show_notifications', None)
#     request.session.flush()
#     request.session['show_notifications'] = show_notifications
#     logout(request)
#     return redirect("/")

# def logoutUser(request):
#     messages.success(request, 'Logout successful.')
#     logout(request)
#     return redirect("/") 


def userProfile(request, id):
    profileUser = CustomUser.objects.get(pk=id)
    show_notifications = request.session.get('show_notifications', None)
    print(profileUser)
    visitingUser = get_user(request) # User
    # visitingUser = CustomUser.objects.get(pk=profileUser.id)
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)
    print(visitingUser)
    if request.method == 'GET':
        # print("Profile of user:", id)
        template = loader.get_template("user/profile.html")
        userFriends = profileUser.friends.all()
        profileUserIsNotVisitingUserFriend = visitingUser.friends.all().contains(profileUser)
        # print(profileUserIsNotVisitingUserFriend)
        # print(type(userFriends))
        return HttpResponse(template.render({
            'profileUser' : profileUser,                
            'visitingUser' : visitingUser,
            'userFriends' : userFriends,
            'profileUserIsNotVisitingUserFriend' : profileUserIsNotVisitingUserFriend,
            'show_notifications' : show_notifications,
            }, request))

def addUserFriend(request, id):
    profileUser = CustomUser.objects.get(pk=id)
    visitingUser = get_user(request) # User
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)
    
    visitingUser.friends.add(profileUser)
    visitingUser.save()
    
    return redirect(f'/user/profile/{profileUser.id}')

def removeUserFriend(request, id):
    profileUser = CustomUser.objects.get(pk=id)
    visitingUser = get_user(request) # User
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)
    
    visitingUser.friends.remove(profileUser)
    visitingUser.save()
        
    return redirect(f'/user/profile/{profileUser.id}')


def editUserProfile(request, id):
    
    if request.method == 'GET':
        profileUser = CustomUser.objects.get(pk=id)
        print(profileUser)
        # print(profileUser.friends.all())
        visitingUser = get_user(request)
        print(visitingUser)
        if profileUser.id == visitingUser.id:
            template = loader.get_template("user/edit-profile.html")
            return HttpResponse(template.render({
                'profileUser' : profileUser,
                }, request))
        else:
            return HttpResponseForbidden('Acces Denied, idi guleai...:)')
        
    elif request.method == 'POST':
        profileUser = CustomUser.objects.get(pk=id)
            
        visitingUser = get_user(request)
        if profileUser.id == visitingUser.id:
                   
            avatar = request.FILES['avatar']
            avatar_file = open (f'app/public/uploads/{avatar}', 'wb+')
            for chunk in avatar.chunks():
                avatar_file.write(chunk)

            avatar_file.close()
            profileUser.avatar = f'uploads/{avatar}'
            profileUser.save()
            return redirect(f'/user/profile/{profileUser.id}')
        else:
            return HttpResponseForbidden('Acces Denied, idi guleai...:)')  

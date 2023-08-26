# Router module
# from django.urls import path
from mini_social.views import *

from django.urls import include, path


urlpatterns = [
    path('', homePage),
    # path('signup', signupPage),
    # path('signin', signinPage),
    # Post Routes
    path('post/create', addPost),
    # path('add-post', addPost),
    # path('save-post', savePost),
    path('post/save', savePost),
    # path('user/profile/<int:id>', userProfile),
    
    # hw5 finish all of these views/urls
    path('get-posts', getPosts), # read post
    # path('delete-post/<str:title>', deletePost),
    path('delete-post/<int:post_id>', deletePost),
    # path('update-post', updatePost),
    path('post/edit-post/<int:post_id>', changePost),
    # path('change-post', changePost),
    path('user/post/<int:post_id>', personalPost),

    #  user routes
    path("user/register", registerUser),
    path("user/login", loginUser),
    path("user/logout", logoutUser),
    path("user/preferences/notifications", toggleUserNotification),
    
    path("user/profile/<int:id>", userProfile ),
    path("user/profile/edit/<int:id>", editUserProfile ),
    path("user/add/friend/<int:id>", addUserFriend ),
    path("user/remove/friend/<int:id>", removeUserFriend ),  

    # development debug
    path("__debug__/", include("debug_toolbar.urls")),  
    
]

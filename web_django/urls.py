# Router module
from django.urls import path
from mini_social.views import *


urlpatterns = [
    path('', homePage),
    path('signup', signupPage),
    path('signin', signinPage),
    # Post Routes
    path('add-post', addPost),
    path('save-post', savePost),
    path('get-posts', getPosts), # read post
    path('delete-post', deletePost),
    path('update-post', updatePost),
    path('change-post', changePost),
]

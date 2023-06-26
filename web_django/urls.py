# Router module
from django.urls import path
from mini_social.views import *


urlpatterns = [
    path('', homePage),
    path('signup', signupPage),
    path('signin', signinPage),
    # Post Routes
    path('add-post', addPost),
    path('delete-post', deletePost),
]

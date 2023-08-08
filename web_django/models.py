from django.db import models
from django.contrib.auth.models import User



# proxy Extending model
class CustomUser(User):
    avatar = models.CharField(max_length=150, default='')  

    # Friendship!!!
    friends = models.ManyToManyField('self')
    session_data_backup = models.TextField(default='')    

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200, default='')
    comments = models.CharField(max_length=200, default='')
    messages = models.CharField(max_length=200, default='')
    posts = models.CharField(max_length=200, default='')

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    pass

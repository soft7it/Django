from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200, default='')
    comments = models.CharField(max_length=200, default='')
    messages = models.CharField(max_length=200, default='')
    posts = models.CharField(max_length=200, default='')

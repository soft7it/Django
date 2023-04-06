from random import randint
from time import time

from .User import User
from .Post import Post

class EntityFactory:

    def create(type, params):  # params - dict
        if type == 'user':
            user = User(params['username'], params['email'], params['password'],)
            user.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
            return user
        
        elif type == 'post':
            post = Post(params['title'], params['body'], params['authorId'],)
            post.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
            return post
        
        else:
            raise TypeError(f'EntityFactory cannot create {type} type !!!')

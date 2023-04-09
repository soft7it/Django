from random import randint
from time import time

from .User import User
from .Post import Post
from .IdentificationService import IdentificationService
# from .Comment import Comment 
# from .Message import Message
# from .Reaction import Reaction  

class EntityFactory:

    def create(type, params, withId = True):  # params - dict
        if type == 'user':
            user = User(params['username'], params['email'], params['password'],)
            if withId:
                # user.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
                user.id = IdentificationService.getId()
            return user
        ######################################
        elif type == 'post':
            post = Post(params['title'], params['body'], params['authorId'],)
            if withId:
                post.id = IdentificationService.getId()
            return post
                
        else:
            raise TypeError(f'EntityFactory cannot create {type} type !!!')

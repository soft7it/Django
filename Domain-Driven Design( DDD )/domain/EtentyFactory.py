from random import randint
from time import time

from .User import User
from .Post import Post
from .Comment import Comment
from .Reaction import Reaction
from .Message import Message
from .IdentificationService import IdentificationService
# user.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'

class EntityFactory:

    def create(type, params, withId = True):  # params - dict
        if type == 'user':
            user = User(params['username'], params['email'], params['password'],)
            if withId:
                user.id = IdentificationService.getId()
            return user
        ######################################
        elif type == 'post':
            post = Post(params['title'], params['body'], params['authorId'],)
            if withId:
                post.id = IdentificationService.getId()
            return post
                
        ######################################
        elif type == 'comment':
            comment = Comment(
                params['type'], params['authorId'], params['post_id'])
            if withId:
                comment.id = IdentificationService.getId()
            return comment
                       
        ######################################
        elif type == 'reaction':
            reaction = Reaction(params['type'], params['authorId'], params['post_id'])
            if withId:
                reaction.id = IdentificationService.getId()
            return reaction
                
        ######################################
        elif type == 'message':
            message = Message(params['body'], params['authorId'], params['receiverId'])
            if withId:
                message.id = IdentificationService.getId()
            return message
                
        else:
            raise TypeError(f'EntityFactory cannot create {type} type !!!')

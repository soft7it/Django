from random import randint
from time import time

from .User import User
from .Post import Post
from .IdentificationService import IdentificationService
# from .Comment import Comment 
# from .Message import Message
# from .Reaction import Reaction  

class EntityFactory:

    def create(type, params):  # params - dict
        if type == 'user':
            user = User(params['username'], params['email'], params['password'],)
            # user.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
            user.id = IdentificationService.getId()
            return user
        ######################################
        elif type == 'post':
            post = Post(params['title'], params['body'], params['authorId'],)
            post.id = IdentificationService.getId()
            return post
                
        else:
            raise TypeError(f'EntityFactory cannot create {type} type !!!')
        
        
        ###################################### 
        # elif type == 'comment':
        #     comment = Comment(params['id'], params['body'], params['targetId'], params['authorId'],)
        #     comment.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
        #     return comment
        # ########################################
        # elif type == 'message':
        #     message = Message(params['id'], params['type'], params['targetId'], params['authorId'],)
        #     message.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
        #     return message
        # ########################################
        # elif type == 'reaction':
        #     reaction = Reaction(params['id'], params['type'], params['targetId'], params['authorId'],)
        #     reaction.id = f'{int(time() * 1000)}-{randint(100000000, 9000000000)}'
        #     return reaction

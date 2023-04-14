from .EtentyFactory import EntityFactory
from .User import User
from .Post import Post


class UserRepository:
    # CRUD + EXTENSION

    # SUPPOSE this is DB

    db = {
        # list of dictionaries
        'users': [
            {
                'id' : '12345',
                'username' : 'jhony',
                'email' : 'hhony@h.com',
                'password' : '123'
            },
            {
                'id' : '56987',
                'username' : 'mony',
                'email' : 'mony@h.com',
                'password' : '654'
            }
        ],
        'posts' : [
        
        ]
    }

    ##########  USER STORAGE METHOD #############################
    def getUser(id):
    #     # HW : should find the user by id and return an User object
    #     # also it will return None if not found 
        
        for user_data in UserRepository.db['users']:
            if user_data['id'] == id:
                user = EntityFactory.create('user', user_data, False)
                user.id = user_data['id']
                return user
        return None        

    def getAllUsers():
        users = []
        for user_data in  UserRepository.db['users']:
            user = EntityFactory.create('user', user_data, False)
            user.id = user_data['id']
            users.append(user)
        return users

    # save the user for the first time  
    def saveUser( user ):
        if type(user) != User:
            raise TypeError('Error : saveUser argument should be of User type')  
        
        user_data = {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
            'password' : user.password,
        }

        UserRepository.db['users'].append(user_data)

    # save changes for existing user
    def updateUser( user ):
        for user_data in UserRepository.db['users']:
            if user_data['id'] == user.id:
                user_data['username'] = user.username
                user_data['email'] = user.email
                user_data['password'] = user.password
                break

    # HW
    def deleteUser( user ):  
        for user_data in UserRepository.db['users']:
            if user_data['id'] == user.id:
                UserRepository.db['users'].remove(user_data)
                # del UserRepository.db['user']
                break    

    ##########  POSTS LOGIC STORAGE METHOD #############################
     # save the user for the first time
    def savePost(post):
        if type(post) != Post:
            raise TypeError('Error : savePost argument should be of Post type')

        post_data = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'authorId': post.authorId,
        }

        UserRepository.db['posts'].append(post_data)

    # save changes for existing post
    def updatePost(post):
        for post_data in UserRepository.db['posts']:
            if post_data['id'] == post.id:
                post_data['title'] = post.title
                post_data['body'] = post.body
                # post_data['authorId'] = post.authorId
                break

#############  getPosts  #############################

    def getPost(id):
        for post_data in UserRepository.db['posts']:
            if post_data['id'] == id:
                post = EntityFactory.create('post', post_data, False)
                post.id = post_data['id']
                return post
        return None
    
#############  getAllPosts  ##########################

    def getAllPosts():
        posts = []
        for post_data in UserRepository.db['posts']:
            post = EntityFactory.create('post', post_data, False)
            post.id = post_data['id']
            posts.append(post)
        return posts

# HW : deletePost(), updatePost(), getPost(), getAllPost()

    def deletePost(post):
        for post_data in UserRepository.db['posts']:
            if post_data['id'] == post.id:
                UserRepository.db['posts'].remove(post_data)
                break

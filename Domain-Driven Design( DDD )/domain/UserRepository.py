from .EtentyFactory import EntityFactory
from .User import User


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
                'password' : '12345'
            },
            {
                'id' : '56987',
                'username' : 'mony',
                'email' : 'mony@h.com',
                'password' : '654'
            },
        ]
    }

    def getUser(id):
        # HW : should find the user by id and return an User object
        # also it will return None if not found 
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
        for i, user_data in enumerate(UserRepository.db['users']):
            if user_data['id'] == user.id:
                del UserRepository.db['user'][i]
                break    






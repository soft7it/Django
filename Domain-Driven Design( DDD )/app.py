from domain.EtentyFactory import EntityFactory
from domain.UserRepository import UserRepository

u1 = EntityFactory.create('user',{'username': 'John', 'email': 'j@d.com', 'password': '123456'})
UserRepository.saveUser(u1)
## save in DB
u1.username = 'new name'
# update in DB
UserRepository.updateUser(u1)

users = UserRepository.getAllUsers()

for u in users:
    print(u.id)
    print(u.username)
print('*'*50)
#######  getObj ############################
print(users)

print('*'*50)
#######  getUser() ############################
u1 = UserRepository.getUser('56987')
if u1:
    print(u1)
else:
    print('User not found.')
print('*'*50)
#######  deleteUser() ############################
u1 = UserRepository.getUser('56987')
UserRepository.deleteUser(u1)
if u1:
    print(UserRepository.db)
else:
    print('User not found.')
print('*'*50)
#######  postUser() ############################
u1 = UserRepository.getUser('12345')

p1 = EntityFactory.create('post',{
    'title': 'The first post by jhony',
    'body' : 'tralala tralala tralala',
    'authorId' : u1.id
})

UserRepository.savePost(p1)
print(UserRepository.db)
print('*'*50)

#######  deletePost() ############################
#######  updatePost() ############################
#######  getPost()    ############################
#######  getAllPost() ############################

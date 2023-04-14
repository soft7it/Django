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
# u1 = UserRepository.getUser('56987')
# UserRepository.deleteUser(u1)
# if u1:
#     print(UserRepository.db)
# else:
#     print('User not found.')
# print('*'*50)

#######  postUser() 1 ############################
print('FIRST POST')
u1 = UserRepository.getUser('12345')

p1 = EntityFactory.create('post',{
    'title': 'The first post by jhony',
    'body' : 'tralala tralala tralala',
    'authorId' : u1.id
})

UserRepository.savePost(p1)
print(UserRepository.db)
print('*'*50)
#######  postUser() 2 ############################
print('FIRST POST')
u1 = UserRepository.getUser('56987')

p1 = EntityFactory.create('post',{
    'title': 'Hello friends',
    'body' : 'learning software',
    'authorId' : u1.id
})

UserRepository.savePost(p1)
print(UserRepository.db)
print('*'*50)

#######  updatePost() 1 ############################
print('UpDate POST ')
u1 = UserRepository.getUser('12345')

p1.title = 'The UpDate the first post by jhony'
p1.body = 'xaxaxaxa xaxxaxa xaxaxxaaaxa'

UserRepository.updatePost(p1)
print(UserRepository.db)
print('*'*50)
#######  updatePost() 2 ############################
print('UpDate POST ')
u1 = UserRepository.getUser('56987')

p1.title = 'Meau zoro'
p1.body = 'IHAaxaxa xaxxaxa xaxaxxaaaxa'

UserRepository.updatePost(p1)
print(UserRepository.db)
print('*'*50)

#######  getPost()    ############################
print('GET POST 1')
user_post = UserRepository.getPost('12345')
if user_post:
    print(user_post)
else:
    print('Post not found.')
print('*'*50)

#######  getAllPost() ############################
print('GET ALL POSTS')
posts = UserRepository.getAllPosts()

for u in posts:
    print('*'*25)
    print(u.id)
    print(u.title)
    print(u.body)
print('*'*50)

#######  deletePost() ############################
print('DELETE')
u1 = UserRepository.getUser('12345')
UserRepository.deletePost(u1)
if u1:
    print(UserRepository.db)
else:
    print('Post not found.')
print('*'*50)

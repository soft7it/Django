from domain.EtentyFactory import EntityFactory
from domain.UserRepository import UserRepository

u1 = EntityFactory.create('user',{'username': 'John', 'email': 'j@d.com', 'password': '123456'})
UserRepository.saveUser(u1)
## save in DB
u1.username = 'new name'
## update in DB
UserRepository.updateUser(u1)

users = UserRepository.getAllUsers()
# print(users)

for u in users:
    print(u.id)
#     print(u.username)

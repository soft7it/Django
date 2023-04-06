from domain.EtentyFactory import EntityFactory

u1 = EntityFactory.create('user',{'username': 'John', 'email': 'j@d.com', 'password': '123456'})
u2 = EntityFactory.create('post', {'title': 'good', 'body':'great', 'authorId':' Romaska'})

print(u1)
print(u2)

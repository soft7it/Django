from domain.EtentyFactory import EntityFactory

u1 = EntityFactory.create('user',{'username': 'John', 'email': 'j@d.com', 'password': '123456'})

print(u1)
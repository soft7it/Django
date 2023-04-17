from domain.EtentyFactory import EntityFactory
from domain.UserRepository import UserRepository

# From a post  -> find the author`s name

user = UserRepository.getUserWithPosts('1')

for post in user.posts:
    print(post.title)

#######  another variant #####################
# post = UserRepository.getPost('1')
# author = UserRepository.getUser(post.authorId)

# print(author.authorId)

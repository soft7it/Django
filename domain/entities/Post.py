import time
from random import randint
from EntityName import Entity


class Post(Entity):
    def __init__(self, title, body, authorId):
        super().__init__()
        self.title = title
        self.body = body

        self.createdAt = int(randint(time.time() * 1000))
        self.updatedAt = self.createdAt
        self.authorId = authorId

        self.id = f"{self.id}-{self.createdAt}"

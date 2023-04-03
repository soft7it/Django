from .Entity import Entity

class Post(Entity):

    def __init__(self, title, body, authorId):
        super().__init__()

        self.title = title
        self.body = body
        self.authorId = authorId
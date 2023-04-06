from .Entity import Entity

class Post(Entity):

    def __init__(self, title, body, authorId):
        super().__init__()

        self.title = title
        self.body = body
        self.authorId = authorId
        self.id = None  # the id will be set by the EntityFactory

    def __str__(self):
        return f"{self.title} by user {self.authorId} felt {self.body}"
 

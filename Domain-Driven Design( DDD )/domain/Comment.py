# id
# body
# targetId
# authorId

from .Entity import Entity

class Comment(Entity):

    def __init__(self, id, body, targetId, authorId):
        super().__init__()

        self.id = id
        self.body = body
        self.targetId = targetId
        self.authorId = authorId

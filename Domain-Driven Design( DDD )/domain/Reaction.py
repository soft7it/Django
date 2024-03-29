# id
# type
# targetId
# authorId

from .Entity import Entity

class Reaction(Entity):

    def __init__(self, id, type, targetId, authorId):
        super().__init__()

        self.id = id
        self.type = type
        self.targetId = targetId
        self.authorId = authorId

    def __str__(self):
        return f'Reaction {self.id} {self.type} {self.targetId} {self.authorId}'

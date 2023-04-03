from .Entity import Entity

class User(Entity):

    def __init__(self, username, email, password):
        super().__init__()

        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'USER {self.username} {self.email}'     
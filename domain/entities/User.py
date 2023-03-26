from random import randint

import time
from random import randint
from EntityName import Entity


class User(Entity):
    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password
        
        self.registeredAt = int(randint(time.time() * 1000))
        self.lastLoginAt = None
        self.online = False

        self.id = f"{self.id}-{self.registeredAt}"

from random import randint


class Entity:
    def __init__(self):
        self.id = f"{randint(1_000_000_000,9_999_999_999)}"

# Module Defines the 'Product' class
# Provider

# Class = Creator + Structure + Behavior

class Prpduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'[Product]<{self.name:15} : {self.price:7.2f}>'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # comparison operator like less than or equal to (<=), greater than or equal to (>=), equal to (==), or not equal to (!=).
    def __eq__(self, other):
        return self.age == other.age

p1 = Person('Mikel', 15)
p2 = Person('Joe', 15)        

if p1 == p2:
    print('Mikel and Joe are of the same ages')
else:
    print('Mikel and Joe are of diffrent ages')

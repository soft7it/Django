class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):  # method in Python that stands for "greater than"
        return self.age > other.age

p1 = Person('Vitaly', 23)
p2 = Person('Mario', 35)    

if p1 > p2:
    print('Vitaly is older than Mario')
else:
    print('Mario is older Vitaly')    
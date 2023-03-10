class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):  # method in Python that stands for "less than"
        return self.age < other.age

p1 = Person('Vitaly', 23)
p2 = Person('Cristi', 34)

if p1 < p2:
    print('Vitaly is yonger than Cristi.')
else:
    print('Cristi is yonger than Vitaly.')

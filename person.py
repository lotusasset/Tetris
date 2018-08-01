class Person:
    name = 'Pheby'
    age = 57

class Human:
    def __init__(self, name,age):
        self.name = name
        self.age=age

    def older(self):
        print(self.age+10)
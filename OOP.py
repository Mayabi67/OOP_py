class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def intro (self):
        print('This persons name is',self.name,'they are', self.age,'years old','and they are', self.gender,'.')
# Creating an instance of the Person class
p1=Person('Mathias',31,'Male')
# Calling the intro method
p1.intro ()
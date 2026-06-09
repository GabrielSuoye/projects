class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    def __init__(self, name, age, degree):
        super().__init__(name=name, age=age)
        self.degree = degree

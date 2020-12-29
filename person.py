from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce_yourself(self):
        print(f'Hi my name is {self.name} {self.surname}')


class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade = str(grade)


class Teacher(Person):
    def __init__(self, name, surname, degree):
        super().__init__(name, surname)
        self.degree = degree

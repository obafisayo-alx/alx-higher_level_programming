#!/usr/bin/python3
"""Module implementing class with method to serialize itself"""


class Student:
    """class to rep student"""
    def __init__(self, first_name, last_name, age):
        """initialize student instance with first, last names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """creates copy of attributes for use in json string"""
        return self.__dict__.copy()

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
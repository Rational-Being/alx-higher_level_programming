#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

class Student:
    """
    creates calss studnet
    
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return vars(self)

    def reload_from_jason(self, json):
        return None

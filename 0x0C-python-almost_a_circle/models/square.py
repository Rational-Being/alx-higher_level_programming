#!/usr/bin/python3

"""
This module crreates a square using tha atributes of a  retangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square

    Inherits from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the square class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        defines te str metod
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        size getter
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        experimenting with no-keyword aruments
        """
        if args is not None and len(args) != 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size == arg
                elif count == 2:
                    self.x == arg
                elif count == 3:
                    self.y == arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns te dictionary of a te square class
        """
        return {"id": self.id, "x": self.x, "y": self.y, "size": self.size}

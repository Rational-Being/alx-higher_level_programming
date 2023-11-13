#!/usr/bin/python3

"""
This module crreates the a retangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle

    Inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes the rectnagle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ "
        property of the above named attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter of the above named attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ "
        property of the above named attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter of the above named attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ "
        property of the above named attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter of the above named attribute
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ "
        property of the above named attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter of the above named attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates te area of te rectanle
        """
        return self.__width * self.__height

    def display(self):
        """
        print te rectanle in # char
        """

        for i in range(self.y):
            print("")
        for i in range(self.__height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        defines te str metod
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        experimenting with no-keyword aruments
        """
        if args is not None and len(args) != 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width == arg
                elif count == 2:
                    self.height == arg
                elif count == 3:
                    self.x == arg
                elif count == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns te dictionary of a te square class
        """
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }

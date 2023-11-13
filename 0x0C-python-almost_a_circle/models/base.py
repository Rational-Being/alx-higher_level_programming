#!/usr/bin/python3

"""
This module crreates the a class
"""

import json
import csv


class Base:
    """
    Class Base

    Attributes - private class attirbutes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns te json of a dictionary
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes json sting to file
        """
        n_o_f = cls.__name__ + ".json"  # n_o_f = name of file
        w_t_s = []  # w_t_S = wht to save
        if list_objs is not None:
            for i in list_objs:
                w_t_s.append(cls.to_dictionary(i))
        with open(n_o_f, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(w_t_s))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of json string rep
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance witha ll attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "r") as fil:
                f = cls.from_json_string(fil.read())
            return [cls.create(**x) for x in f]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        deserialize csv fie
        """
        namefile = cls.__name__ + ".csv"
        try:
            with open(namefile, "r", newline="") as fil:
                if cls.__name__ == "Rectangle":
                    paras = ["id", "width", "height", "x", "y"]
                else:
                    paras = ["id", "size", "x", "y"]
                dict_content = csv.DictReader(csvfile, paras=paras)
                dict_content = [
                    dict([key, int(value)] for key, value in a.items())
                    for a in dict_content
                ]
                return [cls.create(**a) for a in dict_content]
        except IOError:
            return []

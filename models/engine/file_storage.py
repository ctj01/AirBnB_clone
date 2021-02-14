#!/usr/bin/python3
"""
Base model class definition
"""

from models.base_model import BaseModel
import json


class FileStorage(BaseModel):
    """
    Filestorage implementation
    """
    __file_path = "object.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj ([type]): [description]
        """
        self.__objects = obj[type(obj).__name__ + '.' + obj.id].id

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        a = dict()
        for key, value in self.__objects.items():
            a = dict(key, value)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(a,f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r",
                      encoding='utf-8') as read_file:
                type(self).__objects = json.load(read_file)
            for key, value in type(self).__objects.items():
                obj = eval(type(self).__objects[key]['__class__'])(**value)
                type(self).__objects[key] = obj

        except FileNotFoundError:
            pass

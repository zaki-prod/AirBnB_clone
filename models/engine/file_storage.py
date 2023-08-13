#!/usr/bin/python3

"""
This defines A FileStorage class
"""

import json
import datetime


class FileStorage:
    """This class Sotrage serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file(path:__file_path)"""
        tempDict = {}
        for key, value in FileStorage.__objects.items():
            tempDict[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as JF:
                json.dump(tempDict, JF)

    def allclasses(self):
        """Returns a dictionary of accepted classes with references"""
        from models.base_model import BaseModel
        # from models.user import User
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.place import Place
        # from models.review import Review

        allclasses = {
                    "BaseModel": BaseModel,
                    #  "User": User,
                    #  "State": State,
                    #  "City": City,
                    #  "Amenity": Amenity,
                    #  "Place": Place,
                    #  "Review": Review
                    }
        return allclasses

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)"""

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as JS:
                dictObj = json.load(JS)
                for valObj in dictObj.values():
                    clsName = valObj['__class__']
                    clsObj = self.allclasses()[clsName]
                    self.new(clsObj(**valObj))
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""FileStorage Module"""

from models.base_model import BaseModel
from json import dumps, loads
from os import path


class FileStorage:
    """Serializes instances to JSON file and also the reverse"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        objects = FileStorage.__objects

        with open(FileStorage.__file_path, 'w', encoding="UTF_8") as file:
            for i in objects:
                dictionary[i] = objects[i].to_dict()
            file.write(dumps(dictionary))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
            deserialized = loads(file.read())

            for key in deserialized:
                value = deserialized[key]
                name_class = value["__class__"]
                object = eval(name_class)(**value)
                FileStorage.__objects[key] = object

    def delete(self, class_name, id):
        """Delete an instance from storage"""
        FileStorage.__objects.pop("{}.{}".format(class_name, id))
        self.save()

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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        update_dict = {}
        temp_dict = self.__objects
        for key, value in temp_dict.items():
            update_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as my_open:
            json.dump(update_dict, my_open)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        exists = os.path.isfile(self.__file_path)
        if exists:
            with open(self.__file_path) as my_load:
                data_load = json.load(my_load)
            for key in data_load.values():
                my_new_class = key["__class__"]
                del key["__class__"]
                self.new(eval(my_new_class)(**key))
        else:
          return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        objects = FileStorage.__objects

        with open(FileStorage.__file_path, "w", encoding="UTF_8") as file:
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

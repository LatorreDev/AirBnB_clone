#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        #print (obj, "Debug")
        #self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj
        self.__objects["Hello"] = obj

    def save(self):
        update_dict = {}
        temp_dict = self.__objects
        print("My objects\n", self.__objects)
        for key, value in temp_dict.items():
            print(type(key), "For Debugger")
            update_dict[key] = value.to_dict()
        with open (self.__file_path, 'w') as my_open:
            print("dict", update_dict)
            json.dump(update_dict, my_open)
           # var = my_open.write()

    def reload(self):
        print("Reload Debugger")
        exists = os.path.isfile(self.__file_path)
        if exists:
            with open(self.__file_path) as my_load:
                data_load = json.load(my_load)
            self.__objects = data_load
        else:
            pass


#!/usr/bin/python3

from uuid import uuid4
import models
import datetime
import json


class BaseModel:

    def __init__(self, *args, **kwargs):
        my_time = datetime.datetime.now()
        self.id = str(uuid4())
        self.created_at = my_time
        self.updated_at = my_time


        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = my_time
            models.storage.new(self)

    def __str__(self):
        my_name = str("[" + self.__class__.__name__ + "]")
        my_id = str("(" + self.id + ")")
        my_dict = str(self.__dict__)
        return(my_name + " " + my_id + " " + my_dict)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] =  self.created_at.isoformat()
        new_dict["updated_at"] =  self.updated_at.isoformat()
        return (new_dict)

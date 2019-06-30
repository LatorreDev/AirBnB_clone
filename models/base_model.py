#!/usr/bin/python3

from uuid import uuid4
import datetime
import json


class BaseModel:
    id = ""
    created_at = 0
    updated_at = 0

    def __init__(self, *args, **kwargs):
        my_time = datetime.datetime.now().isoformat()
        self.id = str(uuid4())
        self.created_at = my_time
        self.updated_at = my_time

        if kwargs is None:
            self.id = str(uuid4())
            self.created_at = my_time
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        my_name = "[<" + self.__class__.__name__ + ">]"
        my_id = str("(<" + self.id + ">)")
        my_dict = str(self.__dict__)
        return(my_name + " " + my_id + " " + my_dict)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return (self.__dict__)

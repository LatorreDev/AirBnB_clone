#!/usr/bin/python3

from uuid import uuid4
import datetime

class BaseModel:
    id = ""
    create_at = 0
    update_at = 0
    def __init__(self):
        my_time = datetime.datetime.now()
        self.id = str(uuid4())
        self.create_at = my_time
        self.update_at = my_time
    def __str__(self):
        my_name = "[<" + self.__class__.__name__ + ">]"
        my_id = str("(<" + self.id + ">)")
        my_dict = str(self.__dict__)
        return ( my_name + " " + my_id + " " + my_dict)
    def save(self):
        self.update_at = datetime.datetime.now()
    def to_dict(self):
        return (self.__dict__)

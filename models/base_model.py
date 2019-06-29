#!/usr/bin/python3

from uuid import uuid4
import datetime

class BaseModel:
    id = ""
    create_at = 0
    update_at = 0
    def __init__(self, id, created_at, updated_at):
        my_time = datetime.datetime.now()
        self.id = str(uuid4())
        self.create_at = my_time
        self.update_at = my_time
    def __str__(self):
        print(type(self))


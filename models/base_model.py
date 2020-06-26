#!/usr/bin/python3
"""
BaseModel - Module

Parent class to take care of the initialization,
serialization and deserialization of instances
 """

import uuid
import datetime


class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        msg = "[{}] ({}) {}"
        return msg.format(self.__class__.__name__, self.id, self.__dict__)



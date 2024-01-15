#!/usr/bin/python3
import uuid
from datetime import datetime
#Write a class BaseModel that defines all common attributes/methods for other classes

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def save(self):
        class_name = self.__class__.__name__
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = class_name
        dict_representation['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_representation['uodated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dict_representation
    def __str__(self):
        class_name = self.__class__.__name__
g       return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

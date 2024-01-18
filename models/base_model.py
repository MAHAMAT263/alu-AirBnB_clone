#!/usr/bin/python3
# models/base_model.py
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    instance = BaseModel()
    print(type(instance.id)
    instance = BaseModel()
    print(type(instance.created_at))
    instance = BaseModel()
    print(type(instance.updated_at))

    # 2 instances creation + id different
    instance1 = BaseModel()
    instance2 = BaseModel()
    print(instance1.id != instance2.id)  # Expected: True

    
    instance = BaseModel()
    print(str(instance))  # Expected: [BaseModel] (<instance.id>) <instance.__dict__>

    instance = BaseModel()
    print(type(instance.to_dict()))  # Expected: <class 'dict'>
    print(type(instance.to_dict()['created_at']))  # Expected: <class 'str'>
    print(type(instance.to_dict()['updated_at']))  # Expected: <class 'str'>
    print(type(instance.to_dict()['__class__']))  # Expected: <class 'str'>
    print(instance.to_dict()['__class__'])  # Expected: 'BaseModel'

    instance = BaseModel()
    instance.save()
    print(type(instance.updated_at))  # Expected: <class 'datetime.datetime'>
    print(type(instance.to_dict()['updated_at']))  # Expected: <class 'str'>


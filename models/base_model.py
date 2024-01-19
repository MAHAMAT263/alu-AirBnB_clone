#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict

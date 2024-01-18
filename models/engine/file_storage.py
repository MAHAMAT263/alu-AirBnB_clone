#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:

    CLASSES = {
    'BaseModel': BaseModel,
    'User': User,
    }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    # Import the class dynamically to avoid NameError
                    model_class = globals()[class_name]
                    obj_dict['__class__'] = class_name
                    obj = model_class(**obj_dict)
                    self.new(obj)
        except FileNotFoundError:
            pass

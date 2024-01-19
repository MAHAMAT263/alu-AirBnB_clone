#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    CLASSES = {
    'BaseModel': BaseModel,
    'User': User,}

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.save(obj)
    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)
    def reload(self, obj):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    if class_name in CLASSES:
                        obj = CLASSES[class_name](**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass


        except FileNotFoundError:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                file.write('{}')

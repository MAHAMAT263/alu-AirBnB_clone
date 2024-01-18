#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
            serialized_objects = json.load(file)

        for key, obj_dict in serialized_objects.items():
            class_name, obj_id = key.split('.')
            obj_class = globals()[class_name]
            obj_instance = obj_class(**obj_dict)
            self.__objects[key] = obj_instance

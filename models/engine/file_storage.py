#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
    """
    Deserializes the JSON file to __objects
    (only if the JSON file (__file_path) exists; otherwise, do nothing).
    If the file doesn’t exist, no exception should be raised.
    """
    if os.path.exists(self.__file_path):
        with open(self.__file_path, 'r') as file:
            data = json.load(file)
            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                # Import the class dynamically using importlib
                from models.base_model import BaseModel
                module = import_module('models.' + class_name)
                class_ = getattr(module, class_name)
                # Create an instance from the dictionary representation
                obj = class_.from_dict(obj_dict)
                self.__objects[key] = obj

#!/usr/bin/python3
import json
from datetime import datetime

class FileStorage:
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

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                class_name, obj_id = key.split('.')
                # Use globals() to get the class by its name as a string
                obj_class = globals()[class_name]
                obj = obj_class(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass

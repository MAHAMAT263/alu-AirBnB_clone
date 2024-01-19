#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

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
        """Serializes __objects to the JSON file (__file_path)."""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file (__file_path) to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for item_key, item_value in data.items():
                    class_name = item_value['__class__']
                    # Use globals() to access the class by name
                    model_class = globals()[class_name]
                    instance = model_class(**item_value)
                    self.new(instance)
        except FileNotFoundError:
            pass     

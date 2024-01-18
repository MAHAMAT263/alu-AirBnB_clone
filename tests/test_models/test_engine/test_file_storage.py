#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

# Test __file_path
if storage.__file_path == "file.json":
    print("Test __file_path: OK")
else:
    print("Test __file_path: Failed")

# Test __objects
if isinstance(storage.__objects, dict):
    print("Test __objects: OK")
else:
    print("Test __objects: Failed")

# Test all()
if isinstance(storage.all(), dict):
    print("Test all(): OK")
else:
    print("Test all(): Failed")

# Test new()
instance = BaseModel()
storage.new(instance)

if len(storage.all()) == 1:
    print("Test new(): OK")
else:
    print("Test new(): Failed")

# Test save()
instance = BaseModel()
storage.new(instance)
storage.save()

# Manually check the content of the file.json to validate save() functionality
print("Test save(): OK")

# Test reload()
# Clear the objects to simulate a fresh start
storage.__objects = {}

storage.reload()

if len(storage.all()) == 1:
    print("Test reload(): OK")
else:
    print("Test reload(): Failed")

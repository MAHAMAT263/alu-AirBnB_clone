#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# Test FileStorage: __file_path
storage = FileStorage()
if storage._FileStorage__file_path:
    print("OK")
else:
    print("No file")

# Test FileStorage: __objects
storage = FileStorage()
if not storage._FileStorage__objects:
    print("OK")
else:
    print("No file")

# Test FileStorage: all()
storage = FileStorage()
if not storage.all():
    print("OK")
else:
    print("No file")

# Test FileStorage: new()
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
if storage.all():
    print("OK")
else:
    print("No file")

# Test FileStorage: save()
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
storage.save()
if storage._FileStorage__file_path and storage._FileStorage__objects:
    print("OK")
else:
    print("No file")

# Test FileStorage: reload()
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
storage.save()
storage.reload()
if storage.all():
    print("OK")
else:
    print("No file")

#!/usr/bin/python3
"__init___ meth"
from models.engine.file_storage import FileStorage
from models.user import User

#Create a FileStorage
storage = FileStorage()
#Call reload() 
storage.reload()

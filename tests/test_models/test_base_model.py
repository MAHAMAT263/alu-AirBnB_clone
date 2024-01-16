#!/usr/bin/python3
from models.base_model import BaseModel

# Test BaseModel: to_dict()
bm1 = BaseModel()
d_json = bm1.to_dict()
assert type(d_json['created_at']) == str
assert type(d_json['updated_at']) == str
assert type(d_json['__class__']) == str
assert type(d_json) == dict

print("OK")

# Test BaseModel: self.id
bm2 = BaseModel()
assert type(bm2.id) == str

print("OK")

# Test BaseModel: self.created_at
bm3 = BaseModel()
assert type(bm3.created_at) == datetime

print("OK")

# Test BaseModel: __str__(self)
bm4 = BaseModel()
str_representation = str(bm4)
assert type(str_representation) == str

print("OK")

#!/usr/bin/python3

from models.base_model import BaseModel

if __name__ == "__main__":
    bm = BaseModel()

    # Test the to_dict method
    d_json = bm.to_dict()
    print(type(bm.created_at))
    print(type(d_json['created_at']))
    print(type(d_json['updated_at']))
    print(type(d_json['__class__']))

#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv as env
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User



if env("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

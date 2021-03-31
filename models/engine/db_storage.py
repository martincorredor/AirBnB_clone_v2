#!/usr/bin/python3
""" File to create a New engine """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import Column, Integer, String, DateTime, MetaData
import os
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User
from models.city import City


# Environment variables
env = {
    "USER": os.getenv('HBNB_MYSQL_USER'),
    "PASSWORD": os.getenv('HBNB_MYSQL_PWD'),
    "HOST": os.getenv('HBNB_MYSQL_HOST'),
    "STORAGE": os.environ.get('HBNB_TYPE_STORAGE'),
    "DATABASE": os.getenv('HBNB_MYSQL_DB'),
    "ENV": os.getenv('HBNB_ENV')
    }


class DBStorage:
    """ Class DBStorage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor function """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(env['USER'],
                                              env['PASSWORD'],
                                              env['HOST'],
                                              env['DATABASE'],
                                              pool_pre_ping=True))
        if env["ENV"] == "test":
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session all objects depending
        of the class name and this method must return a dictionary
        """
        Class = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        obj_dict = {}

        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj

        else:
            for all_c in Class:
                querys = self.__session.query(all_c).all()
                key = "{}.{}".format(all_c, querys.id)
                setattr(obj_dict, key, querys)

        return(obj_dict)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create the current
        database session
        """
        Base.metadata.create_all(self.__engine)
        # create a configured "Session" class
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create a Scoped Session
        self.__session = scoped_session(Session)

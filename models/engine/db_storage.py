#!/usr/bin/python3
""" File to create a New engine """
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor function """
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(pool_pre_ping=True))

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
        # create a Session
        self.__session = scoped_session(Session)

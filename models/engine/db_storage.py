#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import Base, BaseModel


class DBStorage:
    """
    New engine DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        # will be localhost
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        connection = 'mysql+mysqldb://{}:{}@localhost/{}'
        self.__engine = create_engine(connection.format(
            user, pwd, db), pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        return the dictionary of cls
        """
        objs_dict = {}
        if cls:
            my_query = self.__session.query(cls).all()
            for obj in my_query:
                objs_dict[cls.__name__ + "." + obj.id] = obj
        else:
            for key, value in self.classes.items():
                my_query = self.__session.query(value).all()
                for obj in my_query:
                    objs_dict[key + "." + obj.id] = obj

        return objs_dict

    def new(self, obj):
        """
        add a new object to db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit  the objetc to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ Remove method on the private session attribute """
        self.__session.close()

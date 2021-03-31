#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv as env


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all,delete')

    else:
        @property
        def cities(self):
            """Getter for cities using FileStorage
            """
            list_c = []
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    list_c = list_c.append[value]
            return list_c

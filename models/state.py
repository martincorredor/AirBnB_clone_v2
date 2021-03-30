#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',

                            cascade="all, delete, delete-orphan")

if env("HBNB_TYPE_STORAGE") != 'db':
    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals to the current State.id
        """
        new_list = []
        instances = FileStorage.all()
        for key, value in (instances):
            if value.state_id == State.id:
                new_list.append(value)
        return new_list

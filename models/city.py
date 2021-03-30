#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey=('states.id'))
    name = Column(String(128), nullable=False)

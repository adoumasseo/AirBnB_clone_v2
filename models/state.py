#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete, delete-orphan")

@property
def cities(self):
    """
        Handle The relationship between State and City
        for FileStorage
    """
    var = models.storage.all()
    list_cities = []
    result = []
    for key in var:
        city = key.replace('.', ' ')
        city = shlex.split(city)
        if (city[0] == 'City'):
            list_cities.append(var[key])
    for obj in list_cities:
        if (obj.state_id == self.id):
            result.append(obj)
    return (result)
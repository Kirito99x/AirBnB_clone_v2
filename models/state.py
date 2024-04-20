#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as ev


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if ev.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """get all cities with the current state id
            from filestorage
            """
            city_state_list = [
                i for m, i in models.storage.all(models.City).items()
                if i.state_id == self.id
            ]
            return (city_state_list)

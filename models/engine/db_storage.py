#!/usr/bin/python3
"""This module defines a class to manage db_storage for hbnb clone"""

import os
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

class DBStorage():
    """
        This class will handle DBStorage for HBNB
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            This method is the constructor of DBStorage
        """
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv('HBNB_ENV')
        connection_string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                                user, passwd, host, db
                            )
        self.__engine = create_engine(
                            connection_string,
                            pool_pre_ping=True
                            )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
            Return a ditionnary of all object of cls in the db
            If cls is None Return all object in the db
        """
        obj_dict = {}
        if cls is None:
            lista = [State, City, User, Place, Review, Amenity] 
            for classe in lista:
                objs = self.__session.query(classe).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
            add the object to the current database session
        """
        self.__session.add(obj)

    def save(self, obj):
        """
            commit all changes of the current database session 
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """
            create all tables in the database
            create the current database session
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
    
            
            


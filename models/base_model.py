#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.__init__ import storage



class BaseModel():
    """Class defines the attributes & methods of all other class"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__" and key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        values = dict(self.__dict__)
        values.update({"__class__": self.__class__.__name__,
                       "created_at": self.created_at.isoformat(),
                       "updated_at": self.updated_at.isoformat()})
        return values

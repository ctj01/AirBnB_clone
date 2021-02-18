#!/usr/bin/python3


"""
Base model class definition
"""


import uuid
from datetime import datetime

import models


def cast_datetime(key, value):
    """
    cast to datetime
    Args:
        key ([type]): [description]
        value ([type]): [description]

    Returns:
        [type]: [description]
    """
    if key == "updated_at" or key == "created_at":
        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        return value
    return value


class BaseModel:
    """
    Base model implementation
    """
    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, cast_datetime(key, value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        overrindin str mthod
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """
        updates the public instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """

        Returns:
            [dict]: [description]
        """
        a = dict(self.__dict__)
        a["updated_at"] = self.__dict__["updated_at"].isoformat()
        a["created_at"] = self.__dict__["created_at"].isoformat()
        a["__class__"] = self.__class__.__name__
        return a

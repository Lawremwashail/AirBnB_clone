#!/usr/bin/python3
"""
    Defines BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class"""

    def __init__(self):

        """construcutor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updated with the curretnt time"""

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns the dictionary of the BaseModel"""

        dict_ins = self.__dict__.copy()
        dict_ins["created_at"] = self.created_at.isoformat()
        dict_ins["updated_at"] = self.updated_at.isoformat()
        dict_ins["class_name"] = self.__class__.__name__

        return dict_ins

    def __str__(self):
        """Returns the string representation of the BaseModel Instance"""

        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

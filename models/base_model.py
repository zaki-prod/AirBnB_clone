#!/usr/bin/python3

"""
This is BaseModel, A base class for all classes.
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This Defines all common attributes/methods for other classes."""
    

    def __init__(self, *args, **kwargs):
        """This initialiezes instance attribute of the BaseModel.
        
        Args:
            *args: list of positional arguments
            **kwargs: dict of key-value of keyword arguments
        """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or  key == "updated_at":
                    date_time_object = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_time_object)
                else:
                    setattr(self, key, value)      

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns official representation of the string."""
        return ("[{}] ({}) {}>".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current datetime."""
        updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["updated_at"] = new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return new_dict

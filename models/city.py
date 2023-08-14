#!/usr/bin/pyhton3

"""Creates a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class manages city objects"""

    state_id = ""
    name = ""

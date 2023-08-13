#!/usr/bin/python3

"""Creates a user class"""
from models.base_model import BaseModel


class User(BaseMOdel):
    """This class manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

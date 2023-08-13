#!/usr/bin/python3

"""Creates a Review class"""

from models.base_model import BaseMode


class Review(BaseModel):
    """This class manages review objects"""
    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ 
    Review Class
    Representation of Place in the platform
    """

    place_id = ""
    user_id = ""
    text = ""

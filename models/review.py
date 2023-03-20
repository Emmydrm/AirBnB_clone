#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel
from models.place import Place
from models.user

class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""

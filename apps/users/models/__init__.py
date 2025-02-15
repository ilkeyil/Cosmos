"""
------
README
------

Be sure to define each model in the database in `__all__`.

Reference: `Django Migration Documentation <https://docs.djangoproject.com/en/3.0/topics/migrations/>`_
"""
from .board import Board
from .committee import Committee
from .user import Profile

__all__ = ["Board", "Committee", "Profile"]

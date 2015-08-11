# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.KeyPressComponent import KeyPressComponent

class KeyPressSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        # This class doesn't actually do anything
        pass

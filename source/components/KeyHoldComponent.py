# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from .KeyComponent import *

class KeyHoldComponent(KeyComponent):

    def __init__(self, actions):
        super().__init__()
        self.actions = actions
        self.active = []






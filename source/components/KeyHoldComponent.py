# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component
from .KeyComponent import *

class KeyHoldComponent(KeyComponent):

    def __init__(self, actions):
        self.actions = actions
        self.active = []


	
    


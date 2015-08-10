# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import System
from pyglet.window import key
from components.KeyHoldComponent import KeyHoldComponent
# from components.KeyPressComponent import KeyPressComponent

class KeyHoldSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt): 
        for e, holder in self.entity_manager.pairs_for_type(KeyHoldComponent):
            for k, a in holder.actions.items():
                if k in holder.active:
                    holder.parse(e, a)

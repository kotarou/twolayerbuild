# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from pyglet.window import key
from components.KeyHoldComponent import KeyHoldComponent
# from components.KeyPressComponent import KeyPressComponent

class KeyHoldSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        try:
            for e, holder in self.eman.pairsForType(KeyHoldComponent):
                for k, a in holder.actions.items():
                    if k in holder.active:
                        holder.parse(a)
        except TypeError:
            raise Exception("KeyholdSystem without any KeyHoldComponents")

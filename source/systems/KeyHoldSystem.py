# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from pyglet.window import key
from components import KeyHoldComponent

class KeyHoldSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        try:
            for e, holder in self.eman.pairsForType(KeyHoldComponent):
                for k, a in holder.actions.items():
                    if k in holder.active:
                        holder.parse(a[0])
                    else:
                        if len(a) > 1:
                            holder.parse(a[1])
        except TypeError:
            raise Exception("KeyholdSystem without any KeyHoldComponents")

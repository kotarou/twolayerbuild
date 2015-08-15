# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component

class Health(Component):
    __slots__ = "hp", "maxHp", "alive"
    def __init__(self, maxHp):
        super().__init__()
        self.hp     = maxHp
        self.maxHp  = maxHp
        self.alive  = True

# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component

class Health(Component):
    __slots__ = "hp", "maxHp"
    def __init__(self, maxHp):
        self.hp 	= maxHp
        self.maxHp = maxHp
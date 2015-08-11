# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.HealthComponent import Health

class HealthSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, health in self.eman.pairsForType(Health):
            if health.hp <= 0:
                print("I died!")

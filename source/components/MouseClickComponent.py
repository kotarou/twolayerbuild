# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from components.HealthComponent import Health

class MouseClickComponent(Component):

    def __init__(self, string="I can be clicked on!"):
        super().__init__()
        self.response = string

    def onClick(self, e, x, y):
        print(self.response)
        for e, health in e.eman.pairsForType(Health):
            health.hp = health.hp - 1;
            print(health.hp)

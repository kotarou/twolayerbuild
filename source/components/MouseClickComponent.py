# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component
from components.HealthComponent import Health

class MouseClickComponent(Component):

    def __init__(self, string="I can be clicked on!"):
        self.response = string

    def onClick(self, e, x, y):
        print(self.response)
        for e, health in e.eman.pairs_for_type(Health):
            health.hp = health.hp - 1;
            print(health.hp)

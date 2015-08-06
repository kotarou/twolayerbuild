# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component
from components.HealthComponent import Health

class MouseHoverComponent(Component):

    def __init__(self, string="I can be hovered over!"):
        self.response = string

    def onHover(self, e, x, y):
        print(self.response)


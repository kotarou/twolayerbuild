# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component

class MouseClickComponent(Component):

    def __init__(self, string="I can be clicked on!"):
        self.response = string

    def onClick(self, x, y):
        print(self.response)

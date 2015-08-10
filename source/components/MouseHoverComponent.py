# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import Component

class MouseHoverComponent(Component):

    def __init__(self, string="I can be hovered over!"):
        self.response = string
        self.hoverTime = 0
        self.active = False


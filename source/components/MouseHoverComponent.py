# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component

class MouseHoverComponent(Component):

    def __init__(self, string="I can be hovered over!"):
        super().__init__()
        self.response = string
        self.hoverTime = 0
        self.active = False


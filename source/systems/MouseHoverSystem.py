# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import System
from components.MouseHoverComponent import MouseHoverComponent

class MouseHoverSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt): 
        for e, hover in self.entity_manager.pairs_for_type (MouseHoverComponent):
            if hover.active:
            	print(hover.response)
            	hover.hoverTime += dt
            	print(hover.hoverTime)
            else:
            	hover.hoverTime = 0
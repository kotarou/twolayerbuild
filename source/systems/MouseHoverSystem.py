# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MouseHoverComponent import MouseHoverComponent

class MouseHoverSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        try:
            for e, hover in self.eman.pairsForType(MouseHoverComponent):
                if hover.active:
                    print(hover.response)
                    hover.hoverTime += dt
                    print(hover.hoverTime)
                else:
                    hover.hoverTime = 0
        except TypeError:
            raise Exception("Mouse Hover System invoked without any mouse hover components")

# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.KeyPressComponent import KeyPressComponent

class KeyPressSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        for e, hovers in self.eman.pairsforType(MouseHoverComponent):
            for hover in hovers:
                if hover.active:
                    print(hover.response)
                    hover.hoverTime += dt
                    print(hover.hoverTime)
                else:
                    hover.hoverTime = 0

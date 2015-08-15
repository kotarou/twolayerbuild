# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MouseHoverComponent import MouseHoverComponent
from components.SVAComponent import SVAComponent
from random import uniform
from util import Vector

class MouseHoverSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, dt):
        try:
            for e, hover in self.eman.pairsForType(MouseHoverComponent):
                if hover.active:
                    #print(hover.response)
                    hover.hoverTime += dt
                    e.getSingleComponentByType(SVAComponent).S += Vector(uniform(-100,100),uniform(-100,100),0)
                else:
                    hover.hoverTime = 0
        except TypeError:
            raise Exception("Mouse Hover System invoked without any mouse hover components")

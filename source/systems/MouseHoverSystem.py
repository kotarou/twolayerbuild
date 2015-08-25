# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MouseHoverComponent import MouseHoverComponent
from components.SVAComponent import SVAComponent
from util import Vector

class MouseHoverSystem(System):

    def __init__(self):
        super().__init__()

    def update(self, dt):
        try:
            for e, hover in self.eman.pairsForType(MouseHoverComponent):
                if hover.active:
                    #print(hover.response)
                    hover.hoverTime += dt
                    self.parse(e, hover)
                else:
                    hover.hoverTime = 0
        except TypeError:
            raise Exception("Mouse Hover System invoked without any mouse hover components")

    def parse(self, e, hover):
        d = globals()
        d["eman"] = e.eman
        d["owner"] = e
        d["SVAComponent"] = SVAComponent
        d["Vector"] = Vector
        exec(hover.input, globals(), d)

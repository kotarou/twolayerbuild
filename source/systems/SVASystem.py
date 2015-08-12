# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.SVAComponent import SVAComponent

class SVASystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, sva in self.eman.pairsForType(SVAComponent):
            sva.V += sva.A
            sva.S += sva.V
            # TODO implement angular shite

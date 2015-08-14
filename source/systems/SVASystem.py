# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.SVAComponent import SVAComponent
from components.CollisionComponent import CollisionComponent

class SVASystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, sva in self.eman.pairsForType(SVAComponent):
            # Linear
            sva.V += sva.A
            sva.S += sva.V

            # Rotational
            sva.OMEGA += sva.ALPHA
            sva.THETA += sva.OMEGA
            # if sva.THETA > 360:
            #     sva.THETA -= 360
            # if sva.THETE < -360:
            #     sva.THETA += 360

            # TODO implement angular shite


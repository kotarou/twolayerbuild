# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from util import Vector
from components.CollisionComponent import CollisionComponent
from components.SVAComponent import SVAComponent

class CollisionSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        # First, update for changes in SVA
        for e0, c0 in self.eman.pairsForType(CollisionComponent):
            d0 = Vector(0,0,0)
            r0 = Vector(0,0,0)
            for sva in e0.getComponentsByType(SVAComponent):
                # Offset by position
                d0 += sva.S
                r0 += sva.THETA

            if c0.active:
                for e1, c1 in self.eman.pairsForType(CollisionComponent):
                    if e0 is not e1 and c1.active:
                        d1 = Vector(0,0,0)
                        r1 = Vector(0,0,0)
                        for sva in e1.getComponentsByType(SVAComponent):
                            d1 += sva.S
                            r1 += sva.THETA
                        bCollides = c0.collidesWith(d0, d1, r0, r1, c1)
                        if bCollides:
                            print(e0, " collides with ", e1)






# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from util import Vector
from components.CollisionComponent import CollisionComponent
from components.MeshComponent import MeshComponent
import time

class CollisionSystem(System):

    def __init__(self):
        super().__init__()

    def update(self, _):
        # First, update for changes in SVA
        for e, c in self.eman.pairsForType(CollisionComponent):
            self.newAABB(c, e)

        for e0, c0 in self.eman.pairsForType(CollisionComponent):
            # d0 = Vector(0,0,0)
            # r0 = Vector(0,0,0)
            # for sva in e0.getComponentsByType(SVAComponent):
            #     # Offset by position
            #     d0 += sva.S
            #     r0 += sva.THETA

            if c0.active:
                for e1, c1 in self.eman.pairsForType(CollisionComponent):
                    if e0 is not e1 and c1.active:
                        bCollides = self.collidesWithAABB(c0, c1)
                        if bCollides:
                            print(e0, " collides with ", e1)
                            print(int(round(time.time() * 1000)))

    def newAABB(self, obj, owner):
        obj.tl = Vector(99999, -9999, -999999)
        obj.br = Vector(-99999, 9999, 999999)
        for mesh in owner.getComponentsByType(MeshComponent):
            for triangle in mesh.triangles:
                for vertex in triangle:
                    obj.tl.x = min(vertex[0], obj.tl.x)
                    obj.tl.y = max(vertex[1], obj.tl.y)
                    obj.tl.z = max(vertex[2], obj.tl.z)

                    obj.br.x = max(vertex[0], obj.br.x)
                    obj.br.y = min(vertex[1], obj.br.y)
                    obj.br.z = min(vertex[2], obj.br.z)

    def collidesWithAABB(self, obj1, obj2):
        # print("wwwww", obj1.owner.getSingleComponentByType(MeshComponent).triangles)
        # print("wwwww", obj2.owner.getSingleComponentByType(MeshComponent).triangles)
        # print("ONE", obj1.tl, obj1.br)
        # print("TWO", obj2.tl, obj2.br)
        x = (obj1.br.x >= obj2.tl.x and obj1.tl.x<= obj2.br.x)
        y = (obj1.tl.y >= obj2.br.y and obj1.br.y<= obj2.tl.y)
        z = (obj1.tl.z >= obj2.br.z and obj1.br.z<= obj2.tl.z)
        return x and y and z


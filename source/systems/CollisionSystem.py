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
            if c.AABB:
                self.newAABB(c, e)

        for e0, c0 in self.eman.pairsForType(CollisionComponent):
            if c0.active:
                for e1, c1 in self.eman.pairsForType(CollisionComponent):
                    if e0 is not e1 and c1.active:
                        if c0.AABB and c1.AABB:
                            bCollides = self.collidesWithAABB(c0, c1)
                            #bCollides = self.collidesWithTriangles(c0, c1)
                        else:
                            # Triangle intersections, baby!
                            bCollides = self.collidesWithTriangles(c0, c1)
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
        x = (obj1.br.x >= obj2.tl.x and obj1.tl.x<= obj2.br.x)
        y = (obj1.tl.y >= obj2.br.y and obj1.br.y<= obj2.tl.y)
        z = (obj1.tl.z >= obj2.br.z and obj1.br.z<= obj2.tl.z)
        return x and y and z

    def collidesWithTriangles(self, obj1, obj2):
        raise Exception("Triangle - triangle collsions are not currently supported")
        tri0 = obj1.owner.getSingleComponentByType(MeshComponent).triangles
        tri1 = obj1.owner.getSingleComponentByType(MeshComponent).triangles

        for t0 in tri0:
            for t1 in tri1:
                if self.ttCollision(t0, t1):
                    return True
        return False

    def ttCollision(self, t0, t1):
        p00 = Vector.fromNP(t0[1])
        p01 = Vector.fromNP(t0[1])
        p02 = Vector.fromNP(t0[2])

        p10 = Vector.fromNP(t1[0])
        p11 = Vector.fromNP(t1[1])
        p12 = Vector.fromNP(t1[2])

        b0 = (p00 + p01 + p02) / 3
        b1 = (p10 + p11 + p12) / 3

        e10 = p10 - p11
        e11 = p10 - p12
        e12 = p11 - p12

        e00 = p00 - p01
        e01 = p00 - p02
        e02 = p01 - p02

        e0 = ((e00 + e01 + e02) / 3).length
        e1 = ((e10 + e11 + e12) / 3).length

        print((b0-b1).length)
        return (b0-b1).length > e0+e1

        # e10 = p10 - p11
        # e11 = p10 - p12
        # e12 = p11 - p12

        # n0 = (p01 - p00).cross(p02 - p00)
        # n1 = (p11 - p10).cross(p12 - p10)
        # #print("nnn", n0, n1)
        # t0 = (p10 - p00).dot(n0) / e10.dot(n0)
        # t1 = (p10 - p00).dot(n0) / e11.dot(n0)
        # t2 = (p10 - p00).dot(n0) / e12.dot(n0)

        # print("a", t0, t1, t2)
        return False
        # if abs(n0.cross(n1).length) < 0.005:
        #     # They are parallel













# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from util import Vector
from components import *
import time
import numpy as np
import math

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
                    if e0 is not e1 and c1.active and c1.type_ in c0.typeCollide:
                        if c0.AABB and c1.AABB:
                            bCollides = self.collidesWithAABB(c0, c1)
                            #bCollides = self.collidesWithTriangles(c0, c1)
                        else:
                            # Triangle intersections, baby!
                            bCollides = self.collidesWithTriangles(c0, c1)
                        if bCollides:
                            c0.collide(c1.type_)
                            #print(e0, "(type)", c0.type_, " collides with ", e1, "(type)", c1.type_, )
                            #print(int(round(time.time() * 1000)))


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
        #raise Exception("Triangle - triangle collsions are not currently supported")
        m0 = obj1.owner.getSingleComponentByType(MeshComponent)
        m1 = obj2.owner.getSingleComponentByType(MeshComponent)
        tri0 = m0.triangles
        tri1 = m1.triangles

        #print(tri0)
        for t0 in tri0:
            for t1 in tri1:
                if self.length(m0.bary - m1.bary) <= m0.radius + m1.radius:
                    if self.ttCollision(t0, t1):
                        return True
        return False

    # def lineIntersectLine(self, a0, b0, a1, b1):
    #     # Two lines defined by points (a0, a1) and (b0, b1)
    #     # raise Exception("This methos is untested")
    #     det = np.array([
    #                  [a0[0], a0[1], a0[2], 1],
    #                  [a1[0], a1[1], a1[2], 1],
    #                  [b0[0], b0[1], b0[2], 1],
    #                  [b1[0], b1[1], b1[2], 1]
    #                  ])
    #     x = np.linalg.det(det)
    #     print(x)
    #     return x == 0.

    def length(self, a):
        return np.sqrt(a.dot(a))

    def pointInTriangle(self, a, b, c, q):
        # This assumes the point p is coplanar with the triangle (a,b,c)
        u = b - a
        v = c - a
        w = q - a

        vcw = np.cross(v, w)
        vcu = np.cross(v, u)

        # Sign of r
        if vcw.dot(vcu) < 0:
            return False

        ucw = np.cross(u, w)
        ucv = np.cross(u, v)

        # Sign of t
        if ucw.dot(ucv) < 0:
            return False

        # Both r and t > 0.
        # Given this, as long as their sum <= 1, both are <= 1

        denom = np.sqrt(ucv.dot(ucv))
        r = np.sqrt(vcw.dot(vcw)) / denom
        t = np.sqrt(ucw.dot(ucw)) / denom

        return r + t <= 1

    def normalize(self, a):
        l = np.sqrt(a.dot(a))
        return a / l

    def ttCollision(self, t0, t1):
        # TODO: Make this use my vectors eventually

        # The verticies of triangle0
        A0 = np.array(t0[0])
        B0 = np.array(t0[1])
        C0 = np.array(t0[2])
        # The verticies of triangle1
        A1 = np.array(t1[0])
        B1 = np.array(t1[1])
        C1 = np.array(t1[2])

        # Edges of triangle0
        AB0 = A0 - B0
        AC0 = A0 - C0

        # Edges of triangle1
        AB1 = A1 - B1
        AC1 = A1 - C1
        BC1 = B1 - C1

        # Normal of triangle0
        n0 = np.cross(AB0, AC0)

        # t intersections for projection of triangle1 edges onto plane of triangle0
        t0 = A1.dot(n0) - A0.dot(n0) / AB1.dot(n0)
        # Point of intersection
        q0 = t0*AB1 + A1

        if self.pointInTriangle(A0, B0, C0, q0):
            return True

        t1 = A1.dot(n0) - A0.dot(n0) / AC1.dot(n0)
        q1 = t1*AC1 + A1
        if self.pointInTriangle(A0, B0, C0, q1):
            return True

        t2 = B1.dot(n0) - A0.dot(n0) / BC1.dot(n0)
        q2 = t2*BC1 + A1
        if self.pointInTriangle(A0, B0, C0, q2):
            return True

        # At this point, it is possible that the triangles are simply perfectly coplanar
        # # Do any of tri1's edges cross an edge of tri0?
        # a = self.lineIntersectLine(A0, B0, A1, B1)
        # b = self.lineIntersectLine(A0, B0, A1, C1)
        # c = self.lineIntersectLine(A0, B0, B1, C1)
        # d = self.lineIntersectLine(A0, C0, A1, B1)
        # e = self.lineIntersectLine(A0, C0, A1, C1)
        # f = self.lineIntersectLine(A0, C0, B1, C1)
        # g = self.lineIntersectLine(B0, C0, A1, B1)
        # h = self.lineIntersectLine(B0, C0, A1, C1)
        # i = self.lineIntersectLine(B0, C0, B1, C1)
        # return a or b or c or d or e or f or g or h or i
        # Do any of triangle1's verticies intersect triangle0?
        a = self.pointInTriangle(A0, B0, C0, A1)
        if a:
            return True
        b = self.pointInTriangle(A0, B0, C0, B1)
        if b:
            return True
        c = self.pointInTriangle(A0, B0, C0, C1)
        if c:
            return True
        # Do any of triangle0's verticies intersect triangle1?
        d = self.pointInTriangle(A1, B1, C1, A0)
        if d:
            return True
        e = self.pointInTriangle(A1, B1, C1, B0)
        if e:
            return True
        f = self.pointInTriangle(A1, B1, C1, C0)
        if f:
            return True

        return False

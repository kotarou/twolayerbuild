# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from util import *
from .MeshComponent import MeshComponent
from .SVAComponent import SVAComponent
from pyglet.gl import *

class CollisionComponent(Component):

    #def __init__(self, *args, **kwargs):
    def __init__(self, useAABB=False, AABB=None, collidable=True):
        super().__init__()
        self.tl = Vector(0,0,0)
        self.br = Vector(0,0,0)
        if AABB is not None and useAABB: # 'AABB' in kwargs.keys():
            self.tl, self.br = AABB #kwargs['AABB']
            self.setUp = True
            self.AABB = True
        else:
            self.setUp = False
            self.AABB = useAABB

        self.active = collidable
        # if 'collidable' in kwargs.keys():
        #     self.active = True
        # else:
        #     self.active = False

    def attach(self):
        if not self.setUp and self.AABB:
            # The AABB was not specified, so we will construct it
            for mesh in self.owner.getComponentsByType(MeshComponent):
                iterNum = mesh.vertexList[0][1]
                xList = mesh.vertexList[1][::int(iterNum)] # Every nth number
                self.tl.x = min(min(xList), self.tl.x)
                self.br.x = max(max(xList), self.br.x)
                yList = mesh.vertexList[1][1::int(iterNum)]
                self.tl.y = max(max(yList), self.tl.y)
                self.br.y = min(min(yList), self.br.y)
                if iterNum == 3:
                    zList = mesh.vertexList[1][1::int(iterNum)]
                    self.tl.z = max(max(zList), self.tl.z)
                    self.br.z = min(min(zList), self.br.z)
            #print(self.tl, self.br)
                #self.tl.x = min(self.tl.x, min(mesh)
        elif not self.setUp:
            # Don't use an AABB
            raise Exception("Collisions only work with AABB for now")

    def collidesWith(self, dSelf, dOther, rSelf, rOther, other):
        if self.AABB and other.AABB:
            if rSelf == Vector(0,0,0) and rOther == Vector(0,0,0):
                x = (self.br.x + dSelf.x >= other.tl.x + dOther.x and self.tl.x + dSelf.x <= other.br.x + dOther.x)
                y = (self.tl.y + dSelf.y >= other.br.y + dOther.y and self.br.y + dSelf.z <= other.tl.y + dOther.y)
                z = (self.tl.z + dSelf.z >= other.br.z + dOther.z and self.br.z + dSelf.z <= other.tl.z + dOther.z)
                return (x and y and z)
            else:
                # Rotations have occured and need handling
                # This is a super approximate system
                # Frankly, AABB sucks for rotation
                # WARNING YOU ARE USING AABB WITH A ROTATING OBJECT
                vSelf = [Vector(self.tl.x, self.tl.y, self.tl.z),
                         Vector(self.tl.x, self.br.y, self.tl.z),
                         Vector(self.br.x, self.tl.y, self.tl.z),
                         Vector(self.br.x, self.br.y, self.tl.z),
                         Vector(self.tl.x, self.tl.y, self.br.z),
                         Vector(self.tl.x, self.br.y, self.br.z),
                         Vector(self.br.x, self.tl.y, self.br.z),
                         Vector(self.br.x, self.br.y, self.br.z)]
                vOther = [Vector(other.tl.x, other.tl.y, other.tl.z),
                         Vector(other.tl.x, other.br.y, other.tl.z),
                         Vector(other.br.x, other.tl.y, other.tl.z),
                         Vector(other.br.x, other.br.y, other.tl.z),
                         Vector(other.tl.x, other.tl.y, other.br.z),
                         Vector(other.tl.x, other.br.y, other.br.z),
                         Vector(other.br.x, other.tl.y, other.br.z),
                         Vector(other.br.x, other.br.y, other.br.z)]
                for vec in vSelf:
                    vec.rotate(rSelf.x, rSelf.y, rSelf.z)
                for vec in vOther:
                    vec.rotate(rOther.x, rOther.y, rOther.z)
                sTL = Vector(
                             min(vSelf[0].x,vSelf[1].x,vSelf[2].x,vSelf[3].x,vSelf[4].x,vSelf[5].x,vSelf[6].x,vSelf[7].x),
                             max(vSelf[0].y,vSelf[1].y,vSelf[2].y,vSelf[3].y,vSelf[4].y,vSelf[5].y,vSelf[6].y,vSelf[7].y),
                             max(vSelf[0].z,vSelf[1].z,vSelf[2].z,vSelf[3].z,vSelf[4].z,vSelf[5].z,vSelf[6].z,vSelf[7].z)
                             )
                sBR = Vector(
                             max(vSelf[0].x,vSelf[1].x,vSelf[2].x,vSelf[3].x,vSelf[4].x,vSelf[5].x,vSelf[6].x,vSelf[7].x),
                             min(vSelf[0].y,vSelf[1].y,vSelf[2].y,vSelf[3].y,vSelf[4].y,vSelf[5].y,vSelf[6].y,vSelf[7].y),
                             min(vSelf[0].z,vSelf[1].z,vSelf[2].z,vSelf[3].z,vSelf[4].z,vSelf[5].z,vSelf[6].z,vSelf[7].z)
                             )
                oTL = Vector(
                             min(vOther[0].x,vOther[1].x,vOther[2].x,vOther[3].x,vOther[4].x,vOther[5].x,vOther[6].x,vOther[7].x),
                             max(vOther[0].y,vOther[1].y,vOther[2].y,vOther[3].y,vOther[4].y,vOther[5].y,vOther[6].y,vOther[7].y),
                             max(vOther[0].z,vOther[1].z,vOther[2].z,vOther[3].z,vOther[4].z,vOther[5].z,vOther[6].z,vOther[7].z)
                             )
                oBR = Vector(
                             max(vOther[0].x,vOther[1].x,vOther[2].x,vOther[3].x,vOther[4].x,vOther[5].x,vOther[6].x,vOther[7].x),
                             min(vOther[0].y,vOther[1].y,vOther[2].y,vOther[3].y,vOther[4].y,vOther[5].y,vOther[6].y,vOther[7].y),
                             min(vOther[0].z,vOther[1].z,vOther[2].z,vOther[3].z,vOther[4].z,vOther[5].z,vOther[6].z,vOther[7].z)
                             )
                x = (sBR.x + dSelf.x >= oTL.x + dOther.x and sTL.x + dSelf.x <= oBR.x + dOther.x)
                y = (sTL.y + dSelf.y >= oBR.y + dOther.y and sBR.y + dSelf.y <= oTL.y + dOther.y)
                z = (sTL.z + dSelf.z >= oBR.z + dOther.z and sBR.z + dSelf.z <= oTL.z + dOther.z)
                return (x and y and z)


        else:
            # Do this with the triangles
            # SUPER SLOW
            raise Exception("Collisions only work with AABB for now")








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
    def __init__(self, AABB=None, collidable=True):
        super().__init__()
        self.tl = Vector(0,0,0)
        self.br = Vector(0,0,0)
        if AABB is not None: # 'AABB' in kwargs.keys():
            self.tl, self.br = AABB #kwargs['AABB']
            self.setUp = True
        else:
            self.setUp = False

        self.active = collidable
        # if 'collidable' in kwargs.keys():
        #     self.active = True
        # else:
        #     self.active = False

    def attach(self):
        if not self.setUp:
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
        # If the owner has an SVA component, account for it
        for sva in self.owner.getComponentsByType(SVAComponent):
            self.tl += sva.S
            self.br += sva.S

    def collidesWith(self, dSelf, dOther, other):
        # print(self.br, self.tl)
        # print(other.br, other.tl)
        #print(d0, d1)
        x = (self.br.x + dSelf.x >= other.tl.x + dOther.x and self.tl.x + dSelf.x <= other.br.x + dOther.x)
        y = (self.tl.y + dSelf.y >= other.br.y + dOther.y and self.br.y + dSelf.z <= other.tl.y + dOther.y)
        z = (self.tl.z + dSelf.z >= other.br.z + dOther.z and self.br.z + dSelf.z <= other.tl.z + dOther.z)
        # x = (self.br.x >= other.tl.x and self.tl.x <= other.br.x )
        # y = (self.tl.y >= other.br.y and self.br.y <= other.tl.y )
        # z = (self.tl.z >= other.br.z and self.br.z <= other.tl.z )
        #print(x,y,z)
        return (x and y and z)







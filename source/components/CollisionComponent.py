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
    def __init__(self, type_, typeCollide, useAABB=False, AABB=None, collidable=True):
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
        self.type_ = type_
        self.typeCollide = typeCollide
        self.active = collidable
        # if 'collidable' in kwargs.keys():
        #     self.active = True
        # else:
        #     self.active = False

    def attach(self):
        if not self.setUp and self.AABB:
            # The AABB was not specified, so we will construct it
            for mesh in self.owner.getComponentsByType(MeshComponent):
                for triangle in mesh.triangles:
                    for vertex in triangle:
                        self.tl.x = min(vertex[0], self.tl.x)
                        self.tl.y = max(vertex[1], self.tl.y)
                        self.tl.z = max(vertex[2], self.tl.z)

                        self.br.x = max(vertex[0], self.br.x)
                        self.br.y = min(vertex[1], self.br.y)
                        self.br.z = min(vertex[2], self.br.z)

        elif not self.setUp:
            # Don't use an AABB
            self.triangles = True

        else:
            # Do this with the triangles
            # SUPER SLOW
            self.triangles = True

    def collide(self, type_):
        # Respond to collisions
        # if self.type_ == "limb" and type_ == "ground":
        pass









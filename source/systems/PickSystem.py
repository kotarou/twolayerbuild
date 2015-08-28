# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MeshComponent import MeshComponent
from components import SVAComponent
from pyglet.gl import *

class PickSystem(System):

    def __init__(self):
        super().__init__()

    def update(self, _):
        try:
            for e, mesh in self.eman.pairsForType(MeshComponent):
                glLoadIdentity()
                for sva in self.eman.componentByType(e, SVAComponent):
                    glTranslatef(sva.S.x,sva.S.y,sva.S.z)
                    glTranslatef(mesh.anchor.x,mesh.anchor.y,mesh.anchor.z)
                    glRotatef(sva.THETA.x,1,0,0)
                    glRotatef(sva.THETA.y,0,1,0)
                    glRotatef(sva.THETA.z,0,0,1)
                    glTranslatef(-mesh.anchor.x,-mesh.anchor.y,-mesh.anchor.z)
                self.fboDraw(mesh)
        except TypeError:
            raise Exception("PickSystem without any MeshComponents")

    def fboDraw(self, mesh):
        r, g, b = mesh.color
        vList = pyglet.graphics.vertex_list(
            mesh.numVert,
            mesh.vertexList,
            ('c3B', [r,g,b]*mesh.numVert)
                     )
        vList.draw(mesh.mode)

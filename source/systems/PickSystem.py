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

    def update (self, _):
        for e, sva in self.eman.pairsForType(SVAComponent):
            glTranslatef(sva.S.x,sva.S.y,sva.S.z)
        try:
            for e, mesh in self.eman.pairsForType(MeshComponent):
                #self.fboDraw(e.color, mesh)
                self.fboDraw(mesh)
        except TypeError:
            raise Exception("PickSystem without any MeshComponents")

    def fboDraw(self, mesh):
        r, g, b = mesh.color
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in mesh.indexList:
            glVertex3f(mesh.vertexList[ind[0]][0], mesh.vertexList[ind[0]][1], mesh.vertexList[ind[0]][2])
            glVertex3f(mesh.vertexList[ind[1]][0], mesh.vertexList[ind[1]][1], mesh.vertexList[ind[1]][2])
            glVertex3f(mesh.vertexList[ind[2]][0], mesh.vertexList[ind[2]][1], mesh.vertexList[ind[2]][2])
        glEnd()

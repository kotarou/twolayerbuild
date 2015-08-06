# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import System
from components.MeshComponent import MeshComponent
from pyglet.gl import *

class PickSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _): 
        for e, mesh in self.entity_manager.pairs_for_type(MeshComponent):
            self.fboDraw(e.color, mesh)

    def fboDraw(self, color, mesh):
        r, g, b = color
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in mesh.indexList:
            glVertex3f(mesh.vertexList[ind[0]][0], mesh.vertexList[ind[0]][1], mesh.vertexList[ind[0]][2])
            glVertex3f(mesh.vertexList[ind[1]][0], mesh.vertexList[ind[1]][1], mesh.vertexList[ind[1]][2])
            glVertex3f(mesh.vertexList[ind[2]][0], mesh.vertexList[ind[2]][1], mesh.vertexList[ind[2]][2])
        glEnd()
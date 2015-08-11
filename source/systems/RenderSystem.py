# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MeshComponent import MeshComponent
from pyglet.gl import *

class RenderSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, mesh in self.eman.pairsForType(MeshComponent):
            if mesh.textured:
                self.texRender(mesh)
            else:
                self.colorRender(mesh)

    def texRender(self, mesh):
        glEnable(GL_TEXTURE_2D)
        if mesh.colored:
            r, g, b = mesh.colorList
        else:
            r, g, b = (255, 255, 255)
        glColor3ub(r, g, b)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glBindTexture(GL_TEXTURE_2D, mesh.texture.id)
        glBegin(GL_TRIANGLES)
        for ind in mesh.indexList:
            glTexCoord2f(mesh.textureList[ind[0]][0],mesh.textureList[ind[0]][1])
            glVertex3f(mesh.vertexList[ind[0]][0], mesh.vertexList[ind[0]][1], mesh.vertexList[ind[0]][2])
            glTexCoord2f(mesh.textureList[ind[1]][0],mesh.textureList[ind[1]][1])
            glVertex3f(mesh.vertexList[ind[1]][0], mesh.vertexList[ind[1]][1], mesh.vertexList[ind[1]][2])
            glTexCoord2f(mesh.textureList[ind[2]][0],mesh.textureList[ind[2]][1])
            glVertex3f(mesh.vertexList[ind[2]][0], mesh.vertexList[ind[2]][1], mesh.vertexList[ind[2]][2])
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def colorRender(self, mesh):
        r, g, b = mesh.colorList
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in mesh.indexList:
            glVertex3f(mesh.vertexList[ind[0]][0], mesh.vertexList[ind[0]][1], mesh.vertexList[ind[0]][2])
            glVertex3f(mesh.vertexList[ind[1]][0], mesh.vertexList[ind[1]][1], mesh.vertexList[ind[1]][2])
            glVertex3f(mesh.vertexList[ind[2]][0], mesh.vertexList[ind[2]][1], mesh.vertexList[ind[2]][2])
        glEnd()

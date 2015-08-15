# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.MeshComponent import MeshComponent
from components import SVAComponent
from pyglet.gl import *

class RenderSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        glLoadIdentity()
        for e, mesh in self.eman.pairsForType(MeshComponent):
            glLoadIdentity()
            for sva in self.eman.componentByType(e, SVAComponent):
                glTranslatef(sva.S.x,sva.S.y,sva.S.z)
                glRotatef(sva.THETA.x,1,0,0)
                glRotatef(sva.THETA.y,0,1,0)
                glRotatef(sva.THETA.z,0,0,1)
            vList = pyglet.graphics.vertex_list(
                    mesh.numVert,
                    #('v2i', (5,10, 15,20, 25,30, 35,40, 45,50, 55,60 )),
                    #('c3B', (0,0,255, 0,255,0, 0,0,255, 0,255,0, 0,0,255, 0,255,0))
                    mesh.vertexList,
                    # TODO: Support normals
                    #mesh.normalList if mesh.normal else None,
                    mesh.colorList if mesh.colored else (mesh.textureList if mesh.textured else None)
                     )
            if mesh.textured:
                glEnable(GL_TEXTURE_2D)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
                glBindTexture(GL_TEXTURE_2D, mesh.texture.id)
            vList.draw(mesh.mode)
            if mesh.textured:
                glDisable(GL_TEXTURE_2D)

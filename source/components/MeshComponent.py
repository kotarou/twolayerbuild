# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from pyglet.gl import *
from ecs.models import Component

class MeshComponent(Component):
    #__slots__ = "vertexList", "indexList", "colored", "textured", "textureList", "colorList"
    #def __init__ (self, vertexList, indexList, texture=None, textureList=None, colorList=None, colored=False, textured=False):

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.colorList  = args[0].color
            self.vertexList = args[0].vertexList
            self.indexList  = args[0].indexList
            self.textureList= args[0].textureMap
            self.colored    = args[0].colored
            self.textured   = args[0].textured  
            self.texture    = args[0].texture  
        else:
            print(kwargs)
            self.vertexList = kwargs['vertexList']
            self.indexList  = kwargs['indexList']

            if 'textureList' in kwargs:
                self.textureList    = kwargs['textureList']
                self.texture        = kwargs['texture']
                self.textured       = True
            else:
                self.textured       = False

            if 'colorList' in kwargs:
                self.colorList    = kwargs['colorList']
                self.colored       = True
            else:
                self.colored       = False
            
            #if 'textureList' not in kwargs and 'textured' in kwargs:
            #   raise Exception("Textured object without textureList")
            #if 'colorList' not in kwargs and 'colored' in kwargs:
            #    raise Exception("Colored object without colorList")
            #if not self.colored and not self.textured:
            #    raise Exception("This object cannot be neither colored or textured")

    def draw(self):
        if self.textured:
            glEnable(GL_TEXTURE_2D)
            if self.colored:
                r, g, b = self.colorList
            else:
                r, g, b = (255, 255, 255)
            glColor3ub(r, g, b)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glBindTexture(GL_TEXTURE_2D, self.texture.id)
            glBegin(GL_TRIANGLES)
            for ind in self.indexList:
                glTexCoord2f(self.textureList[ind[0]][0],self.textureList[ind[0]][1])
                glVertex3f(self.vertexList[ind[0]][0], self.vertexList[ind[0]][1], self.vertexList[ind[0]][2])
                glTexCoord2f(self.textureList[ind[1]][0],self.textureList[ind[1]][1])
                glVertex3f(self.vertexList[ind[1]][0], self.vertexList[ind[1]][1], self.vertexList[ind[1]][2])
                glTexCoord2f(self.textureList[ind[2]][0],self.textureList[ind[2]][1])
                glVertex3f(self.vertexList[ind[2]][0], self.vertexList[ind[2]][1], self.vertexList[ind[2]][2])
            glEnd()
            glDisable(GL_TEXTURE_2D)
        # If you are textured, you have no color
        # If you are both, tecture overrides color
        # This is temporary, and will change
        else:
            r, g, b = self.colorList
            glColor3ub(r, g, b)
            glBegin(GL_TRIANGLES)
            for ind in self.indexList:
                glVertex3f(self.vertexList[ind[0]][0], self.vertexList[ind[0]][1], self.vertexList[ind[0]][2])
                glVertex3f(self.vertexList[ind[1]][0], self.vertexList[ind[1]][1], self.vertexList[ind[1]][2])
                glVertex3f(self.vertexList[ind[2]][0], self.vertexList[ind[2]][1], self.vertexList[ind[2]][2])
            glEnd()

    def fboDraw(self, color):
        r, g, b = color
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in self.indexList:
            glVertex3f(self.vertexList[ind[0]][0], self.vertexList[ind[0]][1], self.vertexList[ind[0]][2])
            glVertex3f(self.vertexList[ind[1]][0], self.vertexList[ind[1]][1], self.vertexList[ind[1]][2])
            glVertex3f(self.vertexList[ind[2]][0], self.vertexList[ind[2]][1], self.vertexList[ind[2]][2])
        glEnd()
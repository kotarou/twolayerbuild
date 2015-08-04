# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
import numpy as np
#import pyglet 
import pyglet.graphics as pg
from pyglet.gl import *
import time
import ctypes

current_milli_time = lambda: int(round(time.time() * 1000))

class Element(object):
    """ 
        An object
    """

    def __init__(self, handle):
        """
        glColor3f handle
        """
        # An object should have a unique handle
        self.handle = handle

    def draw(self):
        pass
    
    def fobDraw(self):
        pass

    def update(self):
        pass

class MouseInteractable(Element):

    hoverTime = 0.5

    def onClick(self, x, y):
        pass

    def onHover(self):
        pass

class KeyInteractable(Element):

    def onKey(key, modifier):
        pass

class VertexRendered(Element):

    def draw(self):
        if self.textured:
            glEnable(GL_TEXTURE_2D)
            if self.colored:
                r, g, b = self.color
            else:
                r, g, b = (255, 255, 255)
            glColor3ub(r, g, b)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glBindTexture(GL_TEXTURE_2D, self.texture.id)
            glBegin(GL_TRIANGLES)
            for ind in self.indicies:
                glTexCoord2f(self.textureMap[ind[0]][0],self.textureMap[ind[0]][1])
                glVertex3f(self.verticies[ind[0]][0], self.verticies[ind[0]][1], self.verticies[ind[0]][2])
                glTexCoord2f(self.textureMap[ind[1]][0],self.textureMap[ind[1]][1])
                glVertex3f(self.verticies[ind[1]][0], self.verticies[ind[1]][1], self.verticies[ind[1]][2])
                glTexCoord2f(self.textureMap[ind[2]][0],self.textureMap[ind[2]][1])
                glVertex3f(self.verticies[ind[2]][0], self.verticies[ind[2]][1], self.verticies[ind[2]][2])
            glEnd()
            glDisable(GL_TEXTURE_2D)
        # If you are textured, you have no color
        # If you are both, tecture overrides color
        # This is temporary, and will change
        else:
            r, g, b = self.color
            glColor3ub(r, g, b)
            glBegin(GL_TRIANGLES)
            for ind in self.indicies:
                glVertex3f(self.verticies[ind[0]][0], self.verticies[ind[0]][1], self.verticies[ind[0]][2])
                glVertex3f(self.verticies[ind[1]][0], self.verticies[ind[1]][1], self.verticies[ind[1]][2])
                glVertex3f(self.verticies[ind[2]][0], self.verticies[ind[2]][1], self.verticies[ind[2]][2])
            glEnd()

    def fboDraw(self):
        r, g, b = self.handle
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in self.indicies:
            glVertex3f(self.verticies[ind[0]][0], self.verticies[ind[0]][1], self.verticies[ind[0]][2])
            glVertex3f(self.verticies[ind[1]][0], self.verticies[ind[1]][1], self.verticies[ind[1]][2])
            glVertex3f(self.verticies[ind[2]][0], self.verticies[ind[2]][1], self.verticies[ind[2]][2])
        glEnd()

class tempClass(MouseInteractable, VertexRendered):
    #def __init__(self, handle, color, verticies, indicies):
    def __init__(self, *args, **kwargs):
        self.colored = True
        self.textured = False
        if len(args) == 4:
            self.handle     = args[0]
            self.color      = args[1]
            self.verticies  = args[2]
            self.indicies   = args[3]
        if len(args) == 2:
            self.handle     = args[0]
            self.color      = args[1].color
            self.verticies  = args[1].vertexList
            self.indicies   = args[1].indexList

    def onClick(self, x, y):
        print("Temp class!")

    def update(self):
        x = 3

class tempClass2(MouseInteractable, VertexRendered):
    #def __init__(self, handle, color, verticies, indicies):
    def __init__(self, *args, **kwargs):
        if len(args) == 4:
            self.handle     = args[0]
            self.color      = args[1]
            self.verticies  = args[2]
            self.indicies   = args[3]
        if len(args) == 2:
            self.handle     = args[0]
            self.verticies  = args[1].vertexList
            self.indicies   = args[1].indexList
            self.colored    = args[1].colored
            self.textured   = args[1].textured
            if self.colored:
                self.color      = args[1].color
            if self.textured:
                self.texture    = args[1].texture
            self.textureMap = args[1].textureMap

        # Sanity check. Are we textured or colored or both?
        if not self.colored and not self.textured:
            raise Exception("An entty cannot be neither colored or textured")


    def onClick(self, x, y):
        print("Temp class!")

    def update(self):
        x = 3


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

    def drawInterior(self, color):
        r, g, b = color
        glColor3ub(r, g, b)
        glBegin(GL_TRIANGLES)
        for ind in self.indicies:
            glVertex3f(self.verticies[ind[0]][0], self.verticies[ind[0]][1], self.verticies[ind[0]][2])
            glVertex3f(self.verticies[ind[1]][0], self.verticies[ind[1]][1], self.verticies[ind[1]][2])
            glVertex3f(self.verticies[ind[2]][0], self.verticies[ind[2]][1], self.verticies[ind[2]][2])
        glEnd()

    def draw(self):
        self.drawInterior(self.color)

    def fboDraw(self):
        self.drawInterior(self.handle)

class tempClass(MouseInteractable, VertexRendered):
    #def __init__(self, handle, color, verticies, indicies):
    def __init__(self, *args, **kwargs):
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



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


    # def __cmp__(self, other):
    #     # This defines the order of objects in the depth buffer
    #     return cmp(self.depth, other.depth)

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
    def __init__(self, handle, color, verticies, indicies):
        self.handle     = handle
        self.color      = color
        self.verticies  = verticies
        self.indicies   = indicies

    def onClick(self, x, y):
        print("Temp class!")

    def update(self):
        x = 3



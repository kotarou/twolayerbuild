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

from ecs.models import Component, System, Entity
from ecs.managers import EntityManager, SystemManager
from ecs.exceptions import NonexistentComponentTypeForEntity

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

class MeshComponent(Component):
    #__slots__ = "vertexList", "indexList", "colored", "textured", "textureList", "colorList"
    def __init__ (self, vertexList, indexList, texture=None, textureList=None, colorList=None, colored=False, textured=False):
        """
        """
        self.vertexList     = vertexList
        self.indexList      = indexList
        
        if textureList == None and textured:
            raise Exception("Textured object without textureList")
        self.textureList    = textureList
        self.texture        = texture

        if colorList == None and colored:
            raise Exception("Colored object without colorList")
        self.colorList      = colorList

        self.colored        = colored
        self.textured       = textured
        if not self.colored and not self.textured:
            raise Exception("This object cannot be neither colored or textured")
    
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

class RenderSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _): 
        for e, mesh in self.entity_manager.pairs_for_type(MeshComponent):
            mesh.draw()

class PickSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _): 
        for e, mesh in self.entity_manager.pairs_for_type(MeshComponent):
            mesh.fboDraw(e.color)

class tempClass3(Entity):
    def __init__(self, color, eman):
        self.eman = eman
        self.color = color
        super().__init__(int(color.r*255*255+color.g*255+color.b))

class MouseClickComponent(Component):

    def __init__(self, string="I can be clicked on!"):
        self.response = string

    def onClick(self, x, y):
        print(self.response)


















class MouseInteractable(Element):

    hoverTime = 0.5

    def onClick(self, x, y):
        print("hello!")

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

    def update(self):
        x = 3


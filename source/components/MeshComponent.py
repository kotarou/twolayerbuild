# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from pyglet.gl import *
from util import Square
from util import Vector
import numpy as np

class MeshComponent(Component):
    #__slots__ = "vertexList", "indexList", "colored", "textured", "textureList", "colorList"
    #def __init__ (self, vertexList, indexList, texture=None, textureList=None, colorList=None, colored=False, textured=False):

    def __init__(self, *args, **kwargs):
        super().__init__()

        if 'shape' in kwargs.keys():
            self.mode = kwargs['shape'].mode
            self.indexList = kwargs['shape'].indexList
            self.vertexList = kwargs['shape'].vertexList
            self.colorList = kwargs['shape'].colorList
            self.textureList = kwargs['shape'].textureList
            self.texture = kwargs['shape'].texture
            self.colored = kwargs['shape'].colored
            self.textured = kwargs['shape'].textured
            self.numVert = len(self.indexList)

        vertexByThrees = [self.vertexList[1][i:i+3] for i in range(0, len(self.vertexList[1]), 3)]
        vertexByThrees = [list(e) for e in vertexByThrees]
        # This will be used for checking collisions and the such
        # As such, they will only correspond to the vertexList when the object has had no applied transformations
        self.triangles = [vertexByThrees[i:i+3] for i in range(0, len(vertexByThrees), 3)]
        self.updateBary()

    def updateBary(self):
        x = np.array([0,0,0])
        l1 = 0
        for tri in self.triangles:
            A1 = np.array(tri[0])
            B1 = np.array(tri[1])
            C1 = np.array(tri[2])
            x += (A1 + B1 + C1)
        x /= len(self.triangles*3)
        for tri in self.triangles:
            A1 = np.array(tri[0])
            B1 = np.array(tri[1])
            C1 = np.array(tri[2])
            l1 = max(self.length(A1 - x), self.length(B1 - x), self.length(C1 - x), l1)
        self.bary   = x
        self.radius = l1


    #TODO: Move this to util

    def length(self, a):
        return np.sqrt(a.dot(a))

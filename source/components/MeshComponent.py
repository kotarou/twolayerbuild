# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from pyglet.gl import *
from util import Square
from util import Vector

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

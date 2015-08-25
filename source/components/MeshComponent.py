# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from pyglet.gl import *
from util import Square

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
            self.colored = kwargs['shape'].colored
            self.textured = kwargs['shape'].textured
            print(self.colored)
            self.numVert = len(self.indexList)

        else:
            self.mode = args[0]
            vFormat, vert = args[1]

            if 'index' in kwargs.keys():
                self.index = True
                self.indexList = kwargs['index']
            else:
                self.index = False
                self.indexList = None

            # Using the existing vertexList and the index list, genetate the final list
            #tuple([(element.foo, element.bar) for element in alist])
            # Note this assumes an x,y,z for all verticies
            if self.index:
                self.vertexList = (vFormat, list(sum([(vert[3*i], vert[(3*i)+1], vert[(3*i)+2]) for i in self.indexList], ())))
            else:
                self.vertexList = (vFormat, vert)
            # We can automatically compute the number of triangles/quads/etc so do not require it as a parameter
            if self.index:
                self.numVert = len(self.indexList)
            else:
                # We need to infer this from the verticies themselves
                self.numVert = len(vert) / int(vFormat[1])

            self.numVert = int(self.numVert)
            print(self.numVert)
            # Optional parameters
            if 'normal' in kwargs.keys():
                self.normal = True
                self.normalList = kwargs['normal']
            else:
                self.normal = False
                self.normalList = None

            if 'texture' in kwargs.keys():
                self.textured = True
                tFormat, tex = kwargs['textureList']
                if self.index:
                    # ONLY SUPPORTS 2D
                    self.textureList = (tFormat, list(sum([(tex[2*i], tex[(2*i)+1]) for i in self.indexList], ())))
                else:
                    self.textureList = (tFormat, tex)
                self.texture = kwargs['texture']
            else:
                self.textured = False
                self.textureList = None

            if 'color' in kwargs.keys():
                self.colored = True
                cFormat, col = kwargs['color']
                if self.index:
                    self.colorList = (cFormat, list(sum([(col[3*i], col[(3*i)+1], col[(3*i)+2]) for i in self.indexList], ())))
                else:
                    self.colorList = (cFormat, col)
            else:
                if self.textured:
                    self.colored = False
                    self.colorList = None
                else:
                    self.colored = True
                    self.colorList = ('c3B', [255,255,255] * self.numVert)

        # if len(args) == 1:
        #     self.colorList  = args[0].color
        #     self.vertexList = args[0].vertexList
        #     self.indexList  = args[0].indexList
        #     self.textureList= args[0].textureMap
        #     self.colored    = args[0].colored
        #     self.textured   = args[0].textured
        #     self.texture    = args[0].texture
        # else:
        #     print(kwargs)
        #     self.vertexList = kwargs['vertexList']
        #     self.indexList  = kwargs['indexList']

        #     if 'textureList' in kwargs:
        #         self.textureList    = kwargs['textureList']
        #         self.texture        = kwargs['texture']
        #         self.textured       = True
        #     else:
        #         self.textured       = False

        #     if 'colorList' in kwargs:
        #         self.colorList    = kwargs['colorList']
        #         self.colored       = True
        #     else:
        #         self.colored       = False



# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component

class MeshComponent(Component):
    #__slots__ = "vertexList", "indexList", "colored", "textured", "textureList", "colorList"
    #def __init__ (self, vertexList, indexList, texture=None, textureList=None, colorList=None, colored=False, textured=False):

    def __init__(self, *args, **kwargs):
        super().__init__()
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


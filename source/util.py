# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from color import *
import numpy as np
import math
from pyglet.gl import *

TOPLEFT = 0
BOTTOMRIGHT = 1
CENTER = 2

class Vector(object):

    def __init__(self, x=0, y=0, z=0, w=1):
        self.array = np.array([x, y, z, w])

    def __getitem__(self, index):
        return self.array[index]

    @property
    def xyz(self):
        return (self.array[0], self.array[1], self.array[2])

    @property
    def x(self):
        return self.array[0]

    @x.setter
    def x(self, v):
        self.array[0] = v

    @property
    def y(self):
        return self.array[1]

    @y.setter
    def y(self, v):
        self.array[1] = v

    @property
    def z(self):
        return self.array[2]

    @z.setter
    def z(self, v):
        self.array[2] = v

    @property
    def w(self):
        return self.array[3]

    @w.setter
    def w(self, v):
        self.array[3] = v

    def angleWrap(self):
        if self.x > 360:
            self.x -= 360
        if self.x < -360:
            self.x += 360
        if self.y > 360:
            self.y -= 360
        if self.y < -360:
            self.y += 360
        if self.z > 360:
            self.z -= 360
        if self.z < -360:
            self.z += 360
        # Its an angle!
        if self.w == 1:
            self.w = 0

    def fromNP(npArray, rot=False):
        if len(npArray) is 4:
            return Vector(npArray[0],npArray[1],npArray[2],npArray[3])
        elif len(npArray) is 3:
            print(npArray[2])
            return Vector(npArray[0],npArray[1],npArray[2],0 if rot else 1)

    def __add__(self, other):
        if type(other) == Vector:
            # We do not change w or make it a value other than 1/0
            return Vector(self.array[0] + other.array[0], self.array[1] + other.array[1], self.array[2] + other.array[2], self.array[3])
        else:
            return Vector.fromNP(self.array + other)

    def __sub__(self, other):
        if type(other) == Vector:
            # We do not change w or make it a value other than 1/0
            return Vector(self.array[0] - other.array[0], self.array[1] - other.array[1], self.array[2] - other.array[2], self.array[3])
        else:
            return Vector.fromNP(self.array - other)

    def __mul__(self, other):
        if type(other) == Vector:
            # We do not change w or make it a value other than 1/0
            return Vector(self.array[0] * other.array[0], self.array[1] * other.array[1], self.array[2] * other.array[2], self.array[3])
        else:
            return Vector.fromNP(self.array * other)

    def __truediv__(self, other):
        if type(other) == Vector:
            # We do not change w or make it a value other than 1/0
            return Vector(self.array[0] / other.array[0], self.array[1] / other.array[1], self.array[2] / other.array[2], self.array[3])
        else:
            return Vector.fromNP(self.array / other)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.array)
    #TODO: Interface with numpy

    def dot(self, other):
        raise Exception("Vector dot method not tested.")
        return Vector.fromNP(self.array.dot(other.array))

    def rotate(self, rx, ry, rz):
        """
            Simple rotations: rotate rx degrees around the x axis, ry around y...
        """
        rx = math.radians(rx)
        ry = math.radians(ry)
        rz = math.radians(rz)
        rxx = np.array([
                     [1,0,0,0],
                     [0,math.cos(rx),math.sin(rx),0],
                     [0,-math.sin(rx),-math.cos(rx),0],
                     [0,0,0,1]
                     ])
        ryy = np.array([
                     [math.cos(ry),0,-math.sin(ry),0],
                     [0,1,0,0],
                     [math.sin(ry),0,math.cos(ry),0],
                     [0,0,0,1]
                     ])
        rzz = np.array([
                     [math.cos(rz),math.sin(rz),0,0],
                     [-math.sin(rz),math.cos(rz),0,0],
                     [0,0,1,0],
                     [0,0,0,1]
                     ])
        self.array = self.array.dot(rxx).dot(ryy).dot(rzz)

class Square(object):

    #__slots__ = ('tl', 'tr', 'bl', 'br', 'vertexList', 'indexList')
    # NOTE: The anchor also defines the center of rotation.
    def __init__(self,
                 sideLength=50, position=Vector(0,0,0), anchor=TOPLEFT,
                 colorList=None, texture=None):
        self.tl = self.tr = self.br = self.bl = Vector(0,0,0)
        if anchor == TOPLEFT:
            self.tl = position
            self.tr = position + Vector(sideLength,0,0)
            self.bl = position + Vector(0, -sideLength, 0)
            self.br = position + Vector(sideLength, -sideLength, 0)
        elif anchor == BOTTOMRIGHT:
            self.tl = position + Vector(-sideLength, sideLength, 0)
            self.tr = position + Vector(0,sideLength,0)
            self.bl = position + Vector(-sideLength,0, 0)
            self.br = position
        elif anchor == CENTER:
            self.tl = position + Vector(-sideLength/2, sideLength/2, 0)
            self.tr = position + Vector(sideLength/2, sideLength/2, 0)
            self.bl = position + Vector(-sideLength/2, -sideLength/2, 0)
            self.br = position + Vector(sideLength/2, -sideLength/2, 0)
        else:
            raise Exception("Unsupported square anchor")
            #  ('v3f',

        [*v] = self.bl.xyz+self.br.xyz+self.tr.xyz+self.bl.xyz+self.tr.xyz+self.tl.xyz

        self.vertexList = ('v3f', tuple(v))
        self.indexList = [0, 1, 2, 0, 2, 3]
        print()
        if colorList is None:
            self.colored = False
            self.colorList = None
        else:
            self.colored = True
            # The color list can be a tad complex.
            # A user may be putting values in one of three formats:
            print(colorList)
            # 1) A single color for the entire square
            if len(colorList) == 1 and len(colorList[0]) == 3:
                self.colorList = [colorList[0] * 6]
            # 2) A color for each of the 4 corners
            elif len(colorList) == 4:
                self.colorList = [colorList[0],colorList[1],colorList[2],colorList[3]]  # colorList[0],colorList[2],colorList[3]]
            elif len(colorList[0]) == 12:
                self.colorList = [colorList[0][0],colorList[0][1],colorList[0][2],
                                  colorList[0][3],colorList[0][4],colorList[0][5],
                                  colorList[0][6],colorList[0][7],colorList[0][8],
                                  colorList[0][0],colorList[0][1],colorList[0][2],
                                  colorList[0][6],colorList[0][7],colorList[0][8],
                                  colorList[0][9],colorList[0][10],colorList[0][11]]
            # 3) A color for each vertex
            elif len(colorList) == 6:
                self.colorList = colorList
            elif len(colorList[0]) == 18:
                self.colorList = [colorList[0][0],colorList[0][1],colorList[0][2],
                                  colorList[0][3],colorList[0][4],colorList[0][5],
                                  colorList[0][6],colorList[0][7],colorList[0][8],
                                  colorList[0][9],colorList[0][10],colorList[0][11],
                                  colorList[0][12],colorList[0][13],colorList[0][14],
                                  colorList[0][15],colorList[0][16],colorList[0][17]]
            else:
                raise Exception("Unsupported number of colors")
            try:
                self.colorList = ('c3B', sum(self.colorList, ()))
            except:
                self.colorList = ('c3B', tuple(self.colorList))

        if texture is None:
            self.textured = False
            self.textureList = None
            self.texture = None
        else:
            self.textured = True
            self.texture = texture
            # This assumes that the texture is 2D and fits into the UV [0,1] range nicely
            self.textureList = ('t2i', (0,0, 0,1, 1,1, 0,0, 1,1, 1,0))

        if not self.textured and not self.colored:
            raise Exception("Cannot have an uncolored and untextured sqwuare")

        self.mode = GL_TRIANGLES


if __name__ == "__main__":
    a = Square(50, Vector(0, 0, 0), TOPLEFT)
    print(a)

    # p = Vector(1,2,3)
    # r = Vector(1,1,1)
    # p.rotate(0, 0, 180)
    # print(p)
    # p += 2
    # print(p)
    # q = p * 3
    # print(q)

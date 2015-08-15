# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from color import *
import numpy as np
import math
class Shape(object):
    def __init__(self, color=None, texture=None):
        self.textured=False
        if texture != None:
            self.textured = True
            self.texture = texture
        self.colored = False
        if color != None:
            self.color = color
            self.colored = True

        if not self.colored and not self.textured:
            raise Exception("Squares must have a color or texture")

class Square(Shape):

    def __init__(self, center, side, color=None, texture=None):
        self.vertexList = [	[center[0]-side/2, center[1]-side/2, center[2]],
                            [center[0]-side/2, (center[1]+side/2), center[2]],
                            [(center[0]+side/2), (center[1]+side/2), center[2]],
                            [(center[0]+side/2), center[1]-side/2, center[2]]]
        self.indexList 	= [[0,1,2], [2,3,0]]
        self.textureMap = [[0,0], [0, 1], [1,1], [1, 0]]
        super().__init__(color, texture)


class Triangle(Shape):

    def __init__(self, center, side, color=None, texture=None):
        self.vertexList = [	[center[0]-side/2, center[1]-side/2, center[2]],
                            [center[0]-side/2, (center[1]+side/2), center[2]],
                            [(center[0]+side/2), (center[1]+side/2), center[2]]]
        self.indexList 	= [[0,1,2]]
        self.textureMap = [[0,0], [0, 1], [1,1]]
        super().__init__(color, texture)

class Vector(object):

    def __init__(self, x=0, y=0, z=0, w=1):
        self.array = np.array([x, y, z, w])

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

if __name__ == "__main__":
    p = Vector(1,2,3)
    r = Vector(1,1,1)
    p.rotate(0, 0, 180)
    print(p)
    p += 2
    print(p)
    q = p * 3
    print(q)

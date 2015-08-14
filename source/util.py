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

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1
    # def __new__(cls, x, y, z):
    #     return super(Vector, cls).__new__(cls, x, y, z)

    def rotate(self, rx, ry, rz):
        j = np.array([self.x, self.y, self.z, self.w])
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
                     [math.cos(rx),0,-math.sin(rx),0],
                     [0,1,0,0],
                     [math.sin(rx),0,math.cos(rx),0],
                     [0,0,0,1]
                     ])
        rzz = np.array([
                     [math.cos(rz),math.sin(rz),0,0],
                     [-math.sin(rz),math.cos(rz),0,0],
                     [0,0,1,0],
                     [0,0,0,1]
                     ])
        j = j.dot(rxx).dot(ryy).dot(rzz)
        self.x = j[0]
        self.y = j[1]
        self.z = j[2]


    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __iadd__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __isub__(self, other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Vector: " + str(self.x) + ", " + str(self.y) + ", " + str(self.z)
    #TODO: Interface with numpy

if __name__ == "__main__":
    p = Vector(1,2,3)
    r = Vector(1,1,1)
    p.rotate(0, 0, 270)
    print(p)

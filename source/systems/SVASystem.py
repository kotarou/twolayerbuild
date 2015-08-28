# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.SVAComponent import SVAComponent
from components.CollisionComponent import CollisionComponent
from components.MeshComponent import MeshComponent
import math

# TODO, get these from main game instead of hard coding
WINDOW_WIDTH            = 800
WINDOW_HEIGHT           = 600

class SVASystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, sva in self.eman.pairsForType(SVAComponent):
            # If there are any attached meshes, update the triangles inside it
            # TODO: Implement rotations

            dS = sva.S - sva.oldS
            #print("dS", dS)

            if sva.A.length > 0 or sva.V.length > 0 or dS.length > 0 or sva.OMEGA.length > 0 or sva.ALPHA.length > 0:
                for mesh in e.getComponentsByType(MeshComponent):
                    mesh.anchor += dS
                    print(mesh.anchor)
                    for triangle in mesh.triangles:
                        h = mesh.anchor[0]
                        k = mesh.anchor[1]
                        triangle[0][0] += dS[0]
                        triangle[0][1] += dS[1]
                        triangle[0][2] += dS[2]
                        triangle[1][0] += dS[0]
                        triangle[1][1] += dS[1]
                        triangle[1][2] += dS[2]
                        triangle[2][0] += dS[0]
                        triangle[2][1] += dS[1]
                        triangle[2][2] += dS[2]
                        print(triangle)
                        if sva.OMEGA.length > 0 or sva.ALPHA.length > 0:
                            x = triangle[0][0]
                            y = triangle[0][1]
                            triangle[0][0] = (x - h)*math.cos(sva.THETA[2]) - (y - k)*math.sin(sva.THETA[2]) + h
                            triangle[0][1] = (x - h)*math.sin(sva.THETA[2]) + (y - k)*math.cos(sva.THETA[2]) + k

                            x = triangle[1][0]
                            y = triangle[1][1]
                            triangle[1][0] = (x - h)*math.cos(sva.THETA[2]) - (y - k)*math.sin(sva.THETA[2]) + h
                            triangle[1][1] = (x - h)*math.sin(sva.THETA[2]) + (y - k)*math.cos(sva.THETA[2]) + k

                            x = triangle[2][0]
                            y = triangle[2][1]
                            triangle[2][0] = (x - h)*math.cos(sva.THETA[2]) - (y - k)*math.sin(sva.THETA[2]) + h
                            triangle[2][1] = (x - h)*math.sin(sva.THETA[2]) + (y - k)*math.cos(sva.THETA[2]) + k
                        print(triangle)

                        mesh.updateBary()
                    #print("bbbbbbbbbb", triangle)

            # Linear
            sva.oldS = sva.S

            sva.V += sva.A
            sva.S += sva.V

            # Rotational
            sva.OMEGA += sva.ALPHA
            sva.THETA += sva.OMEGA

            sva.THETA.angleWrap()

            if sva.bounded:
                # TODO: Make these respect the camera as well
                # TODO: Make these work with Z components
                if sva.S.x < -WINDOW_WIDTH / 2:
                    sva.S.x = -WINDOW_WIDTH / 2 + 20
                if sva.S.x > WINDOW_WIDTH / 2:
                    sva.S.x = WINDOW_WIDTH / 2  - 20
                if sva.S.y < -WINDOW_HEIGHT / 2:
                    sva.S.y = -WINDOW_HEIGHT / 2  + 20
                if sva.S.y > WINDOW_HEIGHT / 2:
                    sva.S.y = WINDOW_HEIGHT / 2  - 20

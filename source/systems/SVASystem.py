# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import System
from components.SVAComponent import SVAComponent
from components.CollisionComponent import CollisionComponent

# TODO, get these from main game instead of hard coding
WINDOW_WIDTH            = 800
WINDOW_HEIGHT           = 600

class SVASystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _):
        for e, sva in self.eman.pairsForType(SVAComponent):
            # Linear
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


            # TODO implement angular shite


# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from ecs.models import System
from components.MeshComponent import MeshComponent

class RenderSystem(System):

    def __init__(self):
        super().__init__()

    def update (self, _): 
        for e, mesh in self.entity_manager.pairs_for_type(MeshComponent):
            mesh.draw()
# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from color import *

class Square(object):

	def __init__(self, center, side, color=None, texture=None):
		self.vertexList = [	[center[0]-side/2, center[1]-side/2, center[2]],  
							[center[0]-side/2, (center[1]+side/2), center[2]],   
							[(center[0]+side/2), (center[1]+side/2), center[2]], 
							[(center[0]+side/2), center[1]-side/2, center[2]]]
		self.indexList 	= [[0,1,2], [2,3,0]]
		self.textured=False
		if texture != None:
			self.textured = True
			self.texture = texture
			self.textureMap = [[0,0], [0, 1], [1,1], [1, 0]]
		self.colored = False
		if color != None:
			self.color = color
			self.colored = True

		if not self.colored and not self.textured:
			raise Exception("Squares must have a color or texture")
		# if len(color) == 1:
		# 	self.colorList = [color * 4]
		# elif len(color) == 4:
		# 	self.colorList = color
		# else:
		# 	raise Exception("num colors not 1 or 4. Got: ", len(color))

class Triangle(object):

	def __init__(self, center, side, color):
		self.vertexList = [	[center[0]-side/2, center[1]-side/2, center[2]],  
							[center[0]-side/2, (center[1]+side/2), center[2]],   
							[(center[0]+side/2), (center[1]+side/2), center[2]]]
		self.indexList 	= [[0,1,2]]
		self.color = color    

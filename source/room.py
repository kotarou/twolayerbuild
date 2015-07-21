import pyglet

class Room:

	tileList = ""

	def __init__(self, sizeX, sizeY, inX, inY):
		for i in range(inX, (inX+sizeX)):
			for j in range(inY, (inY+sizeY)):
				if i==inX or i==(inX+sizeX) or j==inY or j==(inY+sizeY):	
					self.tileList += Wall.init("identifier", i, j)
				else:
					self.tileList += Floor.init("identifier", i, j)
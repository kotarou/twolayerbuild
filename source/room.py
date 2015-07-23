import pyglet, tile

class Room:

	tileList = ""
	tileDict = {'floor': tile.Floor, 'wall': tile.Wall, 'corridor': tile.Corridor}

	def __init__(self, roomType, xStart, yStart, xEnd, yEnd):
		for i in range(xStart, xEnd):
			for j in range(yStart, yEnd):
				tileList += tileDict[roomType].init(i,j)
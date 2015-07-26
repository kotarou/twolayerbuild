import pyglet, tile

class Room:

	tileDict = {}
	roomDict = {}

	#defines the rooms used in the current map
	#takes a keyIn array which declares the reference for the tile type at i
	#takes a tileTypeIn 2d array which has:
	#	[n][], where n is the tile reference at i - this should always be in line with key. 
	#	[this could be potentially used to derive a key value, if we don't care that key values are from 0 to numTileTypes rather than explicit predefined values]
	#	AND
	#	[][n], where 0-n define the tile's properties.

	def __init__(self, keyIn, tileTypeIn):
		for i in range(0,keyIn.len()):
			tileDict[keyIn[i]] = Tile.type(str(tileTypeIn[i][0]), (), {'navigatable': tileTypeIn[i][1]})

	#creates each of the rooms
	#adds the room to the roomDict

	def createRoom(self, keyIn, nameIn, xStart, yStart, xEnd, yEnd):
		for i in range(xStart, xEnd):
			for j in range(yStart, yEnd):
				roomDict[nameIn] = tileDict[keyIn].init(i, j)
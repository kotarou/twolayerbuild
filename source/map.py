import pyglet, tile

class Map:

	tileDict = {} # a map of the tile classes used in the current map
	roomDict = {} # a map of the rooms used in the current map - 

	# basically test code atm
	def __init__(self):
		createTileObject((0,True, "."))
		createRoom(tileDict[0], 0, 0, 0, 5, 5)
		for rooms in roomDict:
			for tiles in rooms:
				print(str(navigatable))

	# defines the tiles used in the current map
	# takes tileTypeIn[]:
	#	[0] is always the tile class reference name - unique
	#	[n], where 1-n define the tile's properties.

	def createTileObject(self, tileTypeIn):
		tileDict[tileTypeIn[0]] = Tile.type(str(tileTypeIn[0]), (), {'navigatable': tileTypeIn[1], 'draw': tileTypeIn[2]})

	# creates each of the rooms
	# adds the room to the roomDict
	# also modifies the rooms if needed - checking if a tile exists at the coordinates given and if so, replaces it
	#	Does this by:
	#	Checking if there is a tile at the said coordinates
	#	If so, removing the tile's reference from whatever room it is associated with
	#	Then dereferencing it from the map itself

	def createRoom(self, tileNameIn, roomNameIn, xStart, yStart, xEnd, yEnd):

		for i in range(xStart, xEnd):
			for j in range(yStart, yEnd):
				roomDict[roomNameIn] += tileDict[tileNameIn].init(roomDict[roomNameIn], i, j)
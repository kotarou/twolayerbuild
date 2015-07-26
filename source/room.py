import pyglet, tile

class Room:

	tileDict = {}
	roomDict = {}

	#defines the rooms used in the current map
	#takes a single room input and adds it to the tileDict - which is referenced in the creation of rooms
	#TODO: create the ability for the base characteristics of the tiles to be defined here
	#TODO: create the ability for tile-scripts to be inputted here

	def __init__(self, keyIn, roomTypeIn):
		for i in range(0,keyIn.len()):
			tileDict[keyIn[i]] = o[roomTypeList[i]]

	#creates each of the rooms
	#adds the room to the roomDict

	def createRoom(self, keyIn, nameIn, xStart, yStart, xEnd, yEnd):
		for i in range(xStart, xEnd):
			for j in range(yStart, yEnd):
				roomDict[nameIn] = tileDict[keyIn].init(i, j)
import pyglet, tile, os

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
  #  [0] is always the tile class reference name - unique
  #  [n], where 1-n define the tile's properties.

  def createTileObject(self, tileTypeIn):
    tileDict[tileTypeIn[0]] = Tile.type(str(tileTypeIn[0]), (), {'navigatable': tileTypeIn[1], 'draw': tileTypeIn[2]})

  # creates each of the rooms
  # adds the room to the roomDict
  # also modifies the rooms if needed - checking if a tile exists at the coordinates given and if so, replaces it
  #  Does this by:
  #  Checking if there is a tile at the said coordinates
  #  If so, removing the tile's reference from whatever room it is associated with
  #  Then dereferencing it from the map itself

  def createRoom(self, tileNameIn, roomNameIn, xStart, yStart, xEnd, yEnd):

    for i in range(xStart, xEnd):
      for j in range(yStart, yEnd):
        roomDict[roomNameIn] += tileDict[tileNameIn].init(roomDict[roomNameIn], i, j)


  # Load a map from file
  def load(self, filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    # First line is dimensions of map
    slines = lines[0].split()
    # ugly as sin, but lets make them ints
    self.dimensions = []
    self.dimensions.append(int(slines[0]))
    self.dimensions.append(int(slines[1]))

    self.mapchr = []

    i = 1
    ismap = True

    while ismap == True:
      if lines[i][0] != '[':
        # add an assert here for sanity
        self.mapchr.append(lines[i].strip())

      else: ismap = False
      i += 1

    # room is a dict, name to rooms
    self.rooms = {}
    room = ''

    for line in lines[i-1:]:
      if line[0] == '[':
        room = line.strip().strip('[]')
        self.rooms[room] = []
      else:
        rm = line.strip().split()
        #print(rm)
        rm2 = []
        pair = []
        for item in rm:
          rm2 = self.to_int_pair(item)
          pair.append(rm2)
        self.rooms[room].append(pair)
    return (self.dimensions, self.mapchr, self.rooms)

  # converts a pair of numbers with a comma to a twotupple of int
  def to_int_pair(self, pair):
      proc = pair.split(',')
      return (int(proc[0]),int(proc[1]))


if __name__ == "__main__":
  mapname = 'resources/map.dat'
  # Config file is in root of the project
  mappath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapname)
  loader = Map()
  p = loader.load(mappath)
  print(p)

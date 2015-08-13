import pyglet, tile, os
# lets assume we are calling from the source dir
mapname = os.path.join('resources','map.dat')

class Map:

  # 2d list of tiles
  gamemap = []

  # total x tiles
  mapx = 0

  # total y tiles
  mapy = 0


  # basically test code atm
  def __init__(self):
    # First we load the map
    # Config file is in root of the project
    mappath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapname)
    datas = self.load(mappath)

    # initialise local values
    mapx = datas[0][0]
    mapy = datas[0][1]

    # rudementry map
    basicmap = datas[1]

    # rudementry rooms
    basicrooms = datas[2]

    # build the map as a 2d list of tiles
    for i in xrange(0, mapy):
      for ii in xrange(0, mapx):
        gamemap[ii][i] = Tile(basicmap[ii][i],ii,i)

    # precompute adjacent tiles
    for i in xrange(0, mapy):
      for ii in xrange(0, mapx):
        set_adjacent(self, i,ii)

    # set tiles to rooms


  # set all the adjacencys up
  def set_adjacent(self,i,ii):


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

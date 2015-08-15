# -*- coding: utf-8 -*-
"""
@author: Till
"""


import pyglet, tile, os
# lets assume we are calling from the source dir
mapname = os.path.join('resources','map.dat')

class Map:

  # basically test code atm
  def __init__(self):
    # First we load the map
    # Config file is in root of the project
    mappath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapname)
    datas = self.load(mappath)

    # 2d list of tiles
    self.gamemap = []

    # initialise local values
    self.mapx = datas[0][0]
    self.mapy = datas[0][1]

    # rudementry map
    self.basicmap = datas[1]

    # rudementry rooms
    self.basicrooms = datas[2]

    # build the map as a 2d list of tiles
    for i in range(0, self.mapy):
      for ii in range(0, self.mapx):
        self.gamemap[ii][i] = tile.Tile(self.basicmap[ii][i],ii,i)

    # precompute adjacent tiles
    for i in xrange(0, self.mapy):
      for ii in xrange(0, self.mapx):
        self.set_adjacent(self, i,ii)

    # set tiles to rooms
    # for each room
    for roomname, values in self.basicrooms.items():
      # get all the subrooms that make it up
      for value in values:
        # start of subroom
        sx = value[0][0]
        sy = value[0][1]
        # end of subroom
        ex = value[1][0]
        ey = value[1][1]
        # set all the tiles to that room
        for i in range(sx, ex):
          for ii in range(sy, ey):
            self.gamemap[ii][i].rooms.append(roomname)

  # set all the adjacencies up
  def set_adjacent(self, i, ii):
    # first the regular directions lets leave diagonals for later
    if i != 0:
      self.gamemap[ii][i].above = self.gamemap[ii][i-1]

    if ii != 0:
      self.gamemap[ii][i].left = self.gamemap[ii-1][i]

    if i != mapy:
      self.gamemap[ii][i].below = self.gamemap[ii][i+1]

    if ii != mapx:
      self.gamemap[ii][i].right = self.gamemap[ii+1][i]

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
  #mappath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapname)
  loader = Map()
  #p = loader.load(mappath)
  #print(p)

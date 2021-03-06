# -*- coding: utf-8 -*-
"""
@author: Till
"""


import pyglet, tile, os

class Map:

  # basically test code atm
  def __init__(self, mappath):
    # First we load the map
    # Config file is in root of the project
    datas = self.load(mappath)

    # initialise local values, adjusted for 0 indexes
    self.mapx = (datas[0][0])
    self.mapy = (datas[0][1])

    # 2d list of tiles
    self.gamemap = []

    # seed with empty lists
    for slot in range(0,self.mapy):
      self.gamemap.append([])

    # rudementry map
    self.basicmap = datas[1]

    # rudementry rooms
    self.basicrooms = datas[2]

    # build the map as a 2d list of tiles
    for i in range(0, self.mapy):
      for ii in range(0, self.mapx):
        #print("doing " + str(i) +" "+ str(ii))
        self.gamemap[ii].insert(i, tile.Tile(self.basicmap[ii][i],ii,i))

    # precompute adjacent tiles
    for i in range(0, self.mapy):
      for ii in range(0, self.mapx):
        #print(i, ii)
        #print(self.mapx)
        #print(len(self.gamemap))
        self.set_adjacent(i, ii)

    # set tiles to rooms
    # for each room
    for roomname, values in self.basicrooms.items():
      # get all the subrooms that make it up
      #print(roomname)
      for value in values:
        #print(value)
        # start of subroom
        sx = value[0][0]
        sy = value[0][1]
        # end of subroom
        ex = value[1][0]
        ey = value[1][1]
        # set all the tiles to that room
        for i in range(sy, ey+1):
          for ii in range(sx, ex+1):
            #print(str(i) + "," +str(ii))
            self.gamemap[i][ii].rooms.append(roomname)

  # set all the adjacencies up
  def set_adjacent(self, i, ii):
    # first the regular directions lets leave diagonals for later
    #print("doing " + str(i) +" "+ str(ii))
    if i != 0:
      #print("above")
      self.gamemap[ii][i].left = self.gamemap[ii][i-1]

    if ii != 0:
      #print("left")
      self.gamemap[ii][i].above = self.gamemap[ii-1][i]

    if i != self.mapy -1:
      #print("below")
      self.gamemap[ii][i].right = self.gamemap[ii][i+1]

    if ii != self.mapx -1:
      #print("right")
      self.gamemap[ii][i].below = self.gamemap[ii+1][i]

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

  # prints out a representation of the map
  def draw(self):
    for row in self.gamemap:
      x = ""
      for tile in row:
        x += tile.symbol
      print(x)

  # ensures they have sane adjacencies
  def printadj(self):
    # first print them, see if it looks good
    for row in self.gamemap:
      x = ""
      for tile in row:
        x += (tile.adjsymbol() + " ")
      print(x)
    # here will be some other tests

  def printrooms(self):
    for row in self.gamemap:
      x = ""
      for tile in row:
        for room in tile.rooms:
          x += (room + " ")  
        x += ("|")
      print(x)



# Debug
if __name__ == "__main__":

  mapn = os.path.join('resources','map.dat')
  mapp = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapn)
  # Config file is in root of the project
  #mappath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), mapname)
  loader = Map(mapp)
  loader.printrooms()
  loader.draw()
  loader.printadj()
  #p = loader.load(mappath)
  #print(p)

# -*- coding: utf-8 -*-
"""
@author: EdibleEd
"""
import os



class MapLoader:
  """
     Loads a map file into the game
  """
  def __init__(self):
    pass

  def parse(self, fileloc):

    # load it all to memory
    f = open(fileloc, 'r')
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
  loader = MapLoader()
  p = loader.parse(mappath)
  print(p)

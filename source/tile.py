
class Tile:

  texture = 0
  above = None
  left = None
  right = None
  below = None
  # diagonally adjacent
  adjacentdiag = []

  #vertically or horizontally adjacent
  adjacentxy = []

  navigatable = True
  rooms = []
  contents = []

  def __init__(self, symbol, x, y):

    self.x = x
    self.y = y

    # set its texture based on character in map
    if symbol == "#:
      pass

    elif symbol == "*":
      pass

    elif symbol == ".":
      pass

    elif symbol == "@":
      pass

    else:
      print("oopsy " + symbol)

  def build_adjacentcy(self):
      pass


  def is_adjacent_room(self, room):
      pass

  def is_diag_adjacent_room(self, room):
      pass

  def add_content(self, identifier):
      pass

  def remove_content(self, identifier):
      pass

  def get_contents(self):
      pass

  def contains(self, identifier):
      pass

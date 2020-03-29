from element import Element 

class Node:
  Element[] E
  float[] cent
  Node[] links
  Element parent

  def __init__(self, E, cent, links, parent):
    self.E = E
    self.cent = cent
    self.links = links
    self.parent = parent
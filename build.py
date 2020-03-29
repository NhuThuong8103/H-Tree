from node import Node
from element import Element
import math

def INE(element, root, x1, x2):
  Node NODE = root

  if NODE == None
    root = Node()
    root.E = element
    root.cent = element.v
    root.links = None

    root.parent = None

  else
    float _min = 0
    flag = 0
    for n in range(len(NODE.links)) # 
      i = euclide(NODE.links[n].cent, element.v)
      if n == 0
        _min = i
      if i < _min
        _min = i
        flag = n

    d = euclide(NODE.links[flag].cent, element.v)

    if d <= x1 # create 1 là con cua node hien tai
      NODE.links[flag] = NODE.links[flag].append(element) 

      node = Node()
      node.E = element
      node.cent = element.v
      node.links = None
      node.parent = #NODE.E # lưu 1 element gồm : 1 vector + id + label 

    else if d > x1 && d <= x2
      INE(element, NODE.links[flag], x1, x2)
    else if d > x2 # create 1 node ngang cấp với nó
      node = Node()
      node.E = element
      node.cent = element.v
      node.links = None
      node.parent = NODE.parent

      NODE.links.append(node) # add 1 node vào links tức là add thêm 1 đường link từ node cha tới node mình mới thêm vào

def euclide(v1, v2):
  float f = 0;

  for (i = 1; i < v1.count; i++)
  {
      f += math.pow(v1[i] - v2[i], 2);
  }

  return math.sqrt(f);

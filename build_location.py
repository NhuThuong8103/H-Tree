import math

def drawLine(*args):
  # for arg in args: print arg
  print("would draw line at point: " +str(args))

def drawHTree(x, y, lenght, depth):
  if depth == 0: return

  drawLine((x - lenght / 2, y), (x + lenght / 2, y))

  rightVertXCord = x + lenght / 2

  rightVertYCordBottom = y - lenght / 2

  rightVertYCordTop = y + lenght / 2

  drawLine((rightVertXCord, rightVertYCordTop), (rightVertXCord, rightVertYCordBottom))

  leftVertXCord = x - lenght / 2

  leftVertYCordBottom = y - lenght / 2

  leftVertYCordTop = y + lenght / 2

  drawLine((leftVertXCord, leftVertYCordTop), (leftVertXCord, leftVertYCordBottom))

  drawHTree(leftVertXCord, leftVertYCordBottom, lenght / math.sqrt(2), depth - 1)
  drawHTree(leftVertXCord, leftVertYCordBottom, lenght / math.sqrt(2), depth - 1)
  drawHTree(rightVertXCord, leftVertYCordBottom, lenght / math.sqrt(2), depth - 1)
  drawHTree(rightVertXCord, leftVertYCordBottom, lenght / math.sqrt(2), depth - 1)


drawHTree(10.0, 10.0, 2.0, 4.0)


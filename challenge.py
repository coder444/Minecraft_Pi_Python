from mcpi import minecraft
import math
from time import sleep
import sys
mc = minecraft.Minecraft.create()

def circle(yy, size):
  deg = 0
  while deg < 360:
    xx = math.tan(math.cos(math.radians(deg)) * size)
    zz = math.tan(math.sin(math.radians(deg)) * size)
    mc.player.setPos(xx, yy, zz)
    mc.setBlock(xx, yy, zz, 35, yy + xx + zz)
    deg += 1

try:
  print("Python is working")
  i = 10
  nY = 50
  nSize = 100
  while i > 0:
    circle(nY, nSize)
    nSize -= 1
    nY -= 1
    i -= 1
except KeyboardInterrupt:
  sys.exit()

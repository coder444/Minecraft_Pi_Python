from mcpi import minecraft
#A library that creates random numbers
import random
mc = minecraft.Minecraft.create()

#Forever
while True:
  x, y, z = mc.player.getPos()
  mc.setBlock(x, y, z, random.randint(0, 42))

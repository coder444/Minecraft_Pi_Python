from mcpi import minecraft
import math
mc = minecraft.Minecraft.create()
y = 50
radius = 5
degree = 0
while degree < 36000:
    x = radius * math.sin(math.radians(degree))
    z = radius * math.cos(math.radians(degree))
    mc.setBlock(x, y, z, 35,x)
    degree += 1
    y -= 0.01
    radius += 0.02
mc.postToChat("hello")

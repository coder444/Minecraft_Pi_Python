from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()
rainbows = [
    x for x in range(0, 15)
    ]
x, y, z = mc.player.getPos()
while True:
    for rainbow in rainbows:
        mc.setBlock(x + 1, y, z, 35, rainbow)
        sleep(0.1)

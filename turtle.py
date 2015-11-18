from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

while True:
    e = mc.events.pollBlockHits()
    for ev in e:
        x, y, z = ev.pos
        while True:
            mc.setBlock(x, y + 1, z, 44)
            mc.setBlock(x, y, z, 89)
            sleep(0.1)
            mc.setBlock(x, y, z, 0)
            mc.setBlock(x, y + 1, z, 0)
            x += 1
            mc.setBlocks(x, y, z, x + 5, y + 5, z + 3, 95)
            x += 1
            sleep(0.5)

from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()
rainbows = [
    x for x in range(0, 15)
    ]
while True:
    e = mc.events.pollBlockHits()
    for ev in e:
        while True:
            for rainbow in rainbows:
                mc.setBlock(ev.pos, 35, rainbow)
                sleep(0.1)

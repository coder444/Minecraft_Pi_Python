from mcpi import minecraft
mc = minecraft.Minecraft.create()

#Block you want to place, like 1 = Stone, 2 = Grass, 3 = Dirt, etc.
id = 1
#Finds your XYZ Position
x, y, z = mc.player.getPos()
#Places a block at your XYZ Position
mc.setBlock(x, y, z, id)

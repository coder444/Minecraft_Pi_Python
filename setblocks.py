from mcpi import minecraft
mc = minecraft.Minecraft.create()

#Finds your XYZ position
x, y, z = mc.player.getPos()
#The block you want to set
#Example: 1 = Stone, 2 = Grass, 3 = Dirt, etc.
id = 1
#Sets a block at your XYZ position
mc.setBlock(x, y, z, id)

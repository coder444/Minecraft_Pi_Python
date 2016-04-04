from mcpi import minecraft
mc = minecraft.Minecraft.create()


print(mc.getPlayerEntityIds())
id = input('Hi! Input an Entity ID: ')
pos = mc.entity.getPos(id)
x, y, z = pos
mc.player.setPos(x, y, z)

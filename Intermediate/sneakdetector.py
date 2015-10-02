from mcpi import minecraft
mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x, y, z, 35)
#95 is Invisible Bedrock, only avaliable in early versions of PE and Pi
mc.setBlock(x, y, z, 95)
mc.postToChat('Sneak on this block to detect.')

while True:
  xx, yy, zz = mc.player.getTilePos()
  xxx, yyy, zzz = xx, yy - 1, zz
  if(mc.getBlockWithData(xxx, yyy, zzz).id == 95):
    mc.postToChat('Sneak')

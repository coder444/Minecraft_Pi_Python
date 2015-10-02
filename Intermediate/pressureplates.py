#Jump on a Stone or Wooden Slab to activate
from mcpi import minecraft
mc = minecraft.Minecraft.create()

while True:
  #Creates a XYZ pos for the Tile Pos
  xx, yy, zz = mc.player.getTilePos()
  #getTilePos detects what block your feet are in, so this fixes it
  x, y, z = xx, yy - 1, zz
  #the getTilePos function does not require a for loop to read, it is not a list
  if(mc.getBlockWithData(x, y, z).id == 44):
    #Stone Pressure Plate
    if(mc.getBlockWithData(x, y, z).data == 0):
      mc.postToChat('You stepped on a Stone Pressure Plate!')
    #Wooden Pressure Plate
    elif(mc.getBlockWithData(x, y, z).data == 2):
      mc.postToChat('You stepped on a Wooden Pressure Plate!')
    else:
      mc.postToChat('Use a Stone or Wooden Slab!')

from mcpi import minecraft
mc = minecraft.Minecraft.create()

while True:
  #Sets a XYZ Position to where you Right Click a block
  e = mc.events.pollBlockHits()
  #Goes through variable e
  for ev in e:
    #If the ID that pollBlockHits collects is 46 (TNT), it places a ready to explode TNT
    if(mc.getBlockWithData(ev.pos).id == 46):
      mc.setBlock(ev.pos, 46, 1)

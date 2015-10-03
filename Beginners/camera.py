from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

mc.postToChat('Your camera has been FROZEN!')
#Make the camera fixed
mc.camera.setFixed()
i = 10
while i > 0:
  mc.postToChat(i)
  sleep(1)
mc.postToChat('Your camera has been set NORMAL!')
#Reset the camera
mc.camera.setNormal()

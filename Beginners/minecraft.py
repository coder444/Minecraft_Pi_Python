#Imports Minecraft from MCPI
from mcpi import minecraft
#Connects to Minecraft
mc = minecraft.Minecraft.create()

#Posts Hello World to the chat
mc.postToChat('Hello World')

from mcpi.minecraft import Minecraft as mcs
from time import sleep
mc = mcs.create()
while True:
    mc.executeCommand("time add 300" )
    
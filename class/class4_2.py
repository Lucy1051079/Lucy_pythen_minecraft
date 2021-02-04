from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
x,y,z = mc.player.getPos()
number = 1
for i in range(8):
    time.sleep(1)
    for j  in range(number):
        mc.spawnEntity(x,y,z,60)
    nnumber = number * 2
    mc.postToChat(number)
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()  
x,y,z = mc.player.getPos()
for i in range(30):
    mc.setBlock(x-1,y-1,z,169)
    
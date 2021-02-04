from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
w=5
h=5
mc.setBlocks(x,y,z,x+w,y+h,z+w,89)
mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+w-1,0)
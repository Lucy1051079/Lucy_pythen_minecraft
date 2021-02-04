from mcpi.minecraft import Minecraft as mcs
mc =mcs.create()
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,46)
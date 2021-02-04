from mcpi.minecraft import Minecraft as mcs
mc =mcs.create()
mc.player.setTilePos(15,15,15)
print(mc.player.getTilePos())
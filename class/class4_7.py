from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
ID = mc.getPlayerEntityId("jerry971118")
mc.postToTitle(ID,"hello")

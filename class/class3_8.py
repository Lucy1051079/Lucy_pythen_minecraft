from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
pos = mc.player.getTilePos()
base = int(input())
hieght = (base//2) +1
for i in range(hieght):
    x = pos.x + i
    y = pos.y + i
    x2 = pos.x + base - i
    z = pos.z + i
    z2 = pos.z + base - i
    print(x,y,z,x2,y,z2)
    mc.setBlocks(x,y,z,x2,y,z2,24)
   
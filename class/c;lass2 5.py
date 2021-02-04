from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while time:
    try:
        num = int(input("what do you want?"))
        break
    except:
        print("Error")
x,y,z= mc.player.getTilePos()
mc.setBlock(x,y,z,num)
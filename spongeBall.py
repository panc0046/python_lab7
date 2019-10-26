from gfxhat import lcd, backlight
from spongeBallLibrary import *
import time

obj =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

x = int(input("Enter x coordinate"))
y = int(input("Enter y coordinate"))
vx = int(input("Enter vx value"))
vy = int(input("Enter vy value"))
lcd.clear()
backlight.set_all(0,255,0)
backlight.show()
while True:
    x,y,vx,vy = moveObject(obj,x,y,vx,vy)
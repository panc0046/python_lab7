from gfxhat import lcd, backlight

def displayObject(x,y,selectObject):     
    lcd.clear()
    i = 0
    counter = 0
    while i < len(selectObject):
        j = 0
        temp_x = x
        temp_y = y + counter
        while j < len(selectObject[i]):
            lcd.set_pixel(temp_x,temp_y,selectObject[i][j])
            j = j+1
            temp_x = temp_x+1
        i = i+1
        counter = counter+1
        temp_y=temp_y+1
        lcd.show()

def eraseObject(obj,x,y):
    i = 0
    counter = 0
    while i < len(obj):
        j = 0
        temp_x = x
        temp_y = y + counter
        while j < len(obj[i]):
            lcd.set_pixel(temp_x,temp_y,0)
            j = j+1
            temp_x = temp_x+1
        i = i+1
        counter = counter+1
        temp_y=temp_y+1
        lcd.show()

def moveObject(obj,x,y,vx,vy):
    if y+len(obj) <= 63 and y+len(obj) >= 0 and x+len(obj)<=127 and x+len(obj) >= 0:
        eraseObject(obj,x,y)
    x,y,vx,vy = checkCollision(obj,x,y,vx,vy,128,64)
    if y+len(obj) <= 63 and y+len(obj) >= 0 and x+len(obj)<=127 and x+len(obj) >= 0:
        displayObject(x,y,obj)
    return x,y,vx,vy

def checkCollision(obj,x=0,y=0,vx=0,vy=0,Sx=128,Sy=64):
    if x-len(obj)<0:
        vx=abs(vx)
    if y-len(obj)<0:
        vy=abs(vy)
    if x+len(obj)>Sx:
        vx=-vx
    if y+len(obj)>Sy:
        vy=-vy
    x=x+vx
    y=y+vy
    return x,y,vx,vy
    
    
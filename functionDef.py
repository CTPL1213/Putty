import autopy as a
from config import *
import time
def connectionType():
    y=a.bitmap.Bitmap.open('images/screen.png')
    if(connection_type=='SSH'): 
        x=a.bitmap.Bitmap.open('images/ssh.png')
        pos = y.find_bitmap(x)
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
    elif(connection_type=='Serial'):
        x=a.bitmap.Bitmap.open('images/serial.png')
        pos = y.find_bitmap(x)
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
    elif(connection_type=='Other'):
        x=a.bitmap.Bitmap.open('images/other.png')
        pos = y.find_bitmap(x)
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
    else:
        x=a.bitmap.Bitmap.open('ssh.png')
        pos = y.find_bitmap(x)
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()

def IPconfigure():
    y=a.bitmap.Bitmap.open('images/screen.png')
    x=a.bitmap.Bitmap.open('images/ip.png')
    pos = y.find_bitmap(x)
    if pos:
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
        a.key.type_string(IP, wpm=100)
    else:
        x=a.bitmap.Bitmap.open('images/ip_1.png')
        pos = y.find_bitmap(x)
        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
        a.key.type_string(IP, wpm=100)

def open():
    y=a.bitmap.Bitmap.open('images/screen.png')
    x=a.bitmap.Bitmap.open('images/open.png')
    pos = y.find_bitmap(x)
    a.mouse.move(pos[0],pos[1])
    a.mouse.click()
    
def credentials():
    a.bitmap.capture_screen().save('images/screen_1.png')
    y=a.bitmap.Bitmap.open('images/screen_1.png')
    x=a.bitmap.Bitmap.open('images/cre.png')
    pos = y.find_bitmap(x)
    a.mouse.move(pos[0],pos[1])
    a.mouse.click()
    a.key.type_string('i', wpm=100)
    a.key.type_string(user, wpm=100)
   # a.key.tap(a.key.Code.ENTER, [a.key.Modifier.META])
    time.sleep(2)
    a.bitmap.capture_screen().save('images/screen_2.png')
    y=a.bitmap.Bitmap.open('images/screen_2.png')
    x=a.bitmap.Bitmap.open('images/cre.png')
    pos = y.find_bitmap(x)
    a.mouse.move(pos[0],pos[1])
    a.mouse.click()
    a.key.type_string('i', wpm=100)
    a.key.type_string(password, wpm=100)
    time.sleep(2)
    
def connection_check():
    a.bitmap.capture_screen().save('images/screen_3.png')
    y=a.bitmap.Bitmap.open('images/screen_3.png')
    x=a.bitmap.Bitmap.open('images/success.png')
    pos = y.find_bitmap(x)
    if pos:

        a.mouse.move(pos[0],pos[1])
        a.mouse.click()
        a.key.type_string('echo "Connection Successful..."\n', wpm=100)
        time.sleep(2)
        #a.alert.alert("Connection state: Successful")
    else:
        a.alert.alert("Connection state: Un_Successful")

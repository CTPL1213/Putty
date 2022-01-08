import autopy as a
import subprocess 
import time
from config import *
from functionDef import *

if __name__=='__main__':

    path='/bin/putty'
    subprocess.Popen(path)
    time.sleep(10)
    a.bitmap.capture_screen().save('images/screen.png')

    IPconfigure()
    time.sleep(2)
    connectionType()
    time.sleep(2)
    open()
    time.sleep(2)
    credentials()
    time.sleep(2)
    connection_check()
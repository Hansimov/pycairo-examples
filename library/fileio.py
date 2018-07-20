import os
import time
import subprocess

def openImg(img_name):
    # Refer to: Using os.system() inside a function
    #   https://stackoverflow.com/questions/43502004/using-os-system-inside-a-function
    # This will call the default image viewer
    cmd  = os.path.join(os.getcwd(), img_name)
    # cmd  = 'i_view64 ' + os.path.join(os.getcwd(), img_name)
    os.system(cmd)


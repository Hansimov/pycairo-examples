import sys
sys.path.append('../library/')

from header import *

def startup():
    width, height = 256, 256
    sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    
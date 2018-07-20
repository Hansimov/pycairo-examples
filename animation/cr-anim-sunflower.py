import sys
sys.path.append('../library/')

from header import *


# Start up
width, height = 256, 256
sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(sfc)

# Drawing
ctx.set_source_rgb(0, 1, 0)
ctx.move_to(10, 10)
ctx.arc(330, 60, 40, 0, 2*math.pi)
ctx.fill()

# End up
img_name = './frames/sunflower.png'
sfc.write_to_png(img_name)
openImg(img_name)


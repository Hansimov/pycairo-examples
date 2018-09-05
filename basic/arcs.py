# <arcs.py>

# What you will learn from this script:
'''
- draw several kinds of arcs
  - arc, circle, ellipse
  - (counter) clockwise
- fill
  - preserve path after fill
- stroke
  - set line width
  - preserve path after stroke
'''

import cairo
import os
from math import pi

WIDTH, HEIGHT = 854, 480
sfc = cairo.ImageSurface(cairo.Format.ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(sfc)

ctx.set_source_rgb(0.05, 0.05, 0.05)
# ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.paint()

# arc(xc, yc, radius, angle1, angle2)
ctx.set_source_rgb(1, 1, 0)
ctx.arc(WIDTH/2, HEIGHT/2, 100, 0, 2*pi)
ctx.set_line_width(10)
ctx.stroke()

ctx.set_source_rgb(1, 0, 0)
ctx.arc(WIDTH/2, HEIGHT/2, 100, 0, pi)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(5)
ctx.stroke()

output_filename = 'arcs.png'
sfc.write_to_png(output_filename)
os.system(output_filename)




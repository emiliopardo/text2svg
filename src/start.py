# importing pycairo
import cairo
 
# Defining surface area
WIDTH = 1
HEIGHT = 1
PIXEL_SCALE = 32
 
# creating a SVG surface
# here geek95 is file name

for i in range(33,126):
    print(chr(i))
    surface = cairo.SVGSurface(str(i)+'.svg', WIDTH*PIXEL_SCALE,HEIGHT*PIXEL_SCALE)
 
    # creating a cairo context object for SVG surface
    # using Context method
    context = cairo.Context(surface)
 
    # Scaling Surface
    context.scale(PIXEL_SCALE, PIXEL_SCALE)
 
    # Creating Rectangle For Background
    context.rectangle(0, 0, WIDTH, HEIGHT)
 
    # Color of Rectangle For Background
    context.set_source_rgb(0, 0, 0)
 
    # Filling Color in Rectangle
    context.fill()
 
    # defining color
    context.set_source_rgb(1, 1, 1)

    # Font Style
    context.set_font_size(1)
 
    # font style
    context.select_font_face("ESRI US Forestry 2", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
 
    # Creating Rectangle
    context.rectangle(0, 0, 2, 2)
 
    # move to x, y percentage of surface
    context.move_to(0.2, 1)
 
    # Display Text
    context.text_path(chr(i))
 
    # Filling the area
    context.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
 
    # Filling color
    context.fill()
 
    # stroke out the color and width property
    context.stroke()
 
    # printing message when file is saved
    print("File Saved")
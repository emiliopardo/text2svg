from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from lxml import etree
import os
import sys


# using Space Mono because Recursive has wide code ligatures
fontPath = "sources/ESRI_US_Forestry_2.ttf"

outputDir = "output/exports/svg"

if not os.path.exists(outputDir):
    os.makedirs(outputDir)


with TTFont(fontPath) as f:
    glyphSet = f.getGlyphSet()

    for glyphName in glyphSet.keys():
        print(glyphName)
        # print("\n")
        svgpen = SVGPathPen(glyphSet)
        glyph = glyphSet[glyphName]
        glyph.draw(svgpen)
        path = svgpen.getCommands()
        # print(path)
        # print("\n")

        stringXML='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32pt" height="32pt" viewBox="0 0 32 32" version="1.1">
<g id="surface1">
<rect x="0" y="0" width="32" height="32" style="fill:rgb(0%,0%,0%);fill-opacity:1;stroke:none;"/>
<path style=" stroke:none;fill-rule:evenodd;fill:rgb(100%,100%,100%);fill-opacity:1;" d="'''+path+''' "/>
</g>
</svg>'''
        # root = etree.fromstring(stringXML)

        # print(etree.tostring(root, pretty_print=True).decode('utf-8'))

        with open(glyphName+".svg", "w") as file:  # Use file to refer to the file object
            file.write(stringXML)
        # print(stringXML)

    # for key, value in glyphSet.items() :
    #     print(key, value)

    
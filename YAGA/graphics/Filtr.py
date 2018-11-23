# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import random
import numpy as np
image = Image.open("r2.jpg")
pix=image.load()
draw=ImageDraw.Draw(image)
width=image.size[0]
height=image.size[1]
for i in range(width):
    for j in range(height):
        a=pix[i,j][0]
        b=pix[i,j][1]
        c=pix[i,j][2]
        S = a + b + c
        if (S > (((255 + 30) // 2) * 3)):
            a, b, c = 255, 255, 255
        else:
            a, b, c = 0, 0, 0
        draw.point((i, j), (a, b, c))
        
image.save('r5.jpg')
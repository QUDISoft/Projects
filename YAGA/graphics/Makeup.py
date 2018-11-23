# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import random
import numpy as np
ar=np.asarray
arr=np.array


s=ar([21,24,12,51,512])
image = Image.open("r2.jpg")
#image1 = Image.open("r1.png")
image2 = Image.open("r1.jpg")
pix=image.load()
i=ar(image, dtype='int32')
#i1=ar(image1, dtype='int32')
i2=ar(image2, dtype='int32')
c=((i+i2+i+i)//4).astype('uint8')
im = Image.fromarray(c)
im.save("r3.jpg")

# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
import json
import glob
import os
import time

from PIL import Image

img = Image.open("E:\\screenshot\\new.png")
print(img.size)
# cropped = img.crop((10,50,800,500))  # (left, upper, right, lower)
# cropped.save("E:\\screenshot\\new4.png")
# image = Image.open("E:\\screenshot\\new4.png")
data= pytesseract.image_to_string(img)
print(data)







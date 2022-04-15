# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:34:26 2022

@author: Abdelrahman Ragab
"""

from PIL import Image
from PIL.ExifTags import TAGS

#  open the image

img = Image.open(r"img_1771.jpg")


# extract EXIF data
exif_data = img.getexif()

if exif_data is None:
    print('Sorry, image has no exif data.')

else:
    # iterating over all EXIF data fields
    for tag_id in exif_data:
        
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id)
        data = exif_data.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
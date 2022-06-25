import tkinter
from PIL import Image, Image
import os


# #
l  = '/home/ameen/Desktop/copy_to_usb/PHOTO/pic/'

def imge_file(location):
    loca = os.listdir(f'{location}')
    all_img = []
    for file in loca:
        file = str(file).lower()
        if '.png' in file:
            all_img.append(file)
        elif 'jpg' in file:
            all_img.append(file)
    return print(all_img)


imge_file(l)
# print(imge_file(l))
import tkinter
from PIL import Image, Image
import os


# def fil_loc():
#     print(f' you are in _{os.getcwd}')
#     loc= os.listdir('/home/ameen/Desktop/copy_to_usb/PHOTO/pic')
#     for img in loc:
#         img = img.lower()
#         print(img)

# fil_loc()


# def imgsize(loc):
#     pic = Image.open(loc)
#     pic.size()

def load_image():
    path = os.listdir('/home/ameen/Desktop/copy_to_usb/PHOTO עע/pic/')
    for pic in path:
        pic = str(pic)
        if 'jpg' in pic.lower() or 'png' in pic.lower():
            print(pic)
            return pic


load_image()
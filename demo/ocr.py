# coding:utf-8
from pyocr import pyocr
from PIL import Image

tools = pyocr.get_available_tools()[:]
print tools[0].image_to_string(Image.open('D:\\demo2.jpg'))
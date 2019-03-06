# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:34
# @Author  : Tony Goods
# @FileName: Image.py
# @Software: PyCharm
import os
import win32api
import win32gui

import win32con
from PIL import Image as IMAGE, ImageDraw, ImageFont

from src.utils import get_random_number


class Image:
    def __init__(self, poem):
        self.__poem = poem

    def get_image(self):
        im = IMAGE.open('../images/' + str(get_random_number(self.__get_images_number())) + '.jpg')
        ttfont = ImageFont.truetype('STXINGKA.TTF', 28)
        draw = ImageDraw.Draw(im)
        xSize, ySize = im.size
        print(self.__poem)
        poem_string = u'' + self.__poem['title'] + '\n' + self.__poem['author'] + '\n'
        for sentence in self.__poem['paragraphs']:
            poem_string += sentence + '\n'
        draw.text((xSize * 0.5, ySize * 0.1), poem_string, fill=(255, 255, 255), font=ttfont)
        im.show()
        im.save('../images/desktop.jpg')
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                                      os.path.abspath('../images/desktop.jpg'),
                                      win32con.SPIF_SENDWININICHANGE)

    def __get_images_number(self):
        path = '../images'
        dirs = os.listdir(path)
        return len(dirs) - 1

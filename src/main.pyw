# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 22:40
# @Author  : Tony Goods
# @FileName: main.pyw
# @Software: PyCharm

import os
import json
import time
import win32api
import win32gui

import win32con
from PIL import Image as IMAGE, ImageDraw, ImageFont
import random


def get_random_number(max_number):
    return random.randint(0, max_number)


class Image:
    def __init__(self, poem, setting):
        self.__poem = poem
        self.__setting = setting

    def get_image(self):
        if self.__setting['shouldChangeImage']:
            im = IMAGE.open('../images/DesktopImage/' + str(get_random_number(self.__get_images_number())) + '.jpg')
        else:
            im = IMAGE.open(self.__setting['imagePath'])
        ttfont = ImageFont.truetype('STFANGSO.TTF', 20)
        draw = ImageDraw.Draw(im)
        xSize, ySize = im.size
        print(self.__poem)
        poem_string = u'' + self.__poem['title'] + '\n' + self.__poem['author'] + '\n'
        for sentence in self.__poem['paragraphs']:
            poem_string += sentence + '\n'
        draw.text((xSize * 0.5, ySize * 0.05), poem_string, fill=(255, 255, 255), font=ttfont)
        timeString = str(int(time.time()))
        im.save('../images/DesktopImage/' + timeString + '.jpg')
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                                      os.path.abspath('../images/DesktopImage/' + timeString + '.jpg'),
                                      win32con.SPIF_SENDWININICHANGE)

    def __get_images_number(self):
        path = '../images'
        dirs = os.listdir(path)
        return len(dirs) - 2


class Poem:

    def __init__(self):
        self.poem = {}

    def get_poem(self):
        category = 0
        if category == 0:
            self.poem = self.get_ci()
        elif category == 1:
            self.poem = self.get_shi()
        elif category == 2:
            self.poem = self.get_shijing()
        elif category == 3:
            self.poem = self.get_wudai()
        return self.poem

    def get_ci(self):
        while (True):
            try:
                addr = '../poem/ci/ci.song.' + str(get_random_number(21) * 1000) + '.json'
                poems_array = json.load(open(addr, 'r', encoding='utf-8'))
                poem = poems_array[get_random_number(len(poems_array))]
                poem['title'] = poem['rhythmic']
                break
            except IndexError:
                continue
        return poem

    def get_shi(self):
        random_number = get_random_number(1)
        addr = '../poem/shi/poet.' + ['song', 'tang'][random_number] + '.' + str(
            get_random_number([254, 57][random_number]) * 1000) + '.json'
        poems_array = json.load(open(addr, 'r', encoding='utf-8'))
        return poems_array[get_random_number(1000)]

    def get_shijing(self):
        addr = '../poem/shijing/shijing.json'
        poems_array = json.load(open(addr, 'r', encoding='utf-8'))
        poem = poems_array[get_random_number(len(poems_array))]
        return {
            'title': poem['chapter'] + '·' + poem['section'] + '·' + poem['title'],
            'paragraphs': poem['content'],
            'author': ''
        }

    def get_wudai(self):
        addr = '../poem/wudai/' + ['poetrys', '花间集卷第一', '花间集卷第二', '花间集卷第三', '花间集卷第四', '花间集卷第五', '花间集卷第六', '花间集卷第七',
                                   '花间集卷第八', '花间集卷第九', '花间集卷第十'][get_random_number(10)] + '.json'
        poems_array = json.load(open(addr, 'r', encoding='utf-8'))
        return poems_array[get_random_number(len(poems_array))]


class Setting:
    def __init__(self):
        self.__setting = json.load(open('setting.json', 'r', encoding='utf-8'))

    def get_setting(self):
        return self.__setting


if __name__ == '__main__':
    setting = Setting().get_setting()
    if not setting['usingThisProgram']:
        exit()
    if setting['shouldRemoveBeforeImage']:
        files = os.listdir('../images/DesktopImage')
        for file in files:
            os.remove('../images/DesktopImage/'+file)
    if setting['shouldChangePoem']:
        poem = Poem()
        poem_json = poem.get_poem()
    else:
        poem_json = setting['poem']
    image = Image(poem_json, setting)
    image.get_image()
    exit()

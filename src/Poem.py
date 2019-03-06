# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 9:18
# @Author  : Tony Goods
# @FileName: Poem.py
# @Software: PyCharm
import json

from src.utils import get_random_number


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
        addr = '../poem/ci/ci.song.' + str(get_random_number(21) * 1000) + '.json'
        poems_array = json.load(open(addr, 'r', encoding='utf-8'))
        poem = poems_array[get_random_number(1000)]
        poem['title'] = poem['rhythmic']
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

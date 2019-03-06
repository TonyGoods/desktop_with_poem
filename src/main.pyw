# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 22:40
# @Author  : Tony Goods
# @FileName: main.pyw
# @Software: PyCharm
from src.Image import Image
from src.Poem import Poem

if __name__ == '__main__':
    file = open("test.txt", "w")
    poem = Poem()
    poem_json = poem.get_poem()
    image = Image(poem_json)
    image.get_image()
    file.write(poem_json['title'] + '\n')
    file.write(poem_json['author'] + '\n')
    for i in range(len(poem_json['paragraphs'])):
        file.write(poem_json['paragraphs'][i] + '\n')
    file.close()
    exit()

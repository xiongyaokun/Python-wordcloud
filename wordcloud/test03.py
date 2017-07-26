#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/25 14:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

'''
基础的例子

'''
from os import path

from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# 获取当前文件路径
# __file__为当前文件，在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# f = open(r'D:\Python\Python-wordcloud\wordcloud\alice.txt', 'r')
# txt = f.read()

# 读取文件
f = open(path.join(d, 'alice.txt'))
text = f.read()
f.close()

# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-life-quot-Alice-282261010
# 设置背景图片
alice_coloring = imread(path.join(d, 'alice_color.png'))
# alice_coloring = imread(path.join(d, 'xiongyaokun.jpg'))
# alice_coloring = imread(path.join(d, 'heart03.jpg'))
wc = WordCloud(background_color='white', max_words=200, mask=alice_coloring,
               stopwords=STOPWORDS.add('said'), max_font_size=40, random_state=42)
# 生成词云，可以用generate输入全部文本(中文不好分词)，也可以我们计算好词频后使用genetate_from_frequencies函数
wc.generate(text)

# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100), ('词b', 90), ('词c', 80)]

# 从背景图片生成颜色
image_colors = ImageColorGenerator(alice_coloring)
# 一下代码显示图片
plt.imshow(wc)
plt.axis('off')

# 绘制词云
plt.figure()

# recolor wordcloud and show
# we could also give color_func=image-colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')

# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file(path.join(d, 'test03.png'))
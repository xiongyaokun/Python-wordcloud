#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/25 14:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

'''
利用词频生成词云
显示中文字体

'''
from os import path
import os
import codecs
import jieba
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw, ImageFont

# 获取当前文件路径
# __file__为当前文件，在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# f = open(r'D:\Python\Python-wordcloud\wordcloud\alice.txt', 'r')
# txt = f.read()

# 读取文件
# f = open(path.join(d, 'zhangqingjie.txt'))
# f = open(path.join(d, 'zqingjie.txt'))
f = open(path.join(d, 'zqj-alice.txt'))
text = f.read()
text = text.replace('Alice', '清洁')
text = text.replace('said', '女神')
text = text.replace('Mock', '江西')
text = text.replace('Turtle', '吃货')
text = text.replace('little', 'Beauty')
text = text.replace('thing', 'Honey')
text = text.replace('know', 'Girl')
text = text.replace('wen', 'love')
text = text.replace('much', 'love')
text = text.replace('now', '旅行')
text = text.replace('quite', 'MISS')
text = text.replace('way', 'waiting')
text = text.replace('Mouse', 'Sheep')

f.close()

# 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(text))

# 读取背景图片
color_mask = imread(path.join(d, 'heart03.jpg'))
# color_mask = imread(path.join(d, 'zhangqingjie.jpg'))




wc = WordCloud(font_path=path.join(d,'HYQiHei-25JF.ttf'), background_color='white', max_words=4000, mask=color_mask,
               max_font_size=60, random_state=1)

# 生成词云，可以用generate输入全部文本(中文不好分词)，也可以我们计算好词频后使用generate_from_frequencies函数
word_cloud = wc.generate(cut_text)
# 保存图片
word_cloud.to_file(path.join(d, 'test04_01.jpg'))
# 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()



# 从背景图片生成颜色
image_colors = ImageColorGenerator(color_mask)
# 一下代码显示图片
# plt.imshow(wc)
# plt.axis('off')

# 绘制词云
# plt.figure()

# recolor wordcloud and show
# we could also give color_func=image-colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')

# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(color_mask, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file(path.join(d, 'test04.png'))
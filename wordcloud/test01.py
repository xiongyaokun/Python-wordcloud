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
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 获取当前文件路径
# __file__为当前文件，在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# f = open(r'D:\Python\Python-wordcloud\wordcloud\alice.txt', 'r')
# txt = f.read()

# 读取文件
f = open(path.join(d, 'alice.txt'))
txt = f.read()

f.close()
txt = txt.replace('Alice', 'zhangqingjie')

wordcloud = WordCloud(background_color='black', width=1000, height=860, margin=2).generate(txt)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
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
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, get_single_color_func
import matplotlib.pyplot as plt


d = path.dirname(__file__)

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

cut_text = " ".join(jieba.cut(text))

color_mask = imread(path.join(d, 'heart03.jpg'))

wc = WordCloud(font_path=path.join(d,'HYQiHei-25JF.ttf'), background_color='white', max_words=4000, mask=color_mask,
               max_font_size=60, random_state=1)

word_cloud = wc.generate(cut_text)
# 保存图片
word_cloud.to_file(path.join(d, 'test04_01.jpg'))
# 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()

class SimpleGroupColorFunc(object):

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}
        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

class GroupedColorFunc(object):

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()
        ]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Return a single_color_func assigned with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words
            )
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

# 自定义所以单词的颜色
color_to_word = {
    # words below will be colored with a green color function
    '#00ff00': ['beautiful', 'explicit', 'simple', 'sparse', 'readability', 'rules',
                'practicality', 'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
    #will be colored with a red single color function
    'red': ['ugly', 'implicit', 'complex', 'complicated', 'nested', 'dense', 'special',
            'errors', 'silently', 'ambiguity', 'guess', 'hard']
}






image_colors = ImageColorGenerator(color_mask)

plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')

# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(color_mask, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file(path.join(d, 'test04.png'))
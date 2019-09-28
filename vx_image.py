# -*- coding: utf-8 -*-
# 注意：print_function的导入必须在Image之前，否则会报错
from __future__ import print_function
from PIL import Image

"""
需求：给图片右下角添加中国国旗
欢迎国庆，喜庆70周年
"""
"""
注意我们可以根据头像的大小来修改模板的像素
"""

class Picture:

    def handle_picture(self):
        # 打开图片模版
        img1 = Image.open("./img/1.png")
        img1 = img1.convert('RGBA')
        size = (700, 700)
        img1.thumbnail(size)
        # 打开原来的微信头像
        img2 = Image.open("./img/two.jpg")
        img2 = img2.convert('RGBA')
        if img2.size != (700, 700):  # 判断图片大小，统一改为 700*700
            # 修改图片尺寸
            size = (700, 700)
            img2.thumbnail(size)
            img2.show()
        # 图片粘贴选区
        loc = (0, 0, 700, 700)
        # 将img1 粘贴到 img2
        img2.paste(img1, loc, img1)
        img2.show()   # 显示图片
        img2.save("new.png")   # 保存生成的头像图片

t0 = Picture()
t0.handle_picture()
# -*- coding:utf-8 -*-
'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
使用到Pillow：Python Imaging Library
author:wangt
'''

from PIL import Image,ImageDraw, ImageFont

import random

origin_image = "./image/test.jpg"
new_image = "./image/new_test.jpg"
color = (255,0,0)

def  numRandom():
	return random.randint(0, 100)

def draw_text_for_image(text, origin_image,fill_color):
	try:
		image = Image.open(origin_image)
		size = image.size
		x = size[0] - 60
		font = ImageFont.truetype("arial.ttf", 36)
		draw = ImageDraw.Draw(image)
		draw.text((x, 15), text, font=font, fill=fill_color)
		image.save(new_image,'jpeg');
	except :
		print "Unable to load image"
	
if __name__ == "__main__":
		text = str(numRandom())
		draw_text_for_image(text,origin_image,color)	


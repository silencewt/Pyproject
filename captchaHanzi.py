# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random


class RandomChar():
    @staticmethod
    def unicode():
        value = random.randint(0x4E00, 0x9FBF)
        return unichr(value)
    @staticmethod
    def gb2312():
        head = random.randint(0xB0,0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0,0xF)
        value = (head << 8) | (body << 4) | tail
        str = "%x" % value
        return str.decode('hex').decode('gb2312')

class CaptchaHanzi():
    def __init__(self, fontColor=(0,0,0), size=(150,60),fontPath='Arial.ttf',
                 bgColor=(255,255,255),fontSize=36 ):
        self.size = size
        self.fontColor=fontColor
        self.bgColor = bgColor
        self.font = ImageFont.truetype(fontPath, fontSize)
        self.fontSize = fontSize
        self.image = Image.new('RGB', size, bgColor)

    def randomRGB(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))


    def rotate(self):
        self.image.rotate(random.randint(0,30),expand=0)

    def drawText(self,pos,text,fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, text, font=self.font, fill=fill)
        del draw
    
    def randomPoint(self):
        (width, height) = self.size
        return (random.randint(0,width), random.randint(0,height))
    
    def randomLine(self, num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0,num):
            draw.line([self.randomPoint(),self.randomPoint()], self.randomRGB())
        del draw
    
    def randomHanzi(self,num):
        gap = 5
        start = 0
        for i in range(0, num):
            char = RandomChar.gb2312()
            x = start + self.fontSize*i +random.randint(0,gap)+ gap*i
            self.drawText((x,random.randint(-5,5)), char, self.randomRGB())
            self.rotate()
        self.randomLine(15)
        
    def save(self,path):
        self.image.save(path, 'jpeg')

if __name__ == '__main__':
    captchaHanzi = CaptchaHanzi(fontColor=(100,211,100))
    captchaHanzi.randomHanzi(4)
    captchaHanzi.save('./image/onehanzi.jpg')
    


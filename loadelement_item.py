import pygame

#遊戲視窗大小&FPS
WIDTH = 1280
HEIGHT = 720
FPS = 30

#圖片
chapter=pygame.image.load("image\chapter.jpg")
#字體
pygame.font.init()
startfont = pygame.font.Font('font/simhei.ttf', 64)
namefont = pygame.font.Font('font/simhei.ttf', 32)
textfont = pygame.font.Font('font/simhei.ttf', 24)

#顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (120,170,230)
BLACK = (0,0,0)
#FFD277
ORANGE = (255,210,119)
#對話框大小
textWIDTH = int(WIDTH*0.8)
textHIGHT = int(HEIGHT*0.25)

#角色名框
charnameW = int(textWIDTH*0.25)
charnameH= int(textHIGHT*0.25)

#文本框
dialogW = int(textWIDTH*0.9)
dialogH = int(textHIGHT-charnameH)




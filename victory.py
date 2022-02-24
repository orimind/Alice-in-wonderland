import pygame
import serial  # 引用pySerial模組
import sys # 引用sys模組
import os # 引用os模組
import loadelement_four as le

from XMLread_one import XMLreader
from pygame.locals import* #pygame.locals導入
import time

class victory():
    def __init__ (self):
        pygame.init()
        pygame.font.init()
        
        self.toucha = pygame.font.SysFont("arial",50) #文字樣式設定
        midwindos = pygame.display.set_mode((1000,700)) #視窗尺寸設定
        background = pygame.Surface(midwindos.get_size()) #呼叫版面
        background = background.convert() #刻劃版面

        #pygame.draw.rect(background,(0,0,0),[800,600,100,100],0) #繪製黑底矩形
        textarea = pygame.Surface((100,60))
        midwindos.blit(background,(0,0))#繪製MIDWINDOS
        midwindos.blit(textarea,(800,600))
        
        pygame.display.update() #更新畫面

        # except KeyboardInterrupt :
        #     ser.close()    # 清除序列通訊物件
        #     print('再見！')
    def run (self):
        pygame.init()
               
        midwindos = pygame.display.set_mode((le.WIDTH,le.HEIGHT)) #視窗尺寸設定
        background = pygame.Surface(midwindos.get_size()) #呼叫版面
        background = background.convert() #刻劃版面
        midwindos.blit(background,(0,0))#繪製MIDWINDOS
        pygame.display.update() #更新畫面
        running = True
        while running: #維持pygame視窗執行
            toucha = pygame.font.SysFont("arial",50) #文字樣式設定 
            touch = toucha.render("VICTORY",True,(255,0,0)) #繪製碰觸次數
            textarea = pygame.Surface((100,60))
            textarea.fill((0,0,0)) #文字繪製位置
            textarea.blit(touch,(100,100)) #文字繪製位置
            midwindos.blit(textarea,(500,400))
            midwindos.blit(background,(0,0)) #繪製MIDWINDOS
            pygame.display.update() #更新畫面 
            time.sleep(2)
            running = False    
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #running = False
        pygame.quit()
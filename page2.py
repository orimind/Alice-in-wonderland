import pygame
import loadelement as le
from XMLread import XMLreader2
from page3 import page3
from button import Button
from button_2 import Button_2
#yolo&cam
#import numpy as np
#import cv2
import time
import random
#from PIL import Image
#from yolo import YOLO

#yolo = YOLO()
#camera=cv2.VideoCapture(0)
page3 = page3()

#進入關卡鏡頭辨識
# class cam():
#     def __init__(self):
#         pygame.font.init()
#         self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
#         self.clock = pygame.time.Clock()
#         #self.camera=cv2.VideoCapture('http://192.168.2.81:8088/video')
#         self.camera=cv2.VideoCapture(0)
#         self.product = []
#     def run(self,Ques):
#         pygame.init()
#         #設定題目
#         Q_text = "請掃描下列物品:"
#         for i in range(len(Ques)):
#             Q_text = Q_text+Ques[i]
#             if i != len(Ques)-1:
#                 Q_text = Q_text+"或是"
#         Q_display = le.startfont.render(Q_text, True, le.BLUE)
#         #self.screen.blit(Q_display, (le.WIDTH//2 - Q_display.get_width()//2, le.HEIGHT*0.25))
#         running = True
#         while running:
#             print (Q_text)
#             # keep loop running at the right speed
#             self.clock.tick(le.FPS)           
#             # 读取某一帧
#             ref,frame=camera.read()
#             # 格式转变，BGRtoRGB
#             frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             # 转变成Image
#             frame = Image.fromarray(np.uint8(frame))
#             # 进行检测
#             frame,product = yolo.detect_image(frame)
#             #轉變為ndarray
#             frame = np.array(frame)
#             #旋轉90度符合pygame顯示方式
#             frame = np.rot90(frame)
#             #array轉化fream格式
#             frame = pygame.surfarray.make_surface(frame)
#             # 將cam繪製到Surface上   
#             #self.screen.blit(pygame.transform.scale(frame, (620,471)), (le.WIDTH//2-frame.get_width()//2, le.HEIGHT*0.4))
#             self.screen.blit(pygame.transform.scale(frame, (596,447)), (166,160))
#             print(product)
#             #進行判斷
#             for a in range(len(product)):
#                 for b in range(len(Ques)):
#                     if product[a] == Ques[b]:
#                         running = False
#             # *after* drawing everything, flip the display
#             pygame.display.update()
#             #pygame.display.flip()     
#             # Process input (events)
#             for event in pygame.event.get():
#                 # check for closing window
#                 if event.type == pygame.QUIT:
#                     pygame.quit()

#主遊戲畫面迴圈
class page2():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
        #self.cam = cam()
        self.order = 0
    def run(self):
        pygame.init()
        #ref,frame=camera.read()
        #介面物件設定
        self.screen.blit(pygame.transform.scale(le.grasslnad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)         
        #解析xml劇情
        xmlread = XMLreader2()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        dialog = le.textfont.render(dialoglist[self.order], True, le.BLACK)
        #立繪和對話框
        if namelist[self.order] == "愛麗絲":
            self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
            self.screen.blit(le.AliceDia.convert_alpha(),(80,450))
        if self.order == 14 or self.order == 15:
            self.screen.blit(pygame.transform.scale(le.RabbitHoney.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
            self.screen.blit(le.RabbitDia.convert_alpha(),(80,450))
        elif namelist[self.order] == "兔子先生":
            self.screen.blit(pygame.transform.scale(le.Rabbit.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
            self.screen.blit(le.RabbitDia.convert_alpha(),(80,450))
        if namelist[self.order] == "貓":
            self.screen.blit(pygame.transform.scale(le.Cat.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
            self.screen.blit(le.CatDia.convert_alpha(),(80,450))
        if namelist[self.order] == "旁白":
            self.screen.blit(le.AsideDia.convert_alpha(), (80,450))
            
        # 建立continue
        self.screen.blit(dialog, (140,520))
        next_page =le.continuefont.render("continue>>", True, (0,0,0))
        self.screen.blit(next_page,(800,600))
        pygame.display.update()
        #載入音樂
        pygame.mixer.music.load('music/Grassland.mp3')
        pygame.mixer.music.play()
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.set_volume(0.1)
        running = True
        while running:
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #滑鼠按下，顯示之後的劇情
                    self.order+=1
                    #切換場景
                    if self.order >= 2 and self.order<=5:
                        self.screen.blit(pygame.transform.scale(le.grasslnad_blurry.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    elif self.order == 6:
                        self.screen.blit(pygame.transform.scale(le.Rfell.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    elif self.order >= 7 and self.order <=12:
                        self.screen.blit(pygame.transform.scale(le.Rfell_blurry.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    elif self.order == 20:
                        self.screen.blit(pygame.transform.scale(le.forkroad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    elif self.order >= 21:
                        self.screen.blit(pygame.transform.scale(le.forkroad_blurry.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    else:
                        self.screen.blit(pygame.transform.scale(le.grasslnad_blurry.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #切換音樂
                    if self.order == 20:
                        #pygame.mixer.music.unload()
                        pygame.mixer.music.load('music/Forkroad.mp3')
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.1)
                    #關卡結束後繼續執行迴圈
                    # #第一段關卡      
                    # if self.order ==12:
                    #     self.screen.blit(pygame.transform.scale(le.scanning1.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #     pygame.display.update()
                    #     Ques = ["handbag","backpack"]
                    #     self.cam.run(Ques)
                    #     pygame.init()
                    #     self.screen.blit(pygame.transform.scale(le.grasslnad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    # #第二段關卡
                    # if self.order ==19:
                    #     self.screen.blit(pygame.transform.scale(le.scanning2.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #     pygame.display.update()
                    #     Ques = ["bottle","cup"]
                    #     self.cam.run(Ques)
                    #     pygame.init()
                    #     self.screen.blit(pygame.transform.scale(le.grasslnad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    # #第三段關卡
                    # if self.order ==35:
                    #     self.screen.blit(pygame.transform.scale(le.scanning3.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #     pygame.display.update()
                    #     Ques = ["book"]
                    #     self.cam.run(Ques)
                    #     pygame.init()
                    #     self.screen.blit(pygame.transform.scale(le.forkroad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #對話框初始化
                    #name = le.namefont.render(namelist[self.order], True, le.BLACK)
                    dialog = le.textfont.render(dialoglist[self.order], True, le.BLACK)
                    print (dialoglist[self.order])
                    print (self.order)
                    

                    #角色立繪&對話框
                    if namelist[self.order] == "愛麗絲":
                        self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.AliceDia.convert_alpha(),(80,450))
                    if self.order == 15:
                        self.screen.blit(pygame.transform.scale(le.RabbitHoney.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                    elif self.order == 16:
                        self.screen.blit(pygame.transform.scale(le.RabbitHoney.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.RabbitDia.convert_alpha(),(80,450))
                    elif namelist[self.order] == "兔子先生":
                        self.screen.blit(pygame.transform.scale(le.Rabbit.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.RabbitDia.convert_alpha(),(80,450))
                    if namelist[self.order] == "貓":
                        self.screen.blit(pygame.transform.scale(le.Cat.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.CatDia.convert_alpha(),(80,450))
                    if namelist[self.order] == "旁白":
                        self.screen.blit(le.AsideDia.convert_alpha(), (80,450))

                    #將對話繪製到畫面上
                    #建立continue
                    if self.order != 6 and self.order != 15 and self.order != 20: 
                        self.screen.blit(dialog, (140,520))
                        next_page =le.continuefont.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))
                    
                    pygame.display.update()
                #判斷章節是否完成
                if self.order == len(namelist)-1:
                    self.order = 0
                    #running =False
                    #page3.run()
                    #建構選項
                    #返回鍵
                    back_button = Button_2('BACK',le.WHITE, 900, 620, centered_x=False)
                    back_button.display()
                    #繼續鍵
                    continue_button = Button_2('NEXT',le.WHITE, 800, 620, centered_x=False)
                    continue_button.display()
                    pygame.display.update()
                    while True:
                        # keep loop running at the right speed
                        self.clock.tick(le.FPS)
                        #滑鼠移到按鈕上按鈕變色
                        if back_button.check_click(pygame.mouse.get_pos()):
                            back_button = Button_2('BACK', le.RED, 900,620, centered_x=False)
                        else:
                            back_button = Button_2('BACK', le.WHITE, 900, 620, centered_x=False)

                        if continue_button.check_click(pygame.mouse.get_pos()):
                            continue_button = Button_2('NEXT', le.RED, 800, 620, centered_x=False)
                        else:
                            continue_button = Button_2('NEXT', le.WHITE, 800, 620, centered_x=False)

                        back_button.display()
                        continue_button.display()
                        pygame.display.update()

                        for event in pygame.event.get():
                            # check for closing window
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        if pygame.mouse.get_pressed()[0]:
                            if back_button.check_click(pygame.mouse.get_pos()):
                                running =False
                                break
                            if continue_button.check_click(pygame.mouse.get_pos()):
                                page3.run()
                                running =False
                                break
                #當音樂結束時，重播音樂
                if int(pygame.mixer.music.get_busy()) == 0:
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.play()
            # *after* drawing everything, flip the display
            pygame.init()
            pygame.display.update()
            #pygame.display.flip()     
            # Process input (events)

import pygame
import loadelement as le
from XMLread import XMLreader3
#import numpy as np
import time
# 錄音按鈕
from button import Button
from button_2 import Button_2
from button_function import BFButton
# 抽題&答案驗證
#from chatbot import stt
#from pygame.locals import *
from page4 import page4
page4 = page4()

# 語音辨識答案
#ans = ""

class page3():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
        #self.cam = cam()
        #文本框
        self.clock = pygame.time.Clock()
        self.order = 0

    def run(self):
        pygame.init()
        #ref,frame=camera.read()
        #介面物件設定
        self.screen.blit(pygame.transform.scale(le.teaparty.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)         
        #解析xml劇情
        xmlread = XMLreader3()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        # #繪製介面
        pygame.display.update()
        #載入音樂
        pygame.mixer.music.load('music/Teaparty.mp3')
        pygame.mixer.music.play()
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.set_volume(0.1)
        # 錄音按鈕
        """ def start_record(btn):
            # "答對了!恭喜你" || "答錯了，請繼續加油~"
            global ans
            ans = stt.input()
            if self.order == 6:
                if (ans == "答對了!恭喜你"):
                    self.order = 10
            elif self.order == 43:
                if (ans == "答對了!恭喜你"):
                    self.order = 43
                # elif(ans == "答錯了，請繼續加油~"):
                else:
                    print("fallllllll")
                    dialoglist[42] = "猜錯了~妳得繼續猜下去喔"
                    self.order = 41

            self.screen.blit(pygame.transform.scale(le.teaparty2.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
            dialog = le.textfont.render(ans, True, le.BLACK)
            # self.textarea.blit(self.dialogarea,(int(le.textWIDTH*0.025),le.charnameH))
            # self.screen.blit(self.textarea, (100, int(le.HEIGHT*0.7)))
            self.screen.blit(le.AsideDia.convert_alpha(), (80,450)) 
            self.screen.blit(dialog, (140,520))
            pygame.display.update() """
        #MicButton = BFButton(self.screen, (900,400,160,40),text='start',click=start_record)

        running = True
        while running:
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            for event in pygame.event.get():
                # 監測按鈕事件
                #MicButton.update(event)
                # check for closing window
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #滑鼠按下，顯示之後的劇情
                    self.order+=1
                    self.screen.blit(pygame.transform.scale(le.teaparty.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    #切換場景
                    if self.order >= 12:
                        self.screen.blit(pygame.transform.scale(le.teaparty2.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    # elif self.order == 14:
                    #     self.screen.blit(pygame.transform.scale(le.honey.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    # elif self.order > 14:
                    #     self.screen.blit(pygame.transform.scale(le.forkroad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    # else:
                    #     self.screen.blit(pygame.transform.scale(le.grasslnad.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))

                    # 關卡章節
                    """ if self.order ==5:
                        dialoglist[5] = stt.pick()
                        MicButton.draw()
                    elif self.order ==28:
                        dialoglist[28] = stt.pick()
                        MicButton.draw()
                    elif self.order ==42:
                        dialoglist[42] = stt.pick()
                        MicButton.draw() """

                    #切換音樂
                    if self.order == 30:
                        #pygame.mixer.music.unload()
                        pygame.mixer.music.load('music/Teaparty2.mp3')
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.1)

                    #對話框初始化
                    dialog = le.textfont.render(dialoglist[self.order], True, le.BLACK)
                    print (dialoglist[self.order])
                    print (self.order)

                    #角色立繪
                    if namelist[self.order] == "愛麗絲":
                        self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.AliceDia.convert_alpha(),(80,450))
                    if namelist[self.order] == "三月兔":
                        self.screen.blit(pygame.transform.scale(le.TeaRabbit.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.TeaRabbitDia.convert_alpha(),(80,450))
                    if namelist[self.order] == "瘋帽子":
                        self.screen.blit(pygame.transform.scale(le.Hat.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.HatDia.convert_alpha(),(80,450))
                    if namelist[self.order] == "旁白":
                        self.screen.blit(le.AsideDia.convert_alpha(), (80,450))
                    if namelist[self.order] == "猜謎關卡":
                        self.screen.blit(le.RiddleDia.convert_alpha(), (80,450))  
                        

                    # 建立continue
                    # 劇情留白
                    if self.order != 12: 
                        self.screen.blit(dialog, (140,520))
                        next_page =le.continuefont.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))

                #判斷章節是否完成
                if self.order == len(namelist)-1:
                    self.order = -1
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
                            back_button = Button_2('BACK', le.RED, 900, 620, centered_x=False)
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
                                page4.run()
                                running = False
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

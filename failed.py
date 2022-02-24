import pygame
import loadelement_four as le
from XMLread_fail import XMLreader
from button import Button
from button_function import BFButton
from button_2 import Button_2
from pygame.color import THECOLORS
import random
count =0
class failed():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
        #對話框
        self.textarea = pygame.Surface((le.textWIDTH,le.textHIGHT),pygame.SRCALPHA)
        #角色名
        self.charename = pygame.Surface((le.charnameW,le.charnameH),pygame.SRCALPHA)
        #文本框
        self.dialogarea = pygame.Surface((le.dialogW,le.dialogH),pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
    def run(self):
        pygame.init()      
        #介面物件設定
        self.screen.blit(pygame.transform.scale(le.badend.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)         
        self.textarea.fill(le.BLUE)
        self.charename.fill(le.ORANGE)
        self.dialogarea.fill(le.BLUE)
        pygame.mixer.music.load('music/處刑.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        #解析xml劇情
        xmlread = XMLreader()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        #繪製介面
        order = 0
        another_talk=pygame.image.load('talk/another.png')
        another_talk.convert_alpha()
        self.screen.blit(another_talk, (80,450))
        name = le.namefont.render(namelist[order], True, le.WHITE)
        dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
        self.screen.blit(dialog, (143,520))

        font = pygame.font.SysFont("simhei", 24)
        next_page =font.render("continue>>", True, (0,0,0))
        self.screen.blit(next_page,(800,600))
        pygame.display.update()
        while True:
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    order = order+1
                    another_talk=pygame.image.load('talk/another.png')
                    another_talk.convert_alpha()
                    self.screen.blit(another_talk, (80,450))
                    name = le.namefont.render(namelist[order], True, le.WHITE)
                    dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                    self.screen.blit(dialog, (143,520))
                    if order <2:
                        font = pygame.font.SysFont("simhei", 24)
                        next_page =font.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))
                    else :
                        font = pygame.font.SysFont("simhei", 24)
                        next_page =font.render("BAD END", True, (255,0,0))
                        self.screen.blit(next_page,(800,600))
                        back_button = Button_2('BACK',le.WHITE, 900, 620, centered_x=False)
                        back_button.display()
                        pygame.display.update()
                        while True:
                        # keep loop running at the right speed
                            self.clock.tick(le.FPS)
                        #滑鼠移到按鈕上按鈕變色
                            if back_button.check_click(pygame.mouse.get_pos()):
                                back_button = Button_2('BACK', le.RED, 900,620, centered_x=False)
                            else:
                                back_button = Button_2('BACK', le.WHITE, 900, 620, centered_x=False)
                            back_button.display()
                            pygame.display.update()
                            for event in pygame.event.get():
                                # check for closing window
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            if pygame.mouse.get_pressed()[0]:
                                if back_button.check_click(pygame.mouse.get_pos()):
                                    running =False
                                    break
            pygame.display.update()
        pygame.quit()

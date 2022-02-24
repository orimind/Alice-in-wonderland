import pygame
import loadelement as le
from XMLread_sucess import XMLreader2
from button import Button
from button_2 import Button_2
from button_function import BFButton
from pygame.color import THECOLORS
import random
count =0
class success():
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
        self.screen.blit(pygame.transform.scale(le.goodend.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)         
        self.textarea.fill(le.BLUE)
        self.charename.fill(le.ORANGE)
        self.dialogarea.fill(le.BLUE)

        pygame.mixer.music.load('music/王子.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        #解析xml劇情
        xmlread = XMLreader2()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        #繪製介面
        order = 0
        another_talk=pygame.image.load('talk/another.png')
        another_talk.convert_alpha()
        self.screen.blit(another_talk, (80,450))
        dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
        self.screen.blit(dialog, (143,520))

        font = pygame.font.SysFont("simhei", 24)
        next_page =font.render("continue>>", True, (0,0,0))
        self.screen.blit(next_page,(800,600))
        pygame.display.update()
        running =True
        while running:
            # keep loop running at the right speed
            # check for closing window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("123")
                    if order<6:
                        order = order+1                     
                    self.screen.blit(pygame.transform.scale(le.goodend.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    if namelist[order] == "愛麗絲" or namelist[order] == "愛麗絲(變聲)":
                    # 立繪
                        self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(),(300,500)),(850, 50))
                        another_talk=pygame.image.load('talk/alice.png')
                        another_talk.convert_alpha()
                        self.screen.blit(another_talk, (80,450))
                    if namelist[order] == "旁白":
                        # 立繪
                        another_talk=pygame.image.load('talk/another.png')
                        another_talk.convert_alpha()
                        self.screen.blit(another_talk, (80,450))
                    if namelist[order] == "王子":
                            # 立繪
                        self.screen.blit(pygame.transform.scale(le.prince.convert_alpha(),(300,500)),(850, 50))
                        another_talk=pygame.image.load('talk/王子.png')
                        another_talk.convert_alpha()
                        self.screen.blit(another_talk, (80,450))
                    dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                    self.screen.blit(dialog, (143,520))
                    if order <6:
                        font = pygame.font.SysFont("simhei", 24)
                        next_page =font.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))
                    else:
                        self.screen.blit(pygame.transform.scale(le.end.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                        self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(),(300,500)),(850, 50))
                        another_talk=pygame.image.load('talk/alice.png')
                        another_talk.convert_alpha()
                        self.screen.blit(another_talk, (80,450))
                        font = pygame.font.SysFont("simhei", 24)
                        next_page =font.render("GOOD END", True, (255,0,0))
                        self.screen.blit(next_page,(800,600))
                        self.screen.blit(dialog, (143,520))
                        back_button = Button_2('BACK',le.WHITE, 900, 620, centered_x=False)
                        back_button.display()
                        while True:
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

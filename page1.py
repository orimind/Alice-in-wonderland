import pygame
import loadelement as le
from XMLread_one import XMLreader
#from page1_1 import page1_1
from button import Button
from button_2 import Button_2
#page1_1=page1_1()
pygame.mixer.init()
class page1():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
    def run(self):
        pygame.init()
        #介面物件設定
        self.screen.blit(pygame.transform.scale(le.begin.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)         
        #解析xml劇情
        xmlread = XMLreader()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        #繪製介面
        order = 0
        dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
        
        
        pygame.display.update()

        #載入音樂
        pygame.mixer.music.load('music/樹林.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
        running = True
        while running:
            if order == 12:
                    running = False
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #滑鼠按下，顯示之後的劇情
                    order+=1
                     #切換場景
                    if order == 4:
                        self.screen.blit(pygame.transform.scale(le.fall.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                        pygame.mixer.music.stop()
                    elif order == 5:
                        self.screen.blit(pygame.transform.scale(le.door.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                    
                    #切換音樂
                    if order == 5:
                        #pygame.mixer.music.unload()
                        pygame.mixer.music.load('music/大廳.mp3')
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.2)
                    
                    

                    #角色立繪&對話框
                    if namelist[order] == "愛麗絲":
                        self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(), (480, 640)), (le.WIDTH-540, le.HEIGHT-640))
                        self.screen.blit(le.AliceDia.convert_alpha(),(80,450))
                    if namelist[order] == "門":
                        self.screen.blit(le.DoorDia.convert_alpha(),(80,450))
                    if namelist[order] == "旁白":
                        self.screen.blit(le.AsideDia.convert_alpha(), (80,450))


                    dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                    #將對話繪製到畫面上
                    #建立continue
                    if order != 0 and order != 4 and order != 5 and order != 12:
                        self.screen.blit(dialog, (140,520))
                        next_page =le.continuefont.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))
                    
                    pygame.display.update()
                #當音樂結束時，重播音樂
                if int(pygame.mixer.music.get_busy()) == 0:
                   if order != 4 :
                        pygame.mixer.music.rewind()
                        pygame.mixer.music.play()
                # *after* drawing everything, flip the display
                pygame.display.update()
                """ if(order==12):
                    page1_1.run()
                    running=False
                    break """
            # for event in pygame.event.get():
            #             # check for closing window
            #         if event.type == pygame.QUIT:
            #             pygame.quit()
            #         if pygame.mouse.get_pressed()[0]:
            #             if back_button.check_click(pygame.mouse.get_pos()):
            #                 running =False
            #                 break
                #pygame.display.flip()     
                # Process input (events)


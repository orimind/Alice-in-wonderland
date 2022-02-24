import pygame
import loadelement_item as le
from page1 import page1
from page2 import page2
from page3 import page3
from page4 import page4
from button import Button
page1 = page1()
page2 = page2()
page3 = page3()
page4 = page4()
pygame.init()
class item():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
    def run(self):
        pygame.init()
        #介面物件設定
        
        self.screen.blit(pygame.transform.scale(le.chapter.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)
        # 選單按鈕
        chapter_one = Button('CHAPTER.1',le.WHITE, 943, 120, centered_x=False)
        chapter_one.display()
        chapter_two = Button('CHAPTER.2',le.WHITE, 943, 220, centered_x=False)
        chapter_two.display()
        chapter_three = Button('CHAPTER.3',le.WHITE, 943, 320, centered_x=False)
        chapter_three.display()
        chapter_four = Button('CHAPTER.4',le.WHITE, 943, 420, centered_x=False)
        chapter_four.display()
        #返回鍵
        back_button = Button('BACK',le.WHITE, 1000, 520, centered_x=False)
        back_button.display()
        #解析xml劇情
        #繪製介面
        pygame.display.update()
        while True:
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            # 返回
            if back_button.check_click(pygame.mouse.get_pos()):
                back_button = Button('BACK', le.RED, 1000, 520, centered_x=False)
            else:
                back_button = Button('BACK', le.WHITE, 1000, 520, centered_x=False)
            back_button.display()
            
            # 選單
            if chapter_one.check_click(pygame.mouse.get_pos()):
                chapter_one = Button('CHAPTER.1', le.RED, 943, 120, centered_x=False)
            else:
                chapter_one = Button('CHAPTER.1', le.WHITE, 943, 120, centered_x=False)
            chapter_one.display()

            if chapter_two.check_click(pygame.mouse.get_pos()):
                chapter_two = Button('CHAPTER.2', le.RED, 943, 220, centered_x=False)
            else:
                chapter_two = Button('CHAPTER.2', le.WHITE, 943, 220, centered_x=False)
            chapter_two.display()

            if chapter_three.check_click(pygame.mouse.get_pos()):
                chapter_three = Button('CHAPTER.3', le.RED, 943, 320, centered_x=False)
            else:
                chapter_three = Button('CHAPTER.3', le.WHITE, 943, 320, centered_x=False)
            chapter_three.display()

            if chapter_four.check_click(pygame.mouse.get_pos()):
                chapter_four = Button('CHAPTER.4', le.RED, 943, 420, centered_x=False)
            else:
                chapter_four = Button('CHAPTER.4', le.WHITE, 943, 420, centered_x=False)
            chapter_four.display()
            pygame.display.update()
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    pygame.quit()  
            if pygame.mouse.get_pressed()[0]:
                if chapter_one.check_click(pygame.mouse.get_pos()):
                    page1.run()
                    item.run(self)
                if chapter_two.check_click(pygame.mouse.get_pos()):
                    page2.run()
                    item.run(self)
                if chapter_three.check_click(pygame.mouse.get_pos()):
                    page3.run()
                    item.run(self)
                if chapter_four.check_click(pygame.mouse.get_pos()):
                    page4.run()
                    item.run(self)
                if back_button.check_click(pygame.mouse.get_pos()):
                    break
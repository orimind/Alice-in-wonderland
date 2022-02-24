import pygame
import loadelement_game as le
from button import Button
from item import item
item = item()
#初始化及創建遊戲視窗
pygame.init()
#全螢幕
# screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT),pygame.FULLSCREEN)
class game():
    def run():
        # screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT),pygame.FULLSCREEN)
        screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        clock = pygame.time.Clock()

        #繪製元件
        screen.blit(pygame.transform.scale(le.cover.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))

        #載入音樂
        pygame.mixer.music.load('music/封面.mp3')
        pygame.mixer.music.play()
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.set_volume(0.1)

        play_button = Button('START',le.WHITE, 935, 393, centered_x=False)
        exit_button = Button('EXIT',le.WHITE, 953, 492, centered_x=False)

        play_button.display()
        exit_button.display()

        pygame.display.update()
        # Game loop
        running = True
        while running:
            # keep loop running at the right speed
            clock.tick(le.FPS)
            #按鈕偵測滑鼠位置
            if play_button.check_click(pygame.mouse.get_pos()):
                play_button = Button('START', le.RED, 935, 393, centered_x=False)
            else:
                play_button = Button('START', le.WHITE, 935, 393, centered_x=False)

            if exit_button.check_click(pygame.mouse.get_pos()):
                exit_button = Button('EXIT', le.RED, 953, 492, centered_x=False)
            else:
                exit_button = Button('EXIT', le.WHITE, 953, 492, centered_x=False)

            play_button.display()
            exit_button.display()
            pygame.display.update()

            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False

            if pygame.mouse.get_pressed()[0]:
                if play_button.check_click(pygame.mouse.get_pos()):
                    item.run()
                    game.run()
                if exit_button.check_click(pygame.mouse.get_pos()):
                    break

            #當音樂結束時，重播音樂
                if int(pygame.mixer.music.get_busy()) == 0:
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.play()
            # Draw / render
            # *after* drawing everything, flip the display
            
            pygame.display.update()
            #pygame.display.flip()

        pygame.quit()
game.run()
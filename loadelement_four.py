import pygame

#遊戲視窗大小&FPS
WIDTH = 1280
HEIGHT = 720
FPS = 30

#圖片
# 花園
paint = pygame.image.load("image\paint.jpg")
cover=pygame.image.load("image_four\cover.jpg")
# 追逐
chase = pygame.image.load("image_four\Flee.jpg")
Alice=pygame.image.load("image_four\ALICE.png")
queen=pygame.image.load("image_four\Queen of Hearts.png")
Rabbit=pygame.image.load("image_four\Mr. Rabbit.png")
soldier=pygame.image.load("image_four\Soldier.png")
prince = pygame.image.load("image\Prince of spades.png")

# 失敗結局
badend=pygame.image.load("image_four\kill.jpg")
# 好結局
goodend = pygame.image.load("image\Curse lifted.jpg")
end = pygame.image.load("image\end.jpg")
#字體
pygame.font.init()
startfont = pygame.font.Font('font/清松手寫體3.ttf', 64)
namefont = pygame.font.Font('font/清松手寫體3.ttf', 32)
textfont = pygame.font.Font('font/清松手寫體3.ttf', 30)

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




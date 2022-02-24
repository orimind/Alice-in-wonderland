import pygame

#遊戲視窗大小&FPS
WIDTH = 1280
HEIGHT = 720
FPS = 30

#圖片

#封面
cover=pygame.image.load("image\start.jpg")
chapter=pygame.image.load("image\chapter.jpg")
# 第一章
begin=pygame.image.load("image\Beginning.jpg")
fall = pygame.image.load("image\Fall.jpg")
door = pygame.image.load("image\many door.jpg")
#第二章
grasslnad=pygame.image.load("image\Rabbit is far away.jpg")
Rfell=pygame.image.load("image\Rabbit fell down.jpg")
forkroad=pygame.image.load("image\Ask for directions.jpg")
grasslnad_blurry=pygame.image.load("image\Blurry\Rabbit is far away_blurry.jpg")
Rfell_blurry=pygame.image.load("image\Blurry\Rabbit fell down_blurry.jpg")
forkroad_blurry=pygame.image.load("image\Blurry\Ask for directions_blurry.jpg")
scanning1=pygame.image.load("image\scanning1.jpg")
scanning2=pygame.image.load("image\scanning2.jpg")
scanning3=pygame.image.load("image\scanning3.jpg")
#第三章
teaparty=pygame.image.load("image\Tea party(no alice).jpg")
teaparty2=pygame.image.load("image\Tea party.jpg")
# 第四章
paint=pygame.image.load("image\paint.jpg")
chase =pygame.image.load("image\chase.jpg")
# 失敗結局
badend=pygame.image.load("image_four\kill.jpg")
# 好結局
goodend = pygame.image.load("image\Curse lifted.jpg")
end = pygame.image.load("image\end.jpg")
#腳色立繪
#愛麗絲
Alice=pygame.image.load("image\Alice.png")
#兔子先生
Rabbit=pygame.image.load("image\Mr. Rabbit.png")
RabbitHoney=pygame.image.load("image\Mr. Rabbit(honey).png")
#柴俊貓
Cat=pygame.image.load("image\Cheshire Cat.png")    
#三月兔
TeaRabbit=pygame.image.load("image\March Hare.png")
#瘋帽子
Hat=pygame.image.load("image\Mad Hatter.png")
# 女皇
queen=pygame.image.load("image\Queen of Hearts.png")
# 士兵
soldier=pygame.image.load("image\Soldier.png")
# 王子
prince = pygame.image.load("image\Prince of spades.png")
#字體
pygame.font.init()
startfont = pygame.font.Font('font/simhei.ttf', 64)
#namefont = pygame.font.Font('font/simhei.ttf', 40)
textfont = pygame.font.Font('font/清松手寫體3.ttf', 30)
continuefont = pygame.font.Font('font/清松手寫體3.ttf', 24)

#顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (120,170,230)
BLACK = (0,0,0)
#FFD277
ORANGE = (255,210,119)
#對話框大小
textWIDTH = 1050
textHIGHT = 234

#角色名框
charnameW = int(textWIDTH*0.25)
charnameH= int(textHIGHT*0.25)

#文本框
dialogW = int(textWIDTH*0.9)
dialogH = int(textHIGHT-charnameH)

#對話框
AliceDia=pygame.image.load("image\chat\對話框-愛莉絲.png")
AsideDia=pygame.image.load("image\chat\對話框-旁白.png")
RabbitDia=pygame.image.load("image\chat\對話框-兔子先生.png")
CatDia=pygame.image.load("image\chat\對話框-柴郡貓.png")
HatDia=pygame.image.load("image\chat\對話框-瘋帽子.png")
TeaRabbitDia=pygame.image.load("image\chat\對話框-三月兔.png")
DoorDia=pygame.image.load("image\chat\對話框-大門.png")
RiddleDia =pygame.image.load("image\chat\對話框-none.png")



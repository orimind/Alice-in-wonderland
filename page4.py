import pygame
import loadelement as le
from XMLread_four import XMLreader
from button import Button
from button_function import BFButton
from pygame.color import THECOLORS
from failed import failed
from success import success
import random
# 題目答對答錯記數
count_error =0
count_correct = 0
# 失敗關卡
failed = failed()
success = success()
order=0
json_t=""

class page4():
    def __init__(self):   
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((le.WIDTH, le.HEIGHT))
        self.clock = pygame.time.Clock()
    def run(self):
        pygame.init()
        #介面物件設定
        self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
        self.clock.tick(le.FPS)
        global order
        #解析xml劇情
        xmlread = XMLreader()
        pyorder,namelist,dialoglist = [],[],[]
        pyorder = xmlread.get_order(pyorder)
        namelist,dialoglist = xmlread.output(pyorder)
        pygame.mixer.music.load('music/flower.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        

        """ import json
        # 從json導入文字題目
        with open("word.json",'r',encoding="utf-8") as g:
            result_word = json.load(g)
        print(result_word)
        # 從json導入性別題目
        with open("sex.json",'r',encoding="utf-8") as g:
            result_sex = json.load(g)
        print(result_sex)
        # 從json導入情緒題目
        with open("emotion.json",'r',encoding="utf-8") as g:
            result_emotion = json.load(g)
        print(result_emotion)


        # 聲音輸入
        import wave 
        from pyaudio import PyAudio,paInt16
        # 初始化聲音設定
        framerate=8000
        NUM_SAMPLES=2000
        channels=1
        sampwidth=2
        TIME=2
        # 音檔儲存
        def save_wave_file(filename,data):
            wf = wave.open(filename,"wb")
            wf.setnchannels(channels)
            wf.setsampwidth(sampwidth)
            wf.setframerate(framerate)
            wf.writeframes(b''.join(data))
            wf.close()
        # 對聲音的紀錄
        import keyboard
        import pyaudio
        def my_record():
            print('record')
            pa= PyAudio()
            stream=pa.open(format=paInt16,channels=1,rate=framerate,input=True)
            my_buf=[]
            count=0
            while count<TIME*20:
                string_audio_data = stream.read(NUM_SAMPLES)
                my_buf.append(string_audio_data)
                if keyboard.is_pressed('q'):
                    print('123')
                    count=100000
                count+=1
                print('.')
            save_wave_file("text.wav",my_buf)
            print("save_OK")
            stream.close
            return
        # 聲音辨識
        import speech_recognition as sr
        # 答對次數
        def recog_word(text):
            global count_correct
            global count_error
            global json_t
            print(text)
            print(json_t)
            text=text
            print('recog')
            r = sr.Recognizer()                        #預設辨識英文
            with sr.WavFile("text.wav") as source:  #讀取wav檔
                audio = r.record(source)
            print(r.recognize_google(audio,language="zh-TW"))
            ans = r.recognize_google(audio,language="zh-TW")
            #  測試
            if json_t=="2":
                print("123")
                count_correct=0
                json_t=json_t+1
            if ans==text:
                count_correct=count_correct+1
                print("correct")
                return "correct"
            else:
                count_error=count_error+1
                print("error")
                if count_error==1:
                    pygame.draw.circle(self.screen,THECOLORS["red"],[100,100],30,0)
                    pygame.draw.circle(self.screen,THECOLORS["black"],[100,100],30,5)
                if count_error==2:
                    pygame.draw.circle(self.screen,THECOLORS["red"],[160,100],30,0)
                    pygame.draw.circle(self.screen,THECOLORS["black"],[160,100],30,5)
                if count_error==3:
                    pygame.draw.circle(self.screen,THECOLORS["red"],[220,100],30,0)
                    pygame.draw.circle(self.screen,THECOLORS["black"],[220,100],30,5)
                    failed.run()
                return "error"

        # 按鈕觸發
        global order_t
        def do_click1(btn):
            my_record()
            # 關卡1
            if recog_word(result_word[json_t]) =="correct":
                pygame.display.set_caption('i click %s,ctl id is %s' % (btn._text,btn.ctl_id))
                btn.text = 'correct'
                font = pygame.font.SysFont("simhei", 24)
                next_page =font.render("good", True, (255,0,0))
                self.screen.blit(next_page,(800,600))
            else :
                pygame.display.set_caption('i click %s,ctl id is %s' % (btn._text,btn.ctl_id))
                btn.text = 'error'
                font = pygame.font.SysFont("simhei", 24)
                next_page =font.render("failed", True, (255,0,0))
                self.screen.blit(next_page,(800,600))
            button1.draw()
        topic=0
        pygame.display.update()
        # 錄音按鈕
        button1 = BFButton(self.screen, (900,400,160,40),text='start',click=do_click1)
        order_t =0 #紀錄當前order
        json_t =0 #建立讓order題目對應json """
        order=0
        running=True
        while running:
            # keep loop running at the right speed
            self.clock.tick(le.FPS)
            for event in pygame.event.get():
                # check for closing window
                #button1.update(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position=pygame.mouse.get_pos()  
                    if order==0:
                        # 第一頁
                        another_talk=pygame.image.load('talk/another.png')
                        another_talk.convert_alpha()
                        self.screen.blit(another_talk, (80,450))
                        name = le.textfont.render(namelist[order], True, le.WHITE)
                        dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                        self.screen.blit(dialog, (143,520))

                        font = pygame.font.SysFont("simhei", 24)
                        next_page =font.render("continue>>", True, (0,0,0))
                        self.screen.blit(next_page,(800,600))

                    if position[0]>790 and position[0]<930 and position[1]>580 and position[1]<630:
                        order=order+1
                        print(order)
                        if order <15:
                            self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                            if namelist[order] == "愛麗絲":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/alice.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))                   
                            if namelist[order] == "女皇":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.queen.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/queen.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))                            
                            if namelist[order] == "兔子先生":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.Rabbit.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/rabbit.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "士兵":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.soldier.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/Solider.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "沒漆好油漆的士兵":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.soldier.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/Solider.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "旁白":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                                another_talk=pygame.image.load('talk/another.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))

                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            # 建立continue
                            self.screen.blit(dialog, (140,520))

                            font = pygame.font.SysFont("simhei", 24)
                            next_page =font.render("continue>>", True, (0,0,0))
                            self.screen.blit(next_page,(800,600))
                        if order==15:
                            self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                            # 關卡1
                            print("關卡1")
                            # 導入對話框
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            
                            # 角色名稱與對話
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (143,520))
                            print(namelist[order])
                            # 建立開始
                            font = pygame.font.SysFont("simhei", 24)
                            next_page =font.render("start", True, (0,0,0))
                            self.screen.blit(next_page,(800,600))
                            
                        if order==16 :
                            # 題目顯示
                            json_t="1"
                            self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                            print("題目")
                            print("題目文字")
                            #print(result_word[json_t])
                            # 導入對話框
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            # 角色名稱與對話
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (143,520))
                            # 建立continue
                            print(namelist[order])
                            pygame.draw.circle(self.screen,THECOLORS["white"],[100,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[100,100],30,5)
                            pygame.draw.circle(self.screen,THECOLORS["white"],[160,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[160,100],30,5)
                            pygame.draw.circle(self.screen,THECOLORS["white"],[220,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[220,100],30,5)
                            #button1.draw()
                            # while True:
                        if order ==17:
                            print("題目")
                            print("題目文字")
                            json_t = "2"
                            #print(result_word[json_t])
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            # 角色名稱與對話
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (143,520))
                            # 建立continue
                            print(namelist[order])
                            #button1.draw()

                        if order >17 and order<37:
                            # 第二幕
                            self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                            if namelist[order] == "愛麗絲" or namelist[order] == "愛麗絲(變聲)":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.Alice.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/alice.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))                   
                            if namelist[order] == "女皇":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.queen.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/queen.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))                            
                            if namelist[order] == "兔子先生":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.Rabbit.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/rabbit.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "士兵":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.soldier.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/Solider.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "沒漆好油漆的士兵":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.soldier.convert_alpha(),(300,500)),(850, 50))
                                another_talk=pygame.image.load('talk/Solider.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))
                            if namelist[order] == "旁白":
                                # 立繪
                                self.screen.blit(pygame.transform.scale(le.paint.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                                another_talk=pygame.image.load('talk/another.png')
                                another_talk.convert_alpha()
                                self.screen.blit(another_talk, (80,450))

                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            # 建立continue
                            self.screen.blit(dialog, (140,520))
                            font = pygame.font.SysFont("simhei", 24)
                            next_page =font.render("continue>>", True, (0,0,0))
                            self.screen.blit(next_page,(800,600))
                        if order == 37:
                            pygame.mixer.music.load('music/追逐.mp3')
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(0.1)
                            # 關卡2
                            self.screen.blit(pygame.transform.scale(le.chase.convert(), (le.WIDTH, le.HEIGHT)), (0, 0))
                            # 關卡1
                            print("關卡2")
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            # 角色名稱
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (140,520))
                            font = pygame.font.SysFont("simhei", 24)
                            next_page =font.render("start", True, (0,0,0))
                            self.screen.blit(next_page,(800,600))
                            
                        if order==38 :
                            # 題目顯示
                            print("題目1")
                            print("題目文字")
                            json_t = "3"
                            #print(result_word[json_t])
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            # 角色名稱
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (140,520))
                            pygame.draw.circle(self.screen,THECOLORS["white"],[100,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[100,100],30,5)
                            pygame.draw.circle(self.screen,THECOLORS["white"],[160,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[160,100],30,5)
                            pygame.draw.circle(self.screen,THECOLORS["white"],[220,100],30,0)
                            pygame.draw.circle(self.screen,THECOLORS["black"],[220,100],30,5)
                            #button1.draw()
                        if order==39 :
                            # 題目顯示
                            print("題目2")
                            print("題目文字")
                            json_t = "4"
                            #print(result_word[json_t])
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            # 角色名稱
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (140,520))
                            print(namelist[order])
                            #button1.draw()
                        if order==40 :
                            # 題目顯示
                            order_t=1
                            print("題目3")
                            print("題目文字")
                            json_t = "5"
                            #print(result_word[json_t])
                            another_talk=pygame.image.load('talk/question.png')
                            another_talk.convert_alpha()
                            self.screen.blit(another_talk, (80,450))
                            # 角色名稱
                            name = le.textfont.render(namelist[order], True, le.BLACK)
                            dialog = le.textfont.render(dialoglist[order], True, le.BLACK)
                            self.screen.blit(name, (170,460))
                            self.screen.blit(dialog, (140,520))
                            print(namelist[order])
                            #button1.draw()
                        if order ==41:
                            success.run()
                            running=False
                            break
            pygame.display.update()
            #pygame.display.flip()     
            # Process input (events)
        

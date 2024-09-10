import pygame
import random
import string

class Monkey:
    def __init__(self):
        #init pygame
        pygame.init()
        #create screen
        self.xScreen,self.yScreen = 910,607
        linkBg="./images/bg.jpg"
        self.linkicon="./images/icon.jpg"
        self.linkImgMonkey ="./images/monkey.png"
        self.screen=pygame.display.set_mode((self.xScreen,self.yScreen))
        pygame.display.set_caption("Monkey")
        self.background=pygame.image.load(linkBg)
        self.monkey=pygame.image.load(self.linkicon)
        pygame.display.set_icon(self.monkey)
        self.gamerunning=True

         # --------------------------------------------------------
        self.xSizeMonkey = 80  # Chiều cao ảnh Monkey
        self.ySizeMonkey = 60  # Chiều rộng ảnh Monkey
        self.xMonkey = self.xScreen/2 - 50  # Vị trí bạn đầu của Monkey
        self.yMonkey = self.yScreen-150
        self.MonkeyPos = (self.xMonkey,self.yMonkey)
        self.MonkeyMove = 30  # Tốc độ di chuyen Monkey
        # ------------------------------

        self.xBanana = random.randint(0,self.xScreen-70) # khởi tạo banana đầu tiên
        self.yBanana = 0
        self.BananaPos = (self.xBanana,self.yBanana)
        self.xSizeBanana = 50  # Chiều rộng banana
        self.ySizeBanana = 40
        self.VBanana = 4  # Tốc độ roi
        self.bananaChange = 0
        self.SpawnBanana = True

        self.scores = 0
        self.hscores = 0
        self.checkLost = False
        self.lives = 3

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(
            PlanesImg, (xImg, yImg))  # change size image
        self.screen.blit(PlanesImg, (xLocal, yLocal))

    def show_score(self, x, y, scores, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))
    
    def show_hscore(self, x, y, hscores, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        hscore = font.render(str(hscores), True, (255, 255, 255))
        self.screen.blit(hscore, (x, y))
    
    def show_lives(self, x, y, lives, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        live = font.render(str(lives), True, (255, 255, 255))
        self.screen.blit(live, (x, y))

    def banana(self):
        self.image_draw("./images/banana1.png", self.xBanana,self.yBanana,
                         self.xSizeBanana, self.ySizeBanana)

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamerunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.xMonkey += self.MonkeyMove
                    if event.key == pygame.K_LEFT:
                        self.xMonkey -= self.MonkeyMove

                if event.type == pygame.mouse:
                    if event.mouse==pygame.mouse.get_rel:
                        self.xMonkey += self.MonkeyMove

            self.image_draw(self.linkImgMonkey, self.xMonkey,
                            self.yMonkey, self.xSizeMonkey, self.ySizeMonkey)
            self.banana()
            self.yBanana += self.VBanana

            # ---------Check monkey an duoc banana----------------------------------
            if (self.xMonkey+self.xSizeMonkey > self.xBanana > self.xMonkey or \
            self.xMonkey+self.xSizeMonkey > self.xBanana+self.xSizeBanana> self.xMonkey) and \
            (self.yMonkey+self.ySizeMonkey > self.yBanana  > self.yMonkey or \
            self.yMonkey+self.ySizeMonkey > self.yBanana+self.ySizeBanana  > self.yMonkey):
                self.scores += 1
                if self.scores > self.hscores:
                    self.hscores = self.scores
                self.xBanana = random.randint(0,self.xScreen-70)
                self.yBanana = 0
                self.SpawnBanana = False

            #khi banana roi khoi man hinh
            if self.yBanana > self.yScreen:
                self.lives -= 1
                self.xBanana = random.randint(0,self.xScreen-70)
                self.yBanana = 0
                self.SpawnBanana = False    

            if not self.SpawnBanana:
                self.banana()
            self.SpawnBanana = True
    
            if self.lives < 0:
                self.xMonkey = self.xScreen/2 - 50
                self.checkLost = True

            #toc do tang dan
            self.VBanana = 4 if self.scores < 1 else 4 + self.scores/5 
            
            #gioi han di chuyen cua monkey
            if self.xMonkey<0:
                self.xMonkey = 0
            if self.xMonkey>self.xScreen:
                self.xMonkey = self.xScreen-50

            while(self.checkLost):#neu lives < 0
                for event in pygame.event.get():   # Nếu nhấn
                    if event.type == pygame.QUIT:  # Thoát
                        self.gamerunning = False
                        self.checkLost = False
                        break
                    if event.type == pygame.KEYDOWN:  # Thoát                       
                        self.checkLost = False
                        self.lives = 3
                        self.scores = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.checkLost = False
                        self.lives = 3
                        self.scores = 0
                self.show_hscore(self.xScreen/2-130, 100, "High Scores:{}".format(
                    self.scores), 40)  # In điểm
                self.show_score(self.xScreen/2-120, self.yScreen /
                                2-50, "GAME OVER", 50)  # In Thông báo thua

                self.VBanana = 4
                pygame.display.update()
            
            self.image_draw(self.linkImgMonkey, self.xMonkey,
                            self.yMonkey, self.xSizeMonkey, self.ySizeMonkey)
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)
            self.show_lives(self.xScreen-200, 10, "Lives:{}".format(self.lives), 35)

            #update
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)



if __name__ == "__main__":
    monkey = Monkey()
    monkey.run()       
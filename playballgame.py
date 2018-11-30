import pygame
import sys
from pygame.locals import *
from random import *
class Ball(pygame.sprite.Sprite):
    def __init__(self,image,position,speed,bg_size):
        pygame.sprite.Sprite.__init__(self)#初始化动画精灵
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        #将小球放在指定位置
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]
        self.radius = self.rect.width/2
    def move(self):
        self.rect = self.rect.move(self.speed)
        #对球进行边界检查
        if self.rect.right<=0:
            self.rect.left = self.width
        elif self.rect.left>=self.width:
            self.rect.right=0
        elif self.rect.bottom <=0:
            self.rect.top = self.height
        elif self.rect.top>=self.height:
            self.rect.bottom =0
def main():
    pygame.init()
    ball_image = "0/111.png"
    bg_image = "0/2.jpg"
    running = True
    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('play the ball')
    background = pygame.image.load(bg_image).convert_alpha()
    #用于存放小球对象的列表
    balls =[]
    group = pygame.sprite.Group()
    #创建五个小球
    for i in range(5):
        #位置随机，速度随机
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(0,10),randint(0,10)]
        ball = Ball(ball_image,position,speed,bg_size)
        #碰撞检测
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background,(0,0))
        for each in balls:
            each.move()
            screen.blit(each.image,each.rect)
        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            group.add(each)
        
        pygame.display.flip()
        clock.tick(30)
if __name__=="__main__":
    main()
        

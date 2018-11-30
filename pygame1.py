import pygame
from pygame.locals import * 
import sys
#初始化pygame
pygame.init()
size = width,height=600,400
bg = (255,255,255)#RGB
fullscreen = False
#创建指定大小的窗口Surface
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption('测试一下')
#加载图片
#设置放大缩小的比例
ratio = 1.0
oturtle = pygame.image.load('111.png').convert_alpha()#设置png格式的alpha通道透明度
turtle = oturtle
oturtle_rect = oturtle.get_rect()
speed = [5,0]
turtle_right = pygame.transform.rotate(turtle,90)#设置逆时针旋转角度90
turtle_top = pygame.transform.rotate(turtle,180)
turtle_left = pygame.transform.rotate(turtle,270)
turtle_bottom = turtle
turtle = turtle_top
position = turtle_rect=oturtle_rect
l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            #全屏F11
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920,1080),FULLSCREEN | HWSURFACE)#hwsurface是硬件加速,分辨率可以用pygame.display.list_modes()查看，第0项是分辨率最大值
                    
                else:
                    screen = pygame.display.set_mode(size)
            #放大缩小乌龟(=,-),空格键恢复原始大小
            if event.key == K_EQUALS or event.key== K_MINUS or event.key == K_SPACE:
                #最大只能够放大一倍，缩小只能到50%
                if event.key == K_EQUALS and ratio <2:
                    ratio  += 0.1
                if event.key ==K_MINUS and ratio >0.5:
                    ratio -= 0.1
                if event.key==K_SPACE:
                    ratio = 1.0
                turtle = pygame.transform.smoothscale(oturtle,
                                                     (int(oturtle_rect.width *ratio),
                                                      int(oturtle_rect.height*ratio)))
                                                 
            #用户调整窗口的尺寸
            if event.type == VIDEORESIZE:
                size = event.size
                width,height = size
                print(size)
                screen = pygame.display.set_mode(size,RESIZABLE)
                    
    #移动图像
    position = position.move(speed)
    if position.right >width:
        turtle = turtle_right
        position =turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed= [0,5] 
    if position.bottom >height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top =height- turtle_rect.height
        speed = [-5,0]
    if position.left<0:
        turtle = turtle_left
        position = turtle_rect=turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0,-5]
    if position.top<0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5,0]
    
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(10)
    #此外pygame还提供了修改帧率的方法：如， clock.tick(200),已达到延时目的

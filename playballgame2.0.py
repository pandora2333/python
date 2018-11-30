import pygame
import sys
from pygame.locals import *
from random import *
import traceback
class Ball(pygame.sprite.Sprite):
    def __init__(self,grayball_image,greenball_image,position,speed,bg_size,target):
        pygame.sprite.Sprite.__init__(self)#初始化动画精灵
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        #将小球放在指定位置
        self.rect.left,self.rect.top = position
        self.side = [choice([-1,1]),choice([-1,1])]#对球运动的方向的选择
        self.speed = speed
        self.collide = False
        self.target = target
        self.control = False
        self.width,self.height = bg_size[0],bg_size[1]
        self.radius = self.rect.width/2
    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)#若控制则以我们的控制键设定速度
        else:
            self.rect = self.rect.move((self.side[0]*self.speed[0],self.side[1]*self.speed[1]))#实现了速度与方向的分离,当失控时则随机运动
        #对球进行边界检查,穿越式
        if self.rect.right<=0:
            self.rect.left = self.width
        elif self.rect.left>=self.width:
            self.rect.right=0
        elif self.rect.bottom <=0:
            self.rect.top = self.height
        elif self.rect.top>=self.height:
            self.rect.bottom =0
    #进行小球控制检测
    def check(self,motion):
        if self.target<motion<self.target+5:
            return True
        else:
            return False
class Glass(pygame.sprite.Sprite):
    def __init__(self,glass_image,mouse_image,bg_size):
        #初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left,self.glass_rect.top = \
                                                 (bg_size[0]-self.glass_rect.width)//2,\
                                                bg_size[1]-self.glass_rect.height
        self.mouse_image = pygame.image.load(glass_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left,self.mouse_rect.top = self.glass_rect.left,\
                                                   self.glass_rect.top
        pygame.mouse.set_visible(False)
                                                   
def main():
    pygame.init()
    grayball_image = "gray_ball.png"
    greenball_image = "greenball.png"
    glass_image = 'glass.png'
    mouse_image = 'hand.png'
    bg_image = "background.png"
    running = True
    #添加属性的背景音乐
    pygame.mixer.music.load('bg_music.ogg')
    pygame.mixer.music.play()
    #添加音效
    loser_soound = pygame.mixer.Sounud('loser.wav')
    laugh_sound = pygame.mixer.Sound('laugh.wav')
    winner_sound = pygame.mixer.Sound('winner.wav')
    hole_sound = pygame.mixer.Sound('hole.wav')
    #音乐播放完时游戏结束
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)
    #根据背景图片指定游戏界面大小
    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('play the ball')
    background = pygame.image.load(bg_image).convert_alpha()
    #指定游戏条件的球洞
    hole = [(117,119,199,201),(255,227,390,392),(503,505,320,322)]
    #游戏过程的提示信息
    msgs = []
    #用于存放小球对象的列表
    balls =[]
    #动画精灵的碰撞检测群体
    group = pygame.sprite.Group()
    #创建五个小球
    for i in range(5):
        #位置随机，速度随机
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(1,10),randint(1,10)]
        ball = Ball(ball_image,position,speed,bg_size,5*(i+1))
        #初始化球位置的碰撞检测，防止一直原地抖动
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)
    glass = Glass(glass_image,bg_size)
    motion =0
    MYTIMER = USEREVENT +1
    pygame.time.set_timer(MYTIMER,1*1000)#每一秒发送一次事件，进行事件检测，计时器.反复创建一个事件放在事件 队列中。
                                        #每隔给定的毫秒数，指定事件类型的事 件就会在事件队列中出现一次。第一次事件会在给定时间到了以后才会出现。
    pygame.key.set_repeat(100,50)#监听键盘长按事件，这句话的意思就是，按住某个键以后，长按，再过100毫秒将产生一个KEYDOWN事件，再以后，每隔50毫秒后触发keydown
    
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False
            elif event.type == MYTIMER:
                if motion :
                    for each in group:
                        if each.check(motion):
                            each.speed = [0,0]
                            each.control = True
                    motion = 0
            elif event.type == MOUSEMOTION:
                motion +=1#对多个小球控制
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -=1
                if event.key = K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -=1
                if event.key = K_d :
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                if event.key =K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] +=1
                #控制的球进洞检测
                if event.type = K_SPACE:
                    for each in group:
                        if each.control:
                            for  i in hole:
                                if i[0]<= each.rect.left <= i[1] and\
                                   i[2] <= each.rect.top <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0,0]
                                    group.remove(each)
                                    #为了将以已经入洞的小球先绘制，以达到其他小球从入洞小球的上面穿过的目的
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0,temp)
                                    hole.remove(i)
                            if not hole:
                                pygame.mixer.music.stop()
                                winner_sound.play()
                                pygame.time.delay(3000)
                                msg = pygame.image.load('win.png').convert_alpha()
                                msg_pos = (width - msg.get_width())//2,\
                                          (height - msg.get_height())//2
                                msgs.append((msg,msg_pos))
                                laugh_sound.play()
        screen.blit(background,(0,0))
        screen.blit(glass.glass_image,glass.glass_rect)
        glass.mouse_rect.left,glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left=glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left= glass.mouse_rect.right-glass.mouse_rect.width
        if glass.mouse_rect.top <glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top>glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height
        screen.blit(glass.mouse_image,glass.mouse_rect)
        for each in balls:
            each.move()
            if collide:
                each.speed = [randint(1,10),randint(1,10)]#随机速率
                collide =False
            if each.control:
                screen.blit(each.greenball_image,each.rect)
            else:
                screen.blit(each.grayball_image,each.rect)
            screen.blit(each.image,each.rect)
        #碰撞检测
        for each in group:
            #检测时要从群体中移除自身
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]#分离了速度与方向后防止出现球碰撞后出现抖动不分离问题
                each.collide = True
                #当受我们控制的球碰撞到其它球时，失控
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False
            #检测完毕后将自身重新加入
            group.add(each)
        #若游戏结束则会打印画面，输出为空，什么也不显示（对python而言）
        for msg in msgs:
            screen.blit(msg[0],msg[1])
        pygame.display.flip()
        clock.tick(30)
if __name__=="__main__":
    try:
        main()
    except SystemError:
        pass
    except :
        traceback.print_exc()
        pygame.quit()
        input()
        


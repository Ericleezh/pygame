# -*- coding: utf-8 -*-
__author__ = 'leeho'
import pygame
import time
import sys
import random

class Base(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    def __init__(self,screen_temp,x,y,image_name):
        Base.__init__(self,screen_temp,x,y,image_name)
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断字段是否越界
                self.bullet_list.remove(bullet)

class BaseBullet(Base):
    def __init__(self,screen_temp,x,y,image_name):
        Base.__init__(self,screen_temp,x,y,image_name)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        super().__init__(screen_temp,185,720,"image/plane.png")
        # BasePlane.__init__(self)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane(BasePlane):
    """敌机"""
    def __init__(self,screen_temp):
        super().__init__(screen_temp, 0, 0, "image/diren.png")
        self.direction = "right" # 存储飞机默认的显示方向

    def move(self):
        if self.direction == "right":
            self.x +=5
        elif self.direction == "left":
            self.x -=5

        if self.x>475:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"

    def fire(self):
        # 使用随机数解决子弹发射频率问题
        random_num = random.randint(1,100)
        if  random_num == 25 or random_num == 50:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        super().__init__(screen_temp,x+48,y-30,"image/zidan.png")

    def move(self):
        self.y-=5

    def judge(self):
        if self.y < 50:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        super().__init__(screen_temp, x+35, y+48, "image/direnzidan.png")

    def move(self):
        self.y+=5

    def judge(self):
        if self.y > 810:
            return True
        else:
            return False

def key_control(hero_temp):
    # 获取事件
    for event in pygame.event.get():

        # 判断是否按了退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 判断是否按了键
        elif event.type == pygame.KEYDOWN:
            # 检测是否是按了a或者left
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print("left")
                hero_temp.move_left()
            # 检测是否是按了d或者right
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print("right")
                hero_temp.move_right()
            # 检测是否是按了空格键
            if event.key == pygame.K_SPACE:
                print("SPACE")
                hero_temp.fire()


def main():
    # 创建窗口
    screen = pygame.display.set_mode((550, 852),0,32)
    # 创建背景
    background = pygame.image.load("image/bc.jpg")
    # 创建飞机
    hero = HeroPlane(screen)
    # 创建敌机
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()


        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
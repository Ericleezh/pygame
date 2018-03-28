# -*- coding: utf-8 -*-
__author__ = 'leeho'
import pygame
import time
import sys

class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 185
        self.y = 720
        self.screen = screen_temp
        self.image = pygame.image.load("image/plane.png")
        self.bullet_list = [] # 存储发射出去的子弹对象引用


    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+48
        self.y = y-30
        self.screen = screen_temp
        self.image = pygame.image.load("image/zidan.png")

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y-=5


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
    # 创建子弹
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
import pygame
from obj import Obj, Bee, Text
from random import randrange


class Game:
    def __init__(self):

        self.bg = Obj('assets/bg.png', 0, 0)
        self.bg2 = Obj('assets/bg.png', 0, -640)

        self.change_scene = False

        self.spider = Obj('assets/spider1.png', randrange(0, 300), -50)
        self.flower = Obj('assets/florwer1.png', randrange(0, 300), -50)
        self.bee = Bee('assets/bee1.png', 150, 600)

        self.score = Text(150, '0')
        self.lifes = Text(60, '3')

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.bee.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.draw(window, 160, 15)
        self.lifes.draw(window, 10, 10)

    def update(self):
        self.move_bg()
        self.spider.anim('spider', 8, 5)
        self.flower.anim('florwer', 10, 3)
        self.bee.anim('bee', 2, 5)
        self.move_spider()
        self.move_flower()
        self.bee.colision(self.spider.group, 'Spider')
        self.bee.colision(self.flower.group, 'Flower')
        self.gameover()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spider(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj('assets/spider1.png', randrange(0, 300), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 5

        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj('assets/florwer1.png', randrange(0, 300), -50)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True

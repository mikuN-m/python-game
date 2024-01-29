import pygame
import enemy_shot

import numpy as np

class Enemy(pygame.sprite.Sprite):
  def __init__(self,screen_width,screen_height):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/enemy_img.png')
    self.rect = self.image.get_rect()
    self.width = screen_width
    self.height = screen_height
    self.rect.center = (self.width//2, self.height//6)

  def update(self):
    time = pygame.time.get_ticks()

    if 1000 <= time <= 10000:
      self.move1()
    
    if 11000 <= time <= 20000:
      self.move2()

  def move1(self):
    time = pygame.time.get_ticks()

    if 1000 <= time <= 2000:
      self.rect.move_ip(3,0)
    if 2000 <= time <= 4000:
      self.rect.move_ip(-3,0)
    if 4000 <= time <= 6000:
      self.rect.move_ip(3,0)
    if 7000 <= time <= 10000:
      self.rect.move_ip(-1,0)

    for i in range(1000, 6000, 500):
      if i <= time <= i+30:
        enemy_shot.shot1(self.rect.center)

  def move2(self):
    time = pygame.time.get_ticks()

    for i in range(11000,20000, 800):
      if i <= time <= i+30:
        th = range(0, 390, 30)
        x_box = []
        y_box = []

        for i in th:
          x = 5*np.cos(np.radians(i))
          y = 5*np.sin(np.radians(i))
          x_box.append(x)
          y_box.append(y)

        i = 0
        while i < len(x_box):
          enemy_shot.shot2(self.rect.center,x_box[i],y_box[i],self.width,self.height)
          i += 1
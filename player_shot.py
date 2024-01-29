import pygame
from pygame.locals import *

class Player_shot(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/player_shot.png')
    self.rect = self.image.get_rect()
    self.rect.center = (x+20,y-20)

  def update(self):
    self.rect.move_ip(0,-50)
    if self.rect.top <= 0:
      self.kill()
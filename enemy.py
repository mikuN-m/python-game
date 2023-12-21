import pygame
from pygame.locals import *

class Enemy():
  def __init__(self):
    self.enemy_img = pygame.image.load('images/enemy_img.png')
    self.enemy_rect = self.enemy_img.get_rect()
    self.enemy_rect.center = (725//2, 551-450)

  def draw(self,screen):
    screen.blit(self.enemy_img,self.enemy_rect)
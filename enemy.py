import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
  def __init__(self,screen_width,screen_height):
    pygame.sprite.Sprite.__init__(self)
    self.enemy_img = pygame.image.load('images/enemy_img.png')
    self.rect = self.enemy_img.get_rect()
    self.rect.center = (screen_width//2, screen_height//6)

  def draw(self,screen):
    screen.blit(self.enemy_img,self.rect)
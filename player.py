import pygame
from pygame.locals import *

class Player():
  speed = 5

  def __init__(self):
    self.player_img = pygame.image.load('images/player_img.png')
    self.player_rect = self.player_img.get_rect()
    self.player_rect.center = (725//2, 551-80)

  def updata(self):
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
      self.player_rect.move_ip(0,-self.speed)
    
    if pressed_keys[K_DOWN]:
      self.player_rect.move_ip(0,self.speed)

    if pressed_keys[K_LEFT]:
      self.player_rect.move_ip(-self.speed,0)

    if pressed_keys[K_RIGHT]:
      self.player_rect.move_ip(self.speed,0)

    self.player_rect.clamp_ip(Rect(0,0,725,551))


  def draw(self,screen):
    screen.blit(self.player_img,self.player_rect)
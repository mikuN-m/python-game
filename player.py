import pygame
from pygame.locals import *

import player_shot

class Player(pygame.sprite.Sprite):
  speed = 7

  def __init__(self,screen_width,screen_height):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/player_img.png')
    self.rect = self.image.get_rect()
    self.rect.center = (screen_width//2, screen_height-80)

  def update(self):
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
      self.rect.move_ip(0,-self.speed)
    
    if pressed_keys[K_DOWN]:
      self.rect.move_ip(0,self.speed)

    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-self.speed,0)

    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(self.speed,0)

    self.rect.clamp_ip(Rect(0,30,725,551-30))

    if pressed_keys[K_SPACE]:
      player_shot.Player_shot(self.rect.x,self.rect.y)
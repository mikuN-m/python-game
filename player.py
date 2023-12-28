import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  speed = 5

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.player_img = pygame.image.load('images/player_img.png')
    self.rect = self.player_img.get_rect()
    self.rect.center = (725//2, 551-80)

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

    self.rect.clamp_ip(Rect(0,0,725,551))


  def draw(self,screen):
    screen.blit(self.player_img,self.rect)
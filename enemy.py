import pygame
import enemy_shot

class Enemy(pygame.sprite.Sprite):
  def __init__(self,screen_width,screen_height):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/enemy_img.png')
    self.rect = self.image.get_rect()
    self.rect.center = (screen_width//2, screen_height//6)

  def update(self):
    enemy_shot.Enemy_shot(self.rect.center)
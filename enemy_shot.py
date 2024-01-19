import pygame

class Enemy_shot(pygame.sprite.Sprite):
  def __init__(self,pos):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/enemy_shot.png')
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def update(self):
    self.rect.move_ip(0,5)
    if self.rect.top <= 0:
      self.kill()
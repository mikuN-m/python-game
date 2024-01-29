import pygame

class shot1(pygame.sprite.Sprite):
  def __init__(self,pos):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/enemy_shot.png')
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def update(self):
    self.rect.move_ip(0,3)
    if self.rect.bottom >= 550:
      self.kill()

class shot2(pygame.sprite.Sprite):
  def __init__(self,pos,x,y,width,height):
    pygame.sprite.Sprite.__init__(self,self.containers)
    self.image = pygame.image.load('images/enemy_shot.png')
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def update(self):
    self.rect.move_ip(self.x,self.y)
    if self.rect.top<=0 or self.rect.right>=self.width or self.rect.bottom>=self.height or self.rect.left<=0:
      self.kill()

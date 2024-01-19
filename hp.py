import pygame

class Hp():
  def __init__(self,screen_width):
    self.width = screen_width
    self.hp = screen_width
    self.hp_color = (0,255,0)
    self.rect = pygame.Rect(0,0,self.hp,30)

  def draw(self,screen):
    pygame.draw.rect(screen,self.hp_color,self.rect)
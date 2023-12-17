import pygame
from pygame.locals import *
import os

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 551

running = True

class run():
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Test")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    self.bg = pygame.image.load('images/bg.jpg')

    while running:
      self.draw(screen)
      clock.tick(100)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()

  def draw(self,screen):
    screen.blit(self.bg, (0, 0))



if __name__ == "__main__":
  run()
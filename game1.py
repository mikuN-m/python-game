import pygame
from pygame.locals import *

import player
import enemy

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 551

running = True


class Game():
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Test")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bg = pygame.image.load('images/bg.jpg')

    self.Player = player.Player()
    self.Enemy = enemy.Enemy()

    while running:
      self.updata()
      self.draw(screen,bg)
      clock.tick(70)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()


  def updata(self):
    self.Player.updata()

  def draw(self,screen,bg):
    screen.blit(bg, (0, 0))
    self.Enemy.draw(screen)
    self.Player.draw(screen)

if __name__ == "__main__":
  Game()
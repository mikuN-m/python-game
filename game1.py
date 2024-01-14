import pygame
from pygame.locals import *

import player
import enemy
import player_shot

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 551

player_pos = 0


class Game(pygame.sprite.Sprite):
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Test")
    self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()

    self.bg = pygame.image.load('images/bg.jpg')

    self.Player = player.Player(SCREEN_WIDTH,SCREEN_HEIGHT)
    self.Enemy = enemy.Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)

    self.enemies = pygame.sprite.Group()

    self.enemies.add(self.Enemy)

    self.running = True

    self.all = pygame.sprite.RenderUpdates()
    self.shot = pygame.sprite.Group()

    player_shot.Player_shot.containers = self.all, self.shot

  def run(self):
    while self.running:
      self.update()
      self.draw(self.screen,self.bg)
      self.clock.tick(70)

    pygame.quit()

  def update(self):
    self.Player.update()
    self.all.update()

    self.collision()

    for event in pygame.event.get():
      if event.type == QUIT:
        self.running = False

  def collision(self):
    test = pygame.sprite.spritecollide(self.Player,self.enemies,False)

    if test:
      self.running = False

  def draw(self,screen,bg):
    screen.blit(bg, (0, 0))
    self.Enemy.draw(screen)
    self.Player.draw(screen)
    self.all.draw(screen)

    pygame.display.update()

if __name__ == "__main__":
  game = Game()
  game.run()
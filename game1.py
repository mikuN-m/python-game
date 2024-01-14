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
    
    self.running = True

    self.all = pygame.sprite.RenderUpdates()
    self.shot = pygame.sprite.Group()
    self.player = pygame.sprite.Group()
    self.enemies = pygame.sprite.Group()

    player.Player.containers = self.all, self.player
    enemy.Enemy.containers = self.all, self.enemies
    player_shot.Player_shot.containers = self.all, self.shot

    self.Player = player.Player(SCREEN_WIDTH,SCREEN_HEIGHT)
    self.Enemy = enemy.Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)

  def run(self):
    while self.running:
      self.update()
      self.draw(self.screen,self.bg)
      self.clock.tick(70)

    pygame.quit()

  def update(self):
    self.all.update()

    self.collision()

    for event in pygame.event.get():
      if event.type == QUIT:
        self.running = False

  def collision(self):
    player = pygame.sprite.groupcollide(self.player,self.enemies,True,True)
    shot = pygame.sprite.groupcollide(self.enemies,self.shot,True,True)

    if player or shot:
      self.running = False

  def draw(self,screen,bg):
    screen.blit(bg, (0, 0))
    self.all.draw(screen)

    pygame.display.update()

if __name__ == "__main__":
  game = Game()
  game.run()
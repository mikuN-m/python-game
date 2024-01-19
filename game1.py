import pygame
from pygame.locals import *

import player
import enemy
import player_shot
import enemy_shot
import hp

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 551

class Game(pygame.sprite.Sprite):
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Test")
    self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.bg = pygame.image.load('images/bg.jpg')
    self.hp = hp.Hp(SCREEN_WIDTH)
    
    self.running = True

    self.all = pygame.sprite.RenderUpdates()
    self.player_shot = pygame.sprite.Group()
    self.player = pygame.sprite.Group()
    self.enemies = pygame.sprite.Group()
    self.enemy_shot = pygame.sprite.Group()

    player.Player.containers = self.all, self.player
    enemy.Enemy.containers = self.all, self.enemies
    player_shot.Player_shot.containers = self.all, self.player_shot
    enemy_shot.Enemy_shot.containers = self.all, self.enemy_shot

    self.Player = player.Player(SCREEN_WIDTH,SCREEN_HEIGHT)
    self.Enemy = enemy.Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)

  def run(self):
    while self.running:
      self.update()
      self.draw(self.screen,self.bg)
      self.clock.tick(60)

    pygame.quit()

  def update(self):
    self.all.update()
    self.collision()

    for event in pygame.event.get():
      if event.type == QUIT:
        self.running = False

  def collision(self):
    player = pygame.sprite.groupcollide(self.player,self.enemies,True,True)
    ene_shot = pygame.sprite.groupcollide(self.enemy_shot,self.player,False,False)
    pl_shot = pygame.sprite.groupcollide(self.enemies,self.player_shot,False,False)

    if pl_shot:
      self.hp.hp -= 1
      self.hp.rect.inflate_ip(-1,0)
      
      if self.hp.hp == SCREEN_WIDTH // 4:
        self.hp.hp_color = (200,55,0)
      if self.hp.hp == 0:
        self.running = False

    if player or ene_shot:
      self.running = False

  def draw(self,screen,bg):
    screen.blit(bg, (0, 0))
    self.all.draw(screen)
    self.hp.draw(screen)

    pygame.display.update()

if __name__ == "__main__":
  game = Game()
  game.run()
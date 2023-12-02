import pygame
from pygame.locals import *

running = True


def updata():
  global running



  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

def draw(screen):
  screen.fill((255,255,255))
  pygame.display.update()

def run():
  pygame.init()
  screen = pygame.display.set_mode((500, 300))
  pygame.display.set_caption("Test")

  while running:
    updata()
    draw(screen)
    
  pygame.quit()

if __name__ == "__main__":
    run()
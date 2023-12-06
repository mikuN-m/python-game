import pygame
from pygame.locals import *


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

player_x = SCREEN_WIDTH // 2 
player_y = SCREEN_HEIGHT // 2

running = True
text = None

def updata():
  global running

  for event in pygame.event.get():
    if event.type == QUIT:
      running = False


def draw(screen):
  screen.fill((255,255,255))

  screen_size = screen.get_size()
  text_size = text.get_rect()
  text_size.center = (screen_size[0] // 2, screen_size[1] //5)

  pygame.draw.circle(screen, (0,0,0), (player_x,player_y), 10)

  screen.blit(text,text_size)

  pygame.display.update()


def run():
  global text

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Test")
  font = pygame.font.Font(None,40)
  text = font.render('Hello python',True,(000,000,000))

  while running:
    updata()
    draw(screen)
    
  pygame.quit()

if __name__ == "__main__":
    run()
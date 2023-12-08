import pygame
from pygame.locals import *


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

player_x = SCREEN_WIDTH // 2 
player_y = SCREEN_HEIGHT // 2

running = True
text = None

def updata():
  global running
  global player_x
  global player_y

  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

  # playerの操作
  pressed_keys = pygame.key.get_pressed()

  if pressed_keys[pygame.K_UP]:
    player_y = player_y - 3
    if player_y < 10:
      player_y = 10

  if pressed_keys[pygame.K_DOWN]:
    player_y = player_y + 3
    if player_y > SCREEN_HEIGHT - 10:
      player_y = SCREEN_HEIGHT - 10

  if pressed_keys[pygame.K_LEFT]:
    player_x = player_x - 3
    if player_x < 10:
      player_x = 10

  if pressed_keys[pygame.K_RIGHT]:
    player_x = player_x + 3
    if player_x > SCREEN_WIDTH - 10:
      player_x = SCREEN_WIDTH - 10


def draw(screen):
  screen.fill((255,255,255))

  # テキストの描写
  screen_size = screen.get_size()
  text_size = text.get_rect()
  text_size.center = (screen_size[0] // 2, screen_size[1] //5)
  screen.blit(text,text_size)

  # playerの描写
  pygame.draw.circle(screen, (0,0,0), (player_x,player_y), 10)

  pygame.display.update()


def run():
  global text

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Test")
  font = pygame.font.Font(None,40)
  text = font.render('Hello python',True,(000,000,000))
  clock = pygame.time.Clock()

  while running:
    updata()
    draw(screen)

    clock.tick(100)
    
  pygame.quit()

if __name__ == "__main__":
    run()
import pygame 
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()

size = (width,height) = (screen_info.current_w,screen_info.current_h)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (0,0,0)

#444 x 72
def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      screen.fill(color)
      pygame.display.flip()

if __name__ == "__main__":
  main()
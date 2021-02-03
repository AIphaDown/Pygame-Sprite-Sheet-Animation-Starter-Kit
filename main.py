import pygame 
from pygame.locals import *
from sprite_loader import *
from cat import *

cat_images = []

cats = []

pygame.init()

screen_info = pygame.display.Info()

size = (width,height) = (screen_info.current_w,screen_info.current_h)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (2, 194, 72)

def get_images():
  cat_sheet = SpriteSheet('knightRunning.png') 
  #get individual images
  
  for i in range(1):
    for j in range(6):
      cat_images.append(cat_sheet.get_image(j*70,i*100,70,100))
      #cat_images[-1] = pygame.transform.smoothscale(cat_images[-1],(616,100))

#444 x 72
def main():
  get_images()

  for i in range(5):
    cat = Cat((-90, random.randint(50,height-50)),cat_images)
    cats.append(cat)
  #cat1 = Cat((-90, random.randint(50,height-50)),cat_images)

  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    

    screen.fill(color)

    for cat in cats:
      cat.update()
      cat.draw(screen)
      
    pygame.display.flip()

if __name__ == "__main__":
  main()
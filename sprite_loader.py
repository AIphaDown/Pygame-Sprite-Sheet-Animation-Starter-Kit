import pygame 

class SpriteSheet:
  def __init__(self,img_path):
    self.sprite_sheet = pygame.image.load(img_path)
  def get_image(self,x,y,width,height):
    #self.sprite_sheet.convert_alpha()
    image = pygame.Surface([width,height], pygame.SRCALPHA)
    image.blit(self.sprite_sheet, (0,0),(x,y,width,height))
    image.set_colorkey((120, 92, 67))
    return image
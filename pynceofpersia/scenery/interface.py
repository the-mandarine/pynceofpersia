import pygame
import os

BASE_SPRITE_IMG_PATH = "scenery/imgs"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def load_image(path, key):
    ipath = os.path.join(BASE_SPRITE_IMG_PATH, path)
    img = pygame.image.load(ipath).convert()
    img.set_colorkey(key)
    return img

class Sprite(pygame.sprite.Sprite):
    map_pos = (0,0)
    img_paths = []
    r_img_paths = []
    imgs = None
    prev_tile = None
    def __init__(self):
        super(Sprite, self).__init__()
        # self.imgs = None
        # self.prev_tile = None

    def load_imgs(self, color_key=WHITE):
        if self.prev_tile is not None:
            self.img_paths += self.prev_tile.r_img_paths
        self.imgs = [(load_image(img_path[0], color_key), img_path[1:3])
                     for img_path in self.img_paths]
        print(repr(self.imgs))



    def draw(self, screen, x, y, sx, sy):
        if self.imgs is None:
            self.load_imgs()

        for img, rel_pos in reversed(self.imgs):
            screen.blit(img,
                        (x * sx + rel_pos[0],
                         y * sy + rel_pos[1],)
                        )

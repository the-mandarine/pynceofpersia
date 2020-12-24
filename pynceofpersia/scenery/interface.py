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
    map_pos = (0, 0)
    a_imgs = []
    b_imgs = []
    c_imgs = []
    d_imgs = []
    front_imgs = []
    imgs = None
    prev_tile = None
    def __init__(self):
        super(Sprite, self).__init__()

    def pick_imgs(self):
        pass

    def ordered_img_paths(self):
        if self.bottom:
            return self.bottom.left.c_imgs + self.left.b_imgs + self.d_imgs + self.a_imgs + self.front_imgs
        return self.left.b_imgs + self.d_imgs + self.a_imgs + self.front_imgs

    def load_imgs(self, color_key=WHITE):
        self.pick_imgs()
        img_paths = self.ordered_img_paths()
        self.imgs = [(load_image(img_path[0], color_key), img_path[1:3])
                     for img_path in img_paths]

    def draw(self, screen, tile_width, tile_height):
        if self.imgs is None:
            self.load_imgs()

        for img, rel_pos in self.imgs:
            screen.blit(img,
                        (self.map_pos[0] * tile_width + rel_pos[0],
                         self.map_pos[1] * tile_height + rel_pos[1],)
                        )

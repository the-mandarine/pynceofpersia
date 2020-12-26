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

def nth_elem(l, i, default=[]):
    if l:
        return [l[i % len(l)]]
    return default


class Sprite(pygame.sprite.Sprite):
    map_pos = (0, 0)
    screen_pos = (0, 0)
    a_imgs = []
    b_imgs = []
    c_imgs = []
    d_imgs = []
    e_imgs = []
    f_imgs = []
    imgs = None
    bottom = None

    def __init__(self, tick=10):
        super(Sprite, self).__init__()
        self.img_id = 0
        self.tick = tick
        self.last_tick = 0

    def pick_imgs(self):
        pass

    def ordered_img_paths(self):
        img_list = []
        if self.bottom:
            max_id = max([len(self.bottom.left.c_imgs),
                          len(self.left.b_imgs),
                          len(self.d_imgs),
                          len(self.a_imgs),
                          len(self.e_imgs),
                          len(self.f_imgs),])

            for i in range(max_id):
                img_list.append(nth_elem(self.bottom.left.c_imgs, i)
                                + nth_elem(self.left.b_imgs, i)
                                + nth_elem(self.d_imgs, i)
                                + nth_elem(self.a_imgs, i)
                                + nth_elem(self.e_imgs, i)
                                + nth_elem(self.f_imgs, i))


        else:
            max_id = max([len(self.left.b_imgs),
                          len(self.d_imgs),
                          len(self.a_imgs),
                          len(self.e_imgs),
                          len(self.f_imgs),])
            for i in range(max_id):
                img_list.append(nth_elem(self.left.b_imgs, i)
                                + nth_elem(self.d_imgs, i)
                                + nth_elem(self.a_imgs, i)
                                + nth_elem(self.e_imgs, i)
                                + nth_elem(self.f_imgs, i))

        return img_list

    def load_imgs(self, color_key=WHITE):
        self.pick_imgs()
        img_paths = self.ordered_img_paths()
        self.imgs = []
        for frame in img_paths:
            self.imgs.append([(load_image(img_path[0], color_key), img_path[1:3])
                          for img_path in frame])

    def draw(self, screen, tick=10, tile_width=64, tile_height=125):
        if self.imgs is None:
            self.load_imgs()

        self.last_tick += tick
        if self.last_tick > self.tick:
            self.last_tick %= self.tick
            self.last_tick += tick
            self.img_id += 1
            if self.imgs:
                self.img_id %= len(self.imgs)
            else:
                self.img_id = 0

        for frame in nth_elem(self.imgs, self.img_id):
            for img, rel_pos in frame:
                screen.blit(img,
                            (self.screen_pos[0] * tile_width + rel_pos[0],
                             self.screen_pos[1] * tile_height + rel_pos[1] + 5,)
                           )

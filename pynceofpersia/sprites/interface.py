import numpy
import pygame
import os

BASE_SPRITE_IMG_PATH = "sprites/imgs"
def load_image(path, key):
    ipath = os.path.join(BASE_SPRITE_IMG_PATH, path)
    img = pygame.image.load(ipath).convert()
    img.set_colorkey(key)
    return img

class AnimatedSprite(pygame.sprite.Sprite):
    pos = [0,0]
    img_id = 0
    last_tick = 0
    reverse = False
    def __init__(self, img_paths, colkey, tick=100):
        super(AnimatedSprite, self).__init__()
        self.events = []
        self.imgs = []
        for img_path in img_paths:
            img = load_image(img_path[0], colkey)
            self.imgs.append( (img, img_path[1]) )
        self.tick = tick

    def react(self, event):
        print(event)

    def update(self, screen, tick = 10):
        self.last_tick += tick
        if self.last_tick > self.tick:
            self.last_tick %= self.tick
            self.img_id += 1
        img_id = self.img_id % len(self.imgs)
        if self.reverse:
            max_img_id = 2 * (len(self.imgs) - 1)
            self.img_id %= max_img_id
            #TODO simplify this
            img_id = len(self.imgs) - 1 - abs(len(self.imgs) - 1 - self.img_id)

        screen.blit(self.imgs[img_id][0],
                    numpy.subtract(self.pos, (self.imgs[img_id][1])))

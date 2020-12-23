import pygame
import os
from .interface import Sprite

# Each tile is divided in 4 sprites:
# - Ground
# - FrontGround
# - Wall
# - Left tile

class Empty(Sprite):
    def __init__(self):
        super(Empty, self).__init__()
        self.img_paths = []
        self.r_img_paths = []


class Floor(Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.img_paths = [
                          ("1241.bmp", 0, 108),
                          ("1243.bmp", 0, 134),
                         ]
        self.r_img_paths = [
                            ("1242.bmp", 0, 108),
                           ]


class Wall(Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.img_paths = [
                          ("1296.bmp", 0, 10),
                          ("1297.bmp", 0, -15),
                          ("1366.bmp", 0, 15),
                          ("1363.bmp", 0, 134),
                         ]
        self.r_img_paths = [
                            ("1298.bmp", 0, -20),
                            ("1361.bmp", 0, 15),
                            ("1362.bmp", 0, -10),
                           ]

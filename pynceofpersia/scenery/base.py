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

class Floor(Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.a_imgs = [("1241.bmp", 0, 95),]
        self.b_imgs = [("1242.bmp", 0, 95),]
        self.d_imgs = [("1243.bmp", 0, 120),]


class Wall(Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.a_imgs = [("1366.bmp", 0, 0),]
        self.b_imgs = [("1361.bmp", 0, 0),]
        self.c_imgs = [("1362.bmp", 0, 100),]
        self.d_imgs = [("1363.bmp", 0, 120),]

    def pick_imgs(self):
        if isinstance(self.left, Wall):
            if isinstance(self.right, Wall):
                self.a_imgs = [("1364.bmp", 0, 0,),]
                self.d_imgs = [("1363.bmp", 0, 120,),]
            else:
                self.a_imgs = [("1366.bmp", 0, 0,),]
                self.d_imgs = [("1365.bmp", 0, 120,),]

        else:
            if isinstance(self.right, Wall):
                self.a_imgs = [("1370.bmp", 0, 0,),]
                self.d_imgs = [("1369.bmp", 0, 120,),]

            else:
                self.a_imgs = [("1368.bmp", 0, 0,),]
                self.d_imgs = [("1367.bmp", 0, 120,),]

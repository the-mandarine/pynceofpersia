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
        super().__init__()

class Stairs(Sprite):
    def __init__(self):
        super().__init__()
        self.open = False
        self.a_imgs = [("1237.bmp", 0, 1), ("1238.bmp", 0, -45),]
        self.b_imgs = [("1239.bmp", 0, 1),]
        self.c_imgs = [("1240.bmp", 0, 80),]
        self.d_imgs = [("1236.bmp", 0, 120),]


class Floor(Sprite):
    def __init__(self):
        super().__init__()
        self.a_imgs = [("1241.bmp", 0, 95),]
        self.b_imgs = [("1242.bmp", 0, 95),]
        self.d_imgs = [("1243.bmp", 0, 120),]


class Wall(Sprite):
    def __init__(self):
        super().__init__()
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

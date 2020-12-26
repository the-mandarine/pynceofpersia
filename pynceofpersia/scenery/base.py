import pygame
import os
from .interface import Sprite

# Each tile is divided in 4 sprites:
# - Ground
# - FrontGround
# - Wall
# - Left tile

class Empty(Sprite):
    chr = "."
    def __init__(self):
        super().__init__()

class Stairs(Sprite):
    chr = "@"

    def __init__(self):
        super().__init__()
        self.open = False
        self.b_imgs = [("1239.bmp", 0, 1),]
        self.c_imgs = [("1240.bmp", 0, 80),]
        self.d_imgs = [("1236.bmp", 0, 120),]
        self.e_imgs = [("1238.bmp", 0, -45),]
        self.f_imgs = [("1237.bmp", 0, 1),]

class Floor(Sprite):
    chr = "_"
    def __init__(self):
        super().__init__()
        self.a_imgs = [("1241.bmp", 0, 95),]
        self.b_imgs = [("1242.bmp", 0, 95),]
        self.d_imgs = [("1243.bmp", 0, 120),]


class Wall(Sprite):
    chr = "#"
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

class Torch(Sprite):
    chr = "i"
    def __init__(self):
        super().__init__()
        self.tick = 80
        self.e_imgs = [
                       ("0151.bmp", 60, 0),
                       ("0152.bmp", 60, 0),
                       ("0153.bmp", 60, 0),
                       ("0154.bmp", 60, 0),
                       ("0155.bmp", 60, 0),
                       ("0156.bmp", 60, 0),
                       ("0157.bmp", 60, 0),
                       ("0158.bmp", 60, 0),
                       ("0159.bmp", 60, 0),
                      ]
        self.f_imgs = [("1346.bmp", 65, 35)]

class EmptyTorch(Torch, Empty):
    pass

class FloorTorch(Torch, Floor):
    pass

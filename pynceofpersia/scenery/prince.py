from sprites.interface import AnimatedSprite

class SuspendedPrince(AnimatedSprite):
    reverse = True
    def __init__(self, pos):
        super(SuspendedPrince, self).__init__([("0500.bmp", (25, 0)),
                                               ("0501.bmp", (26, 0)),
                                               ("0502.bmp", (17, 0)),
                                               ("0503.bmp", (11, 0)),
                                               ("0504.bmp", (6, 0)),
                                               ("0505.bmp", (1, 0)),
                                               ("0506.bmp", (0, 0)),
                                               ("0507.bmp", (0, 0)),
                                               ("0508.bmp", (0, 0)),
                                               ("0509.bmp", (0, 0)),
                                               ("0510.bmp", (0, 0)),
                                               ("0511.bmp", (0, 0)),
                                               ("0512.bmp", (0, 0))],
                                              (255, 255, 255), tick=100)
        self.pos = pos

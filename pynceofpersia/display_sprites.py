import os
import pygame
import random
from sprites import SuspendedPrince

TITLE = "Pynce of Persia"
SIZE = (640, 480)
TICK = 60
BASE_SPRITE_IMG_PATH = "../sprites/imgs/"
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GUI(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode(SIZE)
        self.done = False
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        # Ordered list of elements to refresh from back to front
        self.elements = []
        self.events = {}

    def register(self, element):
        self.elements.append(element)
        for event in element.events:
            event_reactors = self.events.get(event, {})
            event_reactors.update({element: str(element)})
            self.events[event] = event_reactors

    def update(self):
        tick = self.clock.tick(TICK)
        self.screen.fill(BLACK)
        pygame.draw.circle(self.screen, WHITE, (300, 300), 2)
        for element in self.elements:
            element.update(self.screen, tick)

        pygame.display.flip()



def main():
    gui = GUI()
#    torch = Torch([100, 100])
    prince = SuspendedPrince([300, 300])
#    princess = Princess([400, 100])
#    gui.register(torch)
    gui.register(prince)
#    gui.register(princess)

    game_is_done = False
    while not game_is_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_done = True
            if str(event) in gui.events:
                for element in gui.events[str(event)]:
                    element.react(event)

        gui.update()
    pygame.quit()

if __name__ == '__main__':
    main()

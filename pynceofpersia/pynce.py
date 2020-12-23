import pygame
import random
import json
from stage import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()


#background_image = pygame.image.load("imgs/motifs.png").convert()




def main():
    # Loop until the user clicks the close button.
    done = False
    # Set the width and height of the screen [width, height]
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pynce of Persia")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    txt_stage = get_txt_stage()
    obj_stage = txt2stage(txt_stage)
    cur_screen_stage = get_stage_part(obj_stage, 0, 0)
    # for i in cur_screen_stage:
    #     for j in i:
    #         print(repr(j))
    #     print(30 * "-")

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #screen.blit(background_image, [0, 0])
        screen.fill(BLACK)

        # --- Drawing code should go here
        player_position = pygame.mouse.get_pos()
        #x = player_position[0]
        #y = player_position[1]
        y = len(cur_screen_stage) - 1
        for line in reversed(cur_screen_stage):
            x = len(line) - 1
            for tile in reversed(line):
                for element in tile:
                    element.draw(screen, x, y, 64, 125)
                x -= 1
            y -= 1

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    main()

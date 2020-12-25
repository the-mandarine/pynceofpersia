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
    size = (640, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pynce of Persia")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    txt_stage = get_txt_stage()
    obj_stage = txt2stage(txt_stage)
    cur_x = 2
    cur_y = 2
    scr_stage, scr_roof = get_stage_part(obj_stage, cur_x, cur_y, scrolling=False)

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
        x = 0
        for tile in scr_roof:
            for element in tile:
                element.draw(screen, roof=True)
            x += 1
        y = 0
        for line in scr_stage:
            x = 0
            for tile in line:
                for element in tile:
                    element.draw(screen)
                x += 1
            y += 1

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    main()

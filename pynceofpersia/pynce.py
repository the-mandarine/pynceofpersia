import pygame
import random
import json
from stage import Stage

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

RED_ST = (255, 0, 0, 50)

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

    stage = Stage("level1.txt")
    cur_x, cur_y = stage.start
    s_pos_x, s_pos_y = stage.start

    scr_stage = stage.get_screen(cur_x, cur_y, scrolling=False)


    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    print("up")
                    cur_y = max(1, cur_y - 1)
                if event.key == pygame.K_j:
                    print("left")
                    # TODO: allow left-right loop
                    cur_x = max(0, cur_x - 1)
                if event.key == pygame.K_k:
                    print("down")
                    cur_y = min(stage.max_y - 1, cur_y + 1)
                if event.key == pygame.K_l:
                    print("right")
                    cur_x = min(stage.max_x - 1, cur_x + 1)

                scr_stage = stage.get_screen(cur_x, cur_y, scrolling=False)
                s_pos_x, s_pos_y = stage.get_scr_pos(cur_x, cur_y)

                print(30 * "=")
                for line in scr_stage:
                    print("".join([tile[0].chr for tile in line]))


        #screen.blit(background_image, [0, 0])
        screen.fill(BLACK)

        y = 0
        for line in scr_stage:
            x = 0
            for tile in line:
                for element in tile:
                    element.draw(screen)
                x += 1
            y += 1

        px = s_pos_x * 64 + 20
        py = (s_pos_y - 1) * 125 + 30
        rect = pygame.Surface((62, 81))
        rect.set_alpha(100)
        rect.fill(RED)
        screen.blit(rect, (px, py))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    main()

"Author name:  <Enes Altun>"
"Date:  <09/05/2022>"
"Description: continuous flash"
"Usage: follow the instructions in the comments"

import pygame
import random


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
w=size[0]
h=size[1]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Drawing code, change 20 if you want to change canvas size
    for i in range(0,w, 20):
        for j in range(0, h, 20):
            pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [i, j, 20, 20])
            # for different animation variations, uncomment the following line and edit the values
            # pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [i, j, 100, 100], 5)
            # aantal = 10
            # for k in range(0, aantal):
            #     pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [i + k * 10, j + k * 10, 100 - k * 20, 100 - k * 20], 5)
            #     aantal = 10
            #     for k in range(0, aantal):
            #         pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [i + k * 10, j + k * 10, 100 - k * 20, 100 - k * 20], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
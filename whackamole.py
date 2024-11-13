import pygame
import random

"""
The mole image should be drawn in the top left square.
When the user clicks on the mole's square, it should move to a different random square.
"""

pygame.init()

mole_image = pygame.image.load("./mole.png")
screen = pygame.display.set_mode((640, 512))
clock = pygame.time.Clock()

def draw_grid():
    # The window should be divided into a 20x16 grid of 32x32 squares.
    # (640, 512)
    # draw horizontal lines
    LINE_COLOR = (0, 128, 0) 
    for i in range(1, 16):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(0, i * 32),
            end_pos=(640, i * 32),
        )
    # draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(i * 32, 0),
            end_pos=(i * 32, 512),
        )

def main():
    try:
        # You can draw the mole with this snippet:
        row, col = (0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos  # tuple of coordinates
                    print("x and y",x, y)
                    a, b = (x // 32, y // 32)
                    print("a and b", a, b)
                    print("row and column",row,col)
                    if a == row and b == col:
                        row, col = (random.randint(0,19), random.randint(0,15))

            screen.fill("light green")
            draw_grid()  # call function to draw the grid while running
            screen.blit(mole_image, mole_image.get_rect(topleft=(row * 32,col * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

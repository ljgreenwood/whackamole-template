import pygame
import random

square_size = 32
dim = (640,512)
grid = (20,16)

pygame.init()
mole_image = pygame.image.load("./mole.png")
screen = pygame.display.set_mode(dim)  # set the dimensions of the screen object
clock = pygame.time.Clock()  # allows setting the frame rate of the game in conjunction with .flip() in the main program

def draw_grid():
    # The window should be divided into a 20x16 grid of 32x32 squares.
    # (640, 512)
    # draw horizontal lines
    LINE_COLOR = (0, 128, 0) 
    for i in range(1, grid[-1]):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(0, i * square_size),
            end_pos=(dim[0], i * square_size),
        )
    # draw vertical lines
    for i in range(1, grid[0]):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(i * square_size, 0),
            end_pos=(i * square_size, dim[-1]),
        )

def main():
    try:
        row, col = (0,0)  # initial location of mole
        running = True
        while running:  # infinite loop to continue checking for pygame events
            for event in pygame.event.get(): # looping through pygame events (quit and mousebuttondown)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x, y = event.pos # get the position of the mouse event on the surface
                    a, b = (x // square_size, y // square_size)  # finding the row and column values
                    print(f"x : {x}\ny : {y}")  # print statements useful for debugging
                    print(f"a : {a} == row: {row}\nb : {b} == col : {col}") # print statements useful for debugging
                    mole_clicked_flag = (a == row and b == col)  # flag to check if the mole is clicked
                    if mole_clicked_flag:
                        row, col = (random.randrange(0,grid[0]), random.randrange(0,grid[-1]))  # generate new column and row values if the mole is clicked
                    print(f"Move? --> {mole_clicked_flag}")  # print statements useful for debugging

            screen.fill("light green") # color screen object background
            draw_grid()  # call function to draw the grid while running
            screen.blit(mole_image, mole_image.get_rect(topleft=(row * square_size,col * square_size))) # print mole at current location
            pygame.display.flip()  # updates the entire display with modifications to the screen surface
            clock.tick(60)  # limits framerate
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

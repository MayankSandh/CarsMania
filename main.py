import pygame
from copy import deepcopy
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1500, 750
GRID_SIZE = 9
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create a separate section for the draw button
BUTTON_SECTION_HEIGHT = 60
GRID_SECTION_HEIGHT = HEIGHT - BUTTON_SECTION_HEIGHT

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Drawing")

# Grid state
grid = [[WHITE for _ in range(COLS)] for _ in range(ROWS)]
drawing = False
prev_status = False
grid_states = []

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, grid[row][col], (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    pygame.draw.rect(screen, WHITE, (0, GRID_SECTION_HEIGHT, WIDTH, BUTTON_SECTION_HEIGHT))

    drawBtnCoord = 10, GRID_SECTION_HEIGHT + 10
    draw_button = pygame.draw.rect(screen, RED if drawing else BLACK, (drawBtnCoord[0],drawBtnCoord[1], 100, 40))
    font = pygame.font.Font(None, 36)
    text = font.render("Draw", True, WHITE)
    screen.blit(text, (drawBtnCoord[0]+20, drawBtnCoord[1]+5))

    undoBtnCoord = 200, GRID_SECTION_HEIGHT + 10
    undo_button = pygame.draw.rect(screen, BLACK, (undoBtnCoord[0],undoBtnCoord[1], 100, 40))
    font = pygame.font.Font(None, 36)
    text = font.render("Undo", True, WHITE)
    screen.blit(text, (undoBtnCoord[0]+20, undoBtnCoord[1]+5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if draw_button.collidepoint(event.pos):
                    drawing = not drawing
                    if drawing:
                        mouse_pos = pygame.mouse.get_pos()
                        row = mouse_pos[1] // GRID_SIZE
                        col = mouse_pos[0] // GRID_SIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            grid[row][col] = BLACK
                elif undo_button.collidepoint(event.pos):
                    grid = grid_states.pop()
                    draw_grid()

        elif event.type == pygame.MOUSEMOTION and drawing and pygame.mouse.get_pressed()[0]:
            if not prev_status:
                grid_states.append(deepcopy(grid))
                prev_status = True
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // GRID_SIZE
            col = mouse_pos[0] // GRID_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                grid[row][col] = BLACK
        else:
            prev_status = False
    pygame.display.flip()

# Quit Pygame
pygame.quit()

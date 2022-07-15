import pygame

# GAME VARIABLES
WIDTH, HEIGHT = 750, 750
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FPS = 60

# COLORS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# IMAGES
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (45, 45))

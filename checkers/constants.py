import pygame

# GAME VARIABLES
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FPS = 60

# COLORS
BLUE = (92, 158, 255)
RED = (255, 95, 95)
WHITE = (255, 250, 250)
BLACK = (31, 31, 30)

# FONTS
pygame.init()
WINNER_FONT = pygame.font.SysFont("comicsans", 60)

# LOADING IMAGES
BLUE_PIECE = pygame.transform.scale(pygame.image.load("assets/blue-piece.png"), (70, 70))
RED_PIECE = pygame.transform.scale(pygame.image.load("assets/red-piece.png"), (70, 70))
CROWN = pygame.transform.scale(pygame.image.load("assets/king.png"), (45, 45))

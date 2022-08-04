import pygame
from checkers.constants import *
from checkers.checkers import Checkers

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def piece_position(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def display_winner(message, color):
    pygame.time.delay(1000)
    WINDOW.fill(color)
    text = WINNER_FONT.render(message, 1, WHITE)
    WINDOW.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    run = True
    clock = pygame.time.Clock()
    checkers = Checkers(WINDOW)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = piece_position(position)
                checkers.select(row, col)

        checkers.update()

        if checkers.board.red_left == 0:
            display_winner("Blue Won!", BLUE)
            break
        elif checkers.board.blue_left == 0:
            display_winner("Red Won!", RED)
            break

    pygame.quit()

main()
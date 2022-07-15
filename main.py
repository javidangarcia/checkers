import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT, FPS
from board import Board

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def piece_position(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = piece_position(position)
                piece = board.get_piece(row, col)
                board.move_piece(piece, 5, 2)

        board.draw_board(WINDOW)
        pygame.display.update()

    pygame.quit()

main()
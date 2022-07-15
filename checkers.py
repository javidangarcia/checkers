import pygame
from board import Board
from constants import RED, WHITE

class Checkers:
    def __init__(self, window):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.window = window

    def update(self):
        self.board.draw_board(self.window)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if result == False:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move_piece(self.selected, row, col)
            self.change_turn
        else:
            return False
        
        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn == RED

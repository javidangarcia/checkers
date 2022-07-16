from constants import SQUARE_SIZE, CROWN, BLUE, BLUE_PIECE, RED_PIECE

class Piece:
    PADDING = 15
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw_piece(self, window):
        if self.color == BLUE:
            window.blit(BLUE_PIECE, (self.x - BLUE_PIECE.get_width() // 2, self.y - BLUE_PIECE.get_height() // 2))
        else:
            window.blit(RED_PIECE, (self.x - RED_PIECE.get_width() // 2, self.y - RED_PIECE.get_height() // 2))
        
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()
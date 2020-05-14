from piece import Piece
from piece_type import PieceType

class Board:
    def __init__ (self):
        self.pieces = []

        # White pawns (0, 1) to (7, 1)
        for i in range(8):
            piece = Piece(PieceType.PAWN, 0, [i, 1])
            self.pieces.append(piece)

        # Update legal moves for pieces
        for piece in self.pieces:
            piece.updateMoves(self.pieces)

    def update(self):
        pass
    
board = Board()
print(board.pieces[0].pieceType)

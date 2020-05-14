from piece import Piece
from piece_type import PieceType

class Board:
    def __init__ (self):
        self.pieces = []

        # White pawns (0, 1) to (7, 1)
        for i in range(8):
            piece = Piece(PieceType.PAWN, 0, [i, 1])
            self.pieces.append(piece)
        
        # White rooks
        piece = Piece(PieceType.ROOK, 0, [0,0])
        self.pieces.append(piece)
        piece = Piece(PieceType.ROOK, 0, [7,0])
        self.pieces.append(piece)

        # White knights
        piece = Piece(PieceType.KNIGHT, 0, [1,0])
        self.pieces.append(piece)
        piece = Piece(PieceType.KNIGHT, 0, [6,0])
        self.pieces.append(piece)

        # White bishops
        piece = Piece(PieceType.BISHOP, 0, [2,0])
        self.pieces.append(piece)
        piece = Piece(PieceType.BISHOP, 0, [5,0])
        self.pieces.append(piece)

        # White queen
        piece = Piece(PieceType.QUEEN, 0, [3,0]) #Queen is on left
        self.pieces.append(piece)

        # White king
        piece = Piece(PieceType.KING, 0, [4,0]) #King is on right
        self.pieces.append(piece)

        # Black pawns
        for i in range(8):
            piece = Piece(PieceType.PAWN, 1, [i, 6])
            self.pieces.append(piece)

        # Black rooks
        piece = Piece(PieceType.ROOK, 1, [0,7])
        self.pieces.append(piece)
        piece = Piece(PieceType.ROOK, 1, [7,7])
        self.pieces.append(piece)

        # Black knights
        piece = Piece(PieceType.KNIGHT, 1, [1,7])
        self.pieces.append(piece)
        piece = Piece(PieceType.KNIGHT, 1, [6,7])
        self.pieces.append(piece)

        # Black bishops
        piece = Piece(PieceType.BISHOP, 1, [2,7])
        self.pieces.append(piece)
        piece = Piece(PieceType.BISHOP, 1, [5,7])
        self.pieces.append(piece)

        # Black queen
        piece = Piece(PieceType.QUEEN, 1, [4,7]) #Queen is on right
        self.pieces.append(piece)

        # Black king
        piece = Piece(PieceType.KING, 1, [3,7]) #King is on left
        self.pieces.append(piece)

        # Update legal moves for pieces
        self.update()

    def update(self):
        for piece in self.pieces:
            piece.updateMoves(self.pieces)
    
board = Board()
print(board.pieces[0].pieceType)

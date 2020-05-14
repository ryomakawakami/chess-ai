from chess.game.piece_type import PieceType

class Piece:
    def __init__(self, pieceType, color, position):
        self.pieceType = pieceType
        self.color = color
        self.position = position
        self.moves = []

    def updateMoves(self, pieces):
        pass

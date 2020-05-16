from chess.game.piece_type import PieceType

class Piece:
    def __init__(self, pieceType, color):
        self.pieceType = pieceType
        self.color = color
        self.moves = []

    def updateMoves(self, squares, position):
        x, y = position
        self.moves = []
        
        if self.pieceType == PieceType.PAWN:
            if y == 7:
                return

            # 1 square forward
            if squares[x][y + 1] == None:
                self.moves.append((x, y + 1))

            # 2 squares forward (pawn first move or idk)
            if y == 1 and squares[x][y + 1] == None and squares[x][y + 2] == None:
                self.moves.append((x, y + 2))

            # Capture left
            if x > 0 and squares[x - 1][y + 1] != None and squares[x - 1][y + 1].color != self.color:
                self.moves.append((x - 1, y + 1))

            # Capture right
            if x < 7 and squares[x + 1][y + 1] != None and squares[x + 1][y + 1].color != self.color:
                self.moves.append((x + 1, y + 1))

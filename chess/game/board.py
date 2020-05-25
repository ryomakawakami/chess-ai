from chess.game.piece import Piece
from chess.game.piece_type import PieceType

class Board:
    def __init__ (self):
        self.squares = [[None for i in range(8)] for j in range(8)]

        # White pawns (0, 1) to (7, 1)
        for i in range(8):
            self.squares[i][1] = Piece(PieceType.PAWN, 0)
        
        # White rooks on (0, 0) and (7, 0)
        self.squares[0][0] = Piece(PieceType.ROOK, 0)
        self.squares[7][0] = Piece(PieceType.ROOK, 0)

        # White knights on (1, 0) and (6, 0)
        self.squares[1][0] = Piece(PieceType.KNIGHT, 0)
        self.squares[6][0] = Piece(PieceType.KNIGHT, 0)

        # White bishops on (2, 0) and (5, 0)
        self.squares[2][0] = Piece(PieceType.BISHOP, 0)
        self.squares[5][0] = Piece(PieceType.BISHOP, 0)

        # White queen on (3, 0) (queen on left)
        self.squares[3][0] = Piece(PieceType.QUEEN, 0)

        # White king on (4, 0)
        self.squares[4][0] = Piece(PieceType.KING, 0)

        # Black pawns (0, 6) to (7, 6)
        for i in range(8):
            piece = Piece(PieceType.PAWN, 1)
            self.squares[i][6] = piece
        
        # Black rooks on (0, 7) and (7, 7)
        self.squares[0][7] = Piece(PieceType.ROOK, 1)
        self.squares[7][7] = Piece(PieceType.ROOK, 1)

        # Black knights on (1, 7) and (6, 7)
        self.squares[1][7] = Piece(PieceType.KNIGHT, 1)
        self.squares[6][7] = Piece(PieceType.KNIGHT, 1)

        # Black bishops on (2, 7) and (5, 7)
        self.squares[2][7] = Piece(PieceType.BISHOP, 1)
        self.squares[5][7] = Piece(PieceType.BISHOP, 1)

        # White queen on (3, 7) (queen on right)
        self.squares[3][7] = Piece(PieceType.QUEEN, 1)

        # White king on (4, 7)
        self.squares[4][7] = Piece(PieceType.KING, 1)
        
        # Update legal moves for pieces
        self.update()

    def update(self):
        i = 0
        j = 0
        for row in self.squares:
            j = 0
            for piece in row:
                if not piece:
                    j += 1
                    continue
                piece.updateMoves(self.squares, (i, j))
                j += 1
            i += 1


    def isValidMove(self, pieceLocation, move):
        x, y = pieceLocation
        for mov in self.squares[x][y].moves:
            if(move == mov):
                return True

        return False        

    def movePiece(self, oldPos, newPos, color):
        oldX, oldY = oldPos
        newX, newY = newPos
        if(self.squares[oldX][oldY] == None or self.squares[oldX][oldY].color != color):
            print("Error: Piece does not exist or is not on your side.")
        elif(not(self.isValidMove(oldPos, newPos))):
            print("Invalid move.")
        else:
            piece = self.squares[oldX][oldY]
            self.squares[oldX][oldY] = None
            self.squares[newX][newY] = piece



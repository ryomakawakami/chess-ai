from chess.game.piece_type import PieceType

class Piece:
    def __init__(self, pieceType, color):
        self.pieceType = pieceType
        self.color = color
        self.moves = []

    def updateMoves(self, squares, position):
        self.moves = []
        
        if self.pieceType == PieceType.PAWN:
            self.addPawnMoves(squares, position)

        elif self.pieceType == PieceType.ROOK:
            self.addRookMoves(squares, position)

        # see knight_moves.png for option numbering
        elif self.pieceType == PieceType.KNIGHT:
            self.addKnightMoves(squares, position)

        elif self.pieceType == PieceType.BISHOP:
            self.addBishopMoves(squares, position)

        elif self.pieceType == PieceType.QUEEN:
            self.addRookMoves(squares, position)
            self.addBishopMoves(squares, position)

        else:
            self.addKingMoves(squares, position)

    def addPawnMoves(self, squares, position):
        x, y = position

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

    def addRookMoves(self, squares, position):
        x, y = position

        tempX = x
        while tempX < 7:
            nextPiece = squares[tempX + 1][y]

            if nextPiece == None:
                self.moves.append((tempX + 1, y))
                tempX += 1
                continue

            if nextPiece.color == self.color:
                break

            self.moves.append((tempX + 1, y))
            break

        tempX = x
        while tempX > 0:
            nextPiece = squares[tempX - 1][y]
            
            if nextPiece == None:
                self.moves.append((tempX - 1, y))
                tempX -= 1
                continue

            if nextPiece.color == self.color:
                break

            self.moves.append((tempX - 1, y))
            break

        tempY = y
        while tempY < 7:
            nextPiece = squares[x][tempY + 1]

            if nextPiece == None:
                self.moves.append((x, tempY + 1))
                tempY += 1
                continue

            if nextPiece.color == self.color:
                break

            self.moves.append((x, tempY + 1))
            break

        tempY = y
        while tempY > 0:
            nextPiece = squares[x][tempY - 1]

            if nextPiece == None:
                self.moves.append((x, tempY - 1))
                tempY -= 1
                continue

            if nextPiece.color == self.color:
                break

            self.moves.append((x, tempY - 1))
            break
    
    def addKnightMoves(self, squares, position):
        x, y = position

        # option 1
        if x < 7 and y < 6:
            if squares[x + 1][y + 2] == None or squares[x + 1][y + 2].color != self.color:
                self.moves.append((x + 1, y + 2))

        # option 2
        if x < 6 and y < 7:
            if squares[x + 2][y + 1] == None or squares[x + 2][y + 1].color != self.color:
                self.moves.append((x + 2, y + 1))
        
        # option 3
        if x < 6 and y > 0:
            if squares[x + 2][y - 1] == None or squares[x + 2][y - 1].color != self.color:
                self.moves.append((x + 2, y - 1))

        # option 4
        if x < 7 and y > 1:
            if squares[x + 1][y - 2] == None or squares[x + 1][y - 2].color != self.color:
                self.moves.append((x + 1, y - 2))
        
        # option 5
        if x > 0 and y > 1:
            if squares[x - 1][y - 2] == None or squares[x - 1][y - 2].color != self.color:
                self.moves.append((x - 1, y - 2))
        
        # option 6
        if x > 1 and y > 0:
            if squares[x - 2][y - 1] == None or squares[x - 2][y - 1].color != self.color:
                self.moves.append((x - 2, y - 1))

        # option 7
        if x > 1 and y < 7:
            if squares[x - 2][y + 1] == None or squares[x - 2][y + 1].color != self.color:
                self.moves.append((x - 2, y + 1))
        
        # option 8
        if x > 0 and y < 6:
            if squares[x - 1][y + 2] == None or squares[x - 1][y + 2].color != self.color:
                self.moves.append((x - 1, y + 2))

    def addBishopMoves(self, squares, position):
        return

    def addKingMoves(self, squares, position):
        return

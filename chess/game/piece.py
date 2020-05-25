from chess.game.piece_type import PieceType

class Piece:
    def __init__(self, pieceType, color):
        self.pieceType = pieceType
        self.color = color
        self.moves = []

    def updateMoves(self, squares, attacks, position):
        self.moves = []
        
        if self.pieceType == PieceType.PAWN:
            self.addPawnMoves(squares, attacks, position)

        elif self.pieceType == PieceType.ROOK:
            self.addRookMoves(squares, attacks, position)

        # see knight_moves.png for option numbering
        elif self.pieceType == PieceType.KNIGHT:
            self.addKnightMoves(squares, attacks, position)

        elif self.pieceType == PieceType.BISHOP:
            self.addBishopMoves(squares, attacks, position)

        elif self.pieceType == PieceType.QUEEN:
            self.addRookMoves(squares, attacks, position)
            self.addBishopMoves(squares, attacks, position)

        else:
            self.addKingMoves(squares, attacks, position)

    def addRookAttacks(self, squares, attacks, position):
        x, y = position
        attackVal = 1
        if(self.color == 1):
            attackVal*=100
        tempX = x
        while tempX < 7:
            nextPiece = squares[tempX + 1][y]

            if (nextPiece == None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.ROOK) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX+1][y]+= attackVal
                tempX += 1
                continue

            attacks[tempX+1][y]+=attackVal
            break

        tempX = x
        while tempX > 0:
            nextPiece = squares[tempX - 1][y]
            
            if (nextPiece == None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.ROOK) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX-1][y]+= attackVal
                tempX -= 1
                continue

            attacks[tempX-1][y]+=attackVal
            break

        tempY = y
        while tempY < 7:
            nextPiece = squares[x][tempY + 1]

            if (nextPiece == None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.ROOK) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[x][tempY+1]+= attackVal
                tempY += 1
                continue

            attacks[x][tempY+1]+=attackVal
            break

        tempY = y
        while tempY > 0:
            nextPiece = squares[x][tempY - 1]

            if (nextPiece == None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.ROOK) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[x][tempY-1]+= attackVal
                tempY -= 1
                continue

            attacks[x][tempY-1]+=attackVal
            break

    def addBishopAttacks(self, squares, attacks, position):
        x, y = position
        
        tempX = x
        tempY = y

        attackVal = 1
        if(self.color == 1):
            attackVal*=100
        
        while(tempX <7 and tempY <7):
            nextPiece = squares[tempX+1][tempY+1]
            if(nextPiece== None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.BISHOP) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX+1][tempY+1]+=attackVal
                tempX+=1
                tempY+=1
                continue
            attacks[tempX+1][tempY+1]+= attackVal
            break
        tempX = x
        tempY = y
        while(tempX <7 and tempY >0):
            nextPiece = squares[tempX+1][tempY-1]
            if(nextPiece== None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.BISHOP) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX+1][tempY-1]+=attackVal
                tempX+=1
                tempY-=1
                continue
            attacks[tempX+1][tempY-1]+=attackVal
            break
        tempX = x
        tempY = y
        while(tempX >0 and tempY <7):
            nextPiece = squares[tempX-1][tempY+1]
            if(nextPiece== None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.BISHOP) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX+1][tempY-1]+=attackVal
                tempX-=1
                tempY+=1
                continue
            attacks[tempX-1][tempY+1]+=attackVal
            break
        tempX = x
        tempY = y
        while(tempX >0 and tempY >0):
            nextPiece = squares[tempX-1][tempY-1]
            if(nextPiece== None or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.BISHOP) or (nextPiece.color == self.color and nextPiece.pieceType == PieceType.QUEEN)):
                attacks[tempX-1][tempY-1]+=attackVal
                tempX-=1
                tempY-=1
                continue
            attacks[tempX-1][tempY-1]+=attackVal
            break
        tempX = x
        tempY = y      
        return

    def addPawnMoves(self, squares, attacks, position):
        x, y = position

        
        if self.color == 0:
            if(x > 0):
                attacks[x-1][y+1]+=1
            if(x < 7):    
                attacks[x+1][y+1]+=1
            if y == 7:
                return
        elif self.color == 1:
            if(x > 0):
            
                attacks[x-1][y-1]+=100
            if(x < 7):
                attacks[x+1][y-1]+=100
            if(y == 0):
                return

        fwd = 1
        if self.color == 1:
            fwd = -1

        # 1 square forward
        if squares[x][y + fwd] == None:
            self.moves.append((x, y + fwd))

        # 2 squares forward (pawn first move or idk)
        if (y == 1 and self.color == 0) or (y == 6 and self.color == 1):
            if squares[x][y + fwd] == None and squares[x][y + 2 * fwd] == None:
                self.moves.append((x, y + 2 * fwd))

        # Capture left
        if x > 0 and squares[x - 1][y + fwd] != None and squares[x - 1][y + fwd].color != self.color:
            self.moves.append((x - 1, y + fwd))

        # Capture right
        if x < 7 and squares[x + 1][y + fwd] != None and squares[x + 1][y + fwd].color != self.color:
            self.moves.append((x + 1, y + fwd))

    def addRookMoves(self, squares, attacks, position):
        x, y = position
        self.addRookAttacks(squares, attacks, position)
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
    
    def addKnightMoves(self, squares, attacks, position):
        x, y = position

        #Attack val is 1 for whites, multiply by 100 if black.
        #Attacks are same as moves, regardless.
        attackVal = 1
        if(self.color == 1):
            attackVal*=100
        
        # option 1
        if x < 7 and y < 6:
            if squares[x + 1][y + 2] == None or squares[x + 1][y + 2].color != self.color:
                self.moves.append((x + 1, y + 2))
                attacks[x + 1][y + 2]+= attackVal

        # option 2
        if x < 6 and y < 7:
            if squares[x + 2][y + 1] == None or squares[x + 2][y + 1].color != self.color:
                self.moves.append((x + 2, y + 1))
                attacks[x + 2][y + 1]+= attackVal
        
        # option 3
        if x < 6 and y > 0:
            if squares[x + 2][y - 1] == None or squares[x + 2][y - 1].color != self.color:
                self.moves.append((x + 2, y - 1))
                attacks[x + 2][y - 1]+= attackVal

        # option 4
        if x < 7 and y > 1:
            if squares[x + 1][y - 2] == None or squares[x + 1][y - 2].color != self.color:
                self.moves.append((x + 1, y - 2))
                attacks[x + 1][y - 2]+= attackVal
        
        # option 5
        if x > 0 and y > 1:
            if squares[x - 1][y - 2] == None or squares[x - 1][y - 2].color != self.color:
                self.moves.append((x - 1, y - 2))
                attacks[x - 1][y - 2]+= attackVal
        
        # option 6
        if x > 1 and y > 0:
            if squares[x - 2][y - 1] == None or squares[x - 2][y - 1].color != self.color:
                self.moves.append((x - 2, y - 1))
                attacks[x - 2][y - 1]+= attackVal

        # option 7
        if x > 1 and y < 7:
            if squares[x - 2][y + 1] == None or squares[x - 2][y + 1].color != self.color:
                self.moves.append((x - 2, y + 1))
                attacks[x - 2][y + 1]+= attackVal
        
        # option 8
        if x > 0 and y < 6:
            if squares[x - 1][y + 2] == None or squares[x - 1][y + 2].color != self.color:
                self.moves.append((x - 1, y + 2))
                attacks[x - 1][y + 2]+= attackVal        

    def addBishopMoves(self, squares, attacks, position):
        self.addBishopAttacks(squares, attacks, position)

        x, y = position

        offset = 0
        while x + offset < 7 and y + offset < 7:
            nextPiece = squares[x + offset + 1][y + offset + 1]
            if nextPiece == None:
                offset += 1
                self.moves.append((x + offset, y + offset))
                continue
            if nextPiece.color == self.color:
                break
            offset += 1
            self.moves.append((x + offset, y + offset))
            break

        offset = 0
        while x + offset < 7 and y - offset > 0:
            nextPiece = squares[x + offset + 1][y - offset - 1]
            if nextPiece == None:
                offset += 1
                self.moves.append((x + offset, y - offset))
                continue
            if nextPiece.color == self.color:
                break
            offset += 1
            self.moves.append((x + offset, y - offset))
            break

        offset = 0
        while x - offset > 0 and y + offset < 7:
            nextPiece = squares[x - offset - 1][y + offset + 1]
            if nextPiece == None:
                offset += 1
                self.moves.append((x - offset, y + offset))
                continue
            if nextPiece.color == self.color:
                break
            offset += 1
            self.moves.append((x - offset, y + offset))
            break

        offset = 0
        while x - offset > 0 and y - offset > 0:
            nextPiece = squares[x - offset - 1][y - offset - 1]
            if nextPiece == None:
                offset += 1
                self.moves.append((x - offset, y - offset))
                continue
            if nextPiece.color == self.color:
                break
            offset += 1
            self.moves.append((x - offset, y - offset))
            break

    def addKingMoves(self, squares, attacks, position):

        x, y = position
        attackVal = 1
        if(self.color == 1):
            attackVal*=100
        
        if x > 0:
            if squares[x - 1][y] == None or squares[x - 1][y].color != self.color:
                self.moves.append((x - 1, y))
                attacks[x - 1][y]+= attackVal
                    

            if y > 0:
                if squares[x - 1][y - 1] == None or squares[x - 1][y - 1].color != self.color:
                    self.moves.append((x - 1, y - 1))
                    attacks[x - 1][y - 1]+= attackVal

            if y < 7:
                if squares[x - 1][y + 1] == None or squares[x - 1][y + 1].color != self.color:
                    self.moves.append((x - 1, y + 1))
                    attacks[x - 1][y + 1]+= attackVal

        if x < 7:
            if squares[x + 1][y] == None or squares[x + 1][y].color != self.color:
                self.moves.append((x + 1, y))
                attacks[x + 1][y]+= attackVal

            if y > 0:
                if squares[x + 1][y - 1] == None or squares[x + 1][y - 1].color != self.color:
                    self.moves.append((x + 1, y - 1))
                    attacks[x + 1][y - 1]+= attackVal

            if y < 7:
                if squares[x + 1][y + 1] == None or squares[x + 1][y + 1].color != self.color:
                    self.moves.append((x + 1, y + 1))
                    attacks[x + 1][y + 1]+= attackVal

        if y > 0:
            if squares[x][y - 1] == None or squares[x][y - 1].color != self.color:
                self.moves.append((x, y - 1))
                attacks[x][y - 1]+= attackVal

        if y < 7:
            if squares[x][y + 1] == None or squares[x][y + 1].color != self.color:
                self.moves.append((x, y + 1))
                attacks[x][y + 1]+= attackVal
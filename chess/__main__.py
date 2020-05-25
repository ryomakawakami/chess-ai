from chess.game.board import Board
from chess.game.piece import Piece
from chess.game.piece_type import PieceType

if __name__ == "__main__":
    board = Board()

    print(board.squares[4][1].moves)
    oldCoords = (4, 1)
    newCoords = (4, 3)
    board.movePiece(oldCoords, newCoords, 0)
    oldCoords = (4,1)
    board.movePiece(oldCoords, newCoords, 0)

    board.update()
    
    board.display()
    print(board.squares[5][0].moves)
            
from chess.game.board import Board
from chess.game.piece import Piece
from chess.game.piece_type import PieceType

if __name__ == "__main__":
    board = Board()

    print(board.squares[5][1].moves)
    oldCoords = (5, 1)
    newCoords = (5, 3)
    board.movePiece(oldCoords, newCoords, 0)
    oldCoords = (5,1)
    board.movePiece(oldCoords, newCoords, 0)

    board.display()
            
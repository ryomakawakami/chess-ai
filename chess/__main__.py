from chess.game.board import Board
from chess.game.piece import Piece
from chess.game.piece_type import PieceType

if __name__ == "__main__":
    board = Board()

    print(board.squares[0][6].moves)

    for row in board.squares:
        rowText = ""
        for piece in row:
            if not piece:
                rowText += "~ "
                continue
            t = piece.pieceType
            color = piece.color
            if t == PieceType.PAWN:
                if color == 0:
                    rowText += "♙"
                else:
                    rowText += "♟"
            elif t == PieceType.ROOK:
                if color == 0:
                    rowText += "♖"
                else:
                    rowText += "♜"
            elif t == PieceType.KNIGHT:
                if color == 0:
                    rowText += "♘"
                else:
                    rowText += "♞"
            elif t == PieceType.BISHOP:
                if color == 0:
                    rowText += "♗"
                else:
                    rowText += "♝"
            elif t == PieceType.QUEEN:
                if color == 0:
                    rowText += "♕"
                else:
                    rowText += "♛"
            else:
                if color == 0:
                    rowText += "♔"
                else:
                    rowText += "♚"

            rowText += " "
        print(rowText)

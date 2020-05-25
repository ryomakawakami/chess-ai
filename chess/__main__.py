from chess.game.board import Board
from chess.game.piece import Piece
from chess.game.piece_type import PieceType
from chess.game.gameSession import GameSession

def displayBoard(board):
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


if __name__ == "__main__":
    board = Board()
    displayBoard(board)
    gameSesh = GameSession()
    gameSesh.game()

            
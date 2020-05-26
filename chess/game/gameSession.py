# -*- coding: utf-8 -*-
import sys
from chess.game.board import Board
from chess.game.piece import Piece
from chess.game.piece_type import PieceType
class GameSession:

    def __init__(self):
        self.turn = 0
        self.gameOn = True


    def displayBoard(self, board):
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

    def game(self):
        board = Board()
        self.displayBoard(board)
        while(self.gameOn):
            print("\n\n\n")
            self.displayBoard(board)
            while(True):
                print("Input piece to move [x,y]: ")
                currentPiece = input().split(' ')
                print("Input where to move [x,y]:")
                movePiece = tuple(input().split(' '))
                if(board.movePiece(currentPiece, movePiece, self.turn)):
                    break
            self.turn = 1-self.turn
            board.update()

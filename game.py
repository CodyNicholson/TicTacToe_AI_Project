import random
from player import Player
from board import Board
from cell import Cell

class Game:
    def __init__(self):
        self.board = Board()
        self.initializeGame()
        self.displayBoard()
        self.makeFirstMove()
        self.playGame()
        self.checkStatus()
    
    def checkStatus(self):
        if self.board.isWinning(Player.COMPUTER):
	        print("Computer has won")
        elif self.board.isWinning(Player.USER):
	        print("Player has won")
        else:
            print("It's a draw!")
            
    def playGame(self):
        while self.board.isRunning():
            print("User move: ")
            userCell:Cell = Cell(self.board.getScanner().nextInt(), self.board.getScanner().nextInt())
            self.board.move(userCell, Player.USER)
            self.board.displayBoard()
            if (~board.isRunning()):
                break
            self.board.callMinimax(0, Player.COMPUTER)
            for cell in board.getRootValues():
                print("Cell values: " + cell + " minimaxValue: " + cell.getMinimaxValue())
            self.board.move(board.getBestMove(), Player.COMPUTER)
            self.board.displayBoard()
            
    def makeFirstMove(self):
        print("Who starts? 1 - Computer ; 2 - User")
        choice:int = self.board.getScanner().nextInt()
        if choice == 1:
	        cell:Cell = Cell(random.nextInt(3), random.nextInt(3))
	        self.board.move(cell, self.player.COMPUTER)
	        self.board.displayBoard()

    def displayBoard(self):
        board.displayBoard()
        
    def initializeGame(self):
        this.board = Board()
        this.board.setupBoard()

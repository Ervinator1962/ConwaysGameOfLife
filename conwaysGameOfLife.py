import random
import copy
from os import system, name
from time import sleep 
from conwaysGameBoardGenerator import BoardGenerator
from math import ceil

class GameOfLife():
	size = 40
	freq = 0.05
	def __init__(self, size):
		self.size = size
		self.currPixels = self.createBoard(self.size)
		self.nextPixels = self.createBoard(self.size)

	def runGame(self):
		while True:
			self.printStuff(self.currPixels)
			self.runRound()

	def createBoard(self, size):
		return [[1 for j in range(self.size)] for i in range(self.size)]

	def printAddress(self, object):
		print(object.__repr__())

	def runRound(self):
		#self.printAddress(self.currPixels)
		#self.printAddress(self.nextPixels)
		for i in range(self.size):
			for j in range(self.size):
				alive = self.numAlive(i, j, self.currPixels)
				#print(i, j, alive)
				if self.currPixels[i][j] == 0:
					if alive == 3:
						self.nextPixels[i][j] = 1
					else:
						self.nextPixels[i][j] = 0
				else:
					if alive < 2 or alive > 3:
						self.nextPixels[i][j] = 0
					else:
						self.nextPixels[i][j] = 1

		temp = self.currPixels
		self.currPixels = self.nextPixels
		self.nextPixels = temp

	def setBoard(self, size, pixels):
		self.size = size
		self.currPixels = pixels

	def numAlive(self, i, j, pixels):
		alive = 0
		for a in range(-1, 2):
			for b in range (-1, 2):
				x, y = i + a, j + b
				#print(x, y)
				if self.isValid(x, y) and (x != i or y != j) and pixels[x][y] == 1:
					alive += 1

		return alive

	def isValid(self, i, j):
		return (0 <= i < self.size) and (0 <= j < self.size)

	def printStuff(self, pixels):
		self.clearScreen()
		for i in range(self.size):
			for j in range(self.size):
				if pixels[i][j] == 0:
					print("+", end="")
				else:
					print("#", end="")
			print()
		print()
		sleep(GameOfLife.freq)
		
	def clearScreen(self):
		# for windows
		if name == 'nt':
			_ = system('cls')

	def randomiseBoard(self):
		random.seed()
		for i in range(self.size):
			for j in range(self.size):
				self.currPixels[i][j] = random.randint(0, 1)

def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')

def main():
	#print("Hello world")
	#sleep(3)
	#clear()
	size = 44
	boardGenerator = BoardGenerator(size)
	i, j = 12, 20
	shapeSize = 20
	#boardGenerator.setIsoscelesTriangle(i, j, BoardGenerator.UP, shapeSize)
	#boardGenerator.setIsoscelesTriangle(i + shapeSize, j, BoardGenerator.UP, shapeSize)
	#boardGenerator.setIsoscelesTriangle(i + 2 * shapeSize, j,  BoardGenerator.UP, shapeSize)
	#boardGenerator.setIsoscelesTriangle(i, j + shapeSize + 1, BoardGenerator.UP, shapeSize)
	#boardGenerator.setIsoscelesTriangle(i + shapeSize, j + shapeSize + 1, BoardGenerator.UP, shapeSize)
	#boardGenerator.setIsoscelesTriangle(i + 2 * shapeSize, j + shapeSize + 1, BoardGenerator.UP, shapeSize)
	
	#boardGenerator.setDiamond(BoardGenerator.ON, i, j, shapeSize)
	#boardGenerator.setDiamond(BoardGenerator.ON, i + shapeSize, j, shapeSize)
	#boardGenerator.setDiamond(BoardGenerator.ON, i, j + shapeSize, shapeSize)
	#boardGenerator.setDiamond(BoardGenerator.ON, i + shapeSize, j + shapeSize, shapeSize)
	
	boardGenerator.setHollowDiamond(BoardGenerator.ON, i, j, shapeSize, shapeSize - 4)
	innerDiamondSize = 12
	boardGenerator.setHollowDiamond(BoardGenerator.ON, i + ceil((shapeSize - innerDiamondSize)/2), j, innerDiamondSize, 8)
	#boardGenerator.printStuff()
	sleep(1)
	game = GameOfLife(size)
	game.randomiseBoard()
	#game.setBoard(size, boardGenerator.getBoard())
	game.runGame()

main()



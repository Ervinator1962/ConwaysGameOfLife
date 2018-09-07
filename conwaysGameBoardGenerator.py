from math import ceil

class BoardGenerator():
	ON = 1
	OFF = 0

	UP = "up"
	DOWN = "down"
	LEFT = "left"
	RIGHT = 'right'

	def __init__(self, size):
		print("Creating board generator")
		self.size = size
		self.board = self.createBoard(self.size)

	def isValid(self, i, j):
		return (0 <= i < self.size) and (0 <= j < self.size)

	def setBoardPiece(self, i, j, val):
		if self.isValid(i, j):
			self.board[i][j] = val

	#adds triangle shape
	def setRightAngleTriangle(self, state, i, j, vert, hori, size):
		for a in range(size):
			for b in range(a + 1):
				if vert == BoardGenerator.UP:
					if hori == BoardGenerator.LEFT:
						self.setBoardPiece(i + a, j + b - a, state)
					else:
						self.setBoardPiece(i + a, j + b, state)
				else:
					offset = 2 * (size - 1)
					if hori == BoardGenerator.LEFT:
						self.setBoardPiece(i + offset - a, j + b - a, state)
					else:
						self.setBoardPiece(i + offset - a, j + b, state)

	def oppositeState(self, state):
		if state == BoardGenerator.ON:
			return BoardGenerator.OFF
		else:
			BoardGenerator.ON

	def setIsoscelesTriangle(self, state, i, j, vert, size):
		offset = 0
		if size % 2 == 0:
			offset = 1
		size = ceil(size/2)
		self.setRightAngleTriangle(state, i, j, vert, BoardGenerator.LEFT, size)
		self.setRightAngleTriangle(state, i, j + offset, vert, BoardGenerator.RIGHT, size)

	def setDiamond(self, state, i, j, size):
		self.setIsoscelesTriangle(state, i, j, BoardGenerator.UP, size)
		self.setIsoscelesTriangle(state, i, j, BoardGenerator.DOWN, size)

	def setHollowDiamond(self, state, i, j, size, innersize):
		offset = ceil((size - innersize)/2)
		self.setDiamond(state, i, j, size)
		self.setDiamond(self.oppositeState(state), i + offset, j, innersize)

	def setSquare(self, state, i, j, size):
		for a in range(size):
			for b in range(size):
				self.setBoardPiece(i + a, j + b, state)

	def createBoard(self, size):
		return [[0 for j in range(self.size)] for i in range(self.size)]
 
	def printStuff(self):
		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] == 0:
					print("+", end="")
				else:
					print("#", end="")
			print()
		print()

	def getBoard(self):
		return self.board

def main():
	print("Starting program")
	boardGenerator = BoardGenerator(6)
	boardGenerator.printStuff()
	boardGenerator.addTriangle(0, 1)
	boardGenerator.printStuff()
	boardGenerator.addSquare(4, 4)
	boardGenerator.printStuff()

if __name__=="__main__":
	main()
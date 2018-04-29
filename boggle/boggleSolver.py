import sys
import random

class Tile:
    def __init__(self, char):
        self.touch = 0
        self.char = char

def main(argv):
    size = int(argv.pop(1))
    board = initBoard(size)
    printBoard(board, size)

#desc:   created  the board of a given size, initalizes board with tiles and letters
#params: size - given size of the board
#return: list of lists populated with tiles (and tiles populated)
def initBoard(size):
    #initalize i and j first, so that first for loop board-code will reference without breaking
    n = 0
    i, j = 0, 0
    board = []
    for i in range(size):
        inner = []
        for j in range(size):
            letter = str(chr(random.randint(97,122)))
            tile = Tile(letter)
            inner.append(tile)
            n += 1 
        board.append(inner)
    return board

#desc:    prints out the current state of a board
#params:  board - list of lists containing tile objects
#returns: void
def printBoard(board, size):
    n = 0;
    i, j = 0, 0
    for i in range(size):
        #print(board[_][0].char,end=' ')
        for j in range(size):
            if(n%size == 0 and n != 0):
                print()
            print(board[i][j].char,end=' ')
            n += 1
    print()

if __name__ == "__main__":
    main(sys.argv)

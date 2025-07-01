import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def save(self):
        '''Save game to default .dat file'''
        oxo_data.saveGame(self.board)

    def load(self):
        '''Restore game from default .dat file'''
        try:
            restored = oxo_data.restoreGame()
            self.board = restored if len(restored) == 9 else [" "] * 9
        except IOError:
            self.board = [" "] * 9

    def saveToFile(self, path):
        '''Save game to custom file'''
        with open(path, 'w') as f:
            f.write(''.join(self.board))

    def loadFromFile(self, path):
        '''Load game from custom file'''
        with open(path, 'r') as f:
            data = f.read().strip()
            self.board = list(data) if len(data) == 9 else [" "] * 9

    def _generateMove(self):
        options = [i for i, cell in enumerate(self.board) if cell == " "]
        return random.choice(options) if options else -1

    def _isWinningMove(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            line = self.board[a] + self.board[b] + self.board[c]
            if line == 'XXX' or line == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.board[cell] != ' ':
            return None
        self.board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        elif " " not in self.board:
            return 'D'
        return ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        elif " " not in self.board:
            return 'D'
        return ""

    def printBoard(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()


# Optional test/demo
if __name__ == "__main__":
    game = Game()
    result = ""
    while not result:
        game.printBoard()
        move = game._generateMove()
        result = game.userMove(move)
        if result is None:
            continue
        if not result:
            result = game.computerMove()
    game.printBoard()
    print("It's a draw!" if result == 'D' else f"Winner is: {result}")

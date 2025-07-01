import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def save(self):
        '''Save game state to disk using oxo_data'''
        oxo_data.saveGame(self.board)

    def load(self):
        '''Restore game state from file'''
        try:
            restored = oxo_data.restoreGame()
            self.board = restored if len(restored) == 9 else [" "] * 9
        except IOError:
            self.board = [" "] * 9

    def _generateMove(self):
        '''Generate a random valid move for computer'''
        options = [i for i, cell in enumerate(self.board) if cell == " "]
        return random.choice(options) if options else -1

    def _isWinningMove(self):
        '''Check if a player has a winning line'''
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in wins:
            line = self.board[a] + self.board[b] + self.board[c]
            if line == 'XXX' or line == 'OOO':
                return True
        return False

    def userMove(self, cell):
        '''Process user's move at specified cell'''
        if self.board[cell] != ' ':
            return None  # Invalid move
        self.board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        elif " " not in self.board:
            return 'D'
        return ""  # Game continues

    def computerMove(self):
        '''Perform computer's move and return result'''
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        elif " " not in self.board:
            return 'D'
        return ""  # Game continues

    def printBoard(self):
        '''Print board to console for testing/debugging'''
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()

# Optional test runner
if __name__ == "__main__":
    game = Game()
    result = ""
    while not result:
        game.printBoard()
        user_cell = game._generateMove()
        result = game.userMove(user_cell)
        if result is None:
            continue
        if not result:
            result = game.computerMove()
    game.printBoard()
    if result == 'D':
        print("It's a draw!")
    else:
        print("Winner is:", result)

'''
This is the main logic for a Tic-tac-toe game.
It is not optimized for a smart AI—it generates random moves
and checks for winning lines. Exposed functions are:
    - newGame()
    - saveGame()
    - restoreGame()
    - userMove()
    - computerMove()
'''

import os
import random
import oxo_data

def newGame():
    '''Return a new empty game board'''
    return list(" " * 9)

def saveGame(game):
    '''Save game state to disk'''
    oxo_data.saveGame(game)

def restoreGame():
    '''Restore previously saved game. If invalid, return a new game'''
    try:
        game = oxo_data.restoreGame()
        return game if len(game) == 9 else newGame()
    except IOError:
        return newGame()

def _generateMove(game):
    '''Generate a random move from available cells. Return -1 if full'''
    options = [i for i, cell in enumerate(game) if cell == " "]
    return random.choice(options) if options else -1

def _isWinningMove(game):
    '''Check if current board has a winning line'''
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in wins:
        line = game[a] + game[b] + game[c]
        if line == 'XXX' or line == 'OOO':
            return True
    return False

def userMove(game, cell):
    '''Attempt to make a user move. Return result or None if invalid.'''
    if game[cell] != ' ':
        return None  # Invalid move
    game[cell] = 'X'
    if _isWinningMove(game):
        return 'X'
    elif " " not in game:
        return 'D'  # Draw
    return ""  # Game continues

def computerMove(game):
    '''Generate a computer move and return the result'''
    cell = _generateMove(game)
    if cell == -1:
        return 'D'  # Draw if no move left
    game[cell] = 'O'
    if _isWinningMove(game):
        return 'O'
    elif " " not in game:
        return 'D'  # Draw
    return ""  # Game continues

# Optional test runner
def test():
    result = ""
    game = newGame()
    while not result:
        print(game)
        result = userMove(game, _generateMove(game))
        if result is None:
            continue  # Try again
        if not result:
            result = computerMove(game)
        if result == 'D':
            print("It's a draw!")
        elif result in ['X', 'O']:
            print("Winner is:", result)
        print(game)

if __name__ == "__main__":
    test()

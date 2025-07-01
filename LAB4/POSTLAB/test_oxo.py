import unittest
from oxo_logic import Game


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Initialize a new game before each test"""
        self.game = Game()

    def test_empty_board(self):
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move_valid(self):
        result = self.game.userMove(0)
        self.assertEqual(self.game.board[0], 'X')
        self.assertIn(result, ["", "X", "D"])

    def test_user_move_invalid(self):
        self.game.board[0] = 'O'
        result = self.game.userMove(0)
        self.assertIsNone(result)

    def test_computer_move(self):
        result = self.game.computerMove()
        self.assertIn(result, ["", "O", "D"])
        self.assertIn("O", self.game.board)

    def test_winning_move(self):
        self.game.board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        result = self.game.userMove(2)
        self.assertEqual(result, 'X')

    def test_draw_condition(self):
        self.game.board = ['X', 'O', 'X',
                           'X', 'O', 'O',
                           'O', 'X', ' ']
        result = self.game.userMove(8)
        self.assertEqual(result, 'D')
if __name__ == '__main__':
    unittest.main()

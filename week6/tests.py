import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', '.', 'O'],
            ['.', 'X', '.'],
            ['.', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        board = [
            ['X', '.', 'O'],
            ['X', 'X', 'X'],
            ['.', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        board = [
            ['X', '.', 'O'],
            ['.', 'O', '.'],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
        board = [
            ['O', '.', 'O'],
            ['O', 'X', '.'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_make_empty_board(self):
        board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(board, logic.make_empty_board())
    
    def test_other_player(self):
        self.assertEqual("X", logic.other_player("O"));
        self.assertEqual("O", logic.other_player("X"));
    


if __name__ == '__main__':
    unittest.main()

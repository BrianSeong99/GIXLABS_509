import unittest
import logic
from unittest.mock import patch

import pandas as pd

class TestLogic(unittest.TestCase):

    def test_board(self):
        board = logic.Board()
        self.assertEqual(str(board), '...\n...\n...\n')
        board.rows = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.get(0,0), 'X')
        board.set(0, 1, 'O')
        self.assertEqual(board.get(0,1), 'O')
        self.assertEqual(board.get(1,0), None)
        board.rows = [
            ['X', 'X', 'X'],
            ['O', 'X', None],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'X')
        board.rows = [
            ['O', 'X', None],
            ['X', 'X', 'X'],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'X')
        board.rows = [
            ['O', 'X', None],
            ['O', None, 'O'],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(board.get_winner(), 'X')
        board.rows = [
            ['O', 'X', 'X'],
            ['O', 'X', None],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'O')
        board.rows = [
            ['O', 'O', 'X'],
            ['X', 'O', None],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(board.get_winner(), 'O')
        board.rows = [
            ['X', 'X', 'O'],
            [None, 'X', 'O'],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'O')
        board.rows = [
            ['O', 'X', 'X'],
            ['O', 'X', None],
            ['X', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'X')
        board.rows = [
            ['O', 'X', 'X'],
            ['X', 'O', None],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.get_winner(), 'O')
        board.rows = [
            ['O', 'X', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(board.is_board_filled(), True)
        board.rows = [
            ['O', 'X', 'X'],
            ['O', 'X', None],
            ['O', None, 'O'],
        ]
        self.assertEqual(board.is_board_filled(), False)
        self.assertEqual(board.get_row_size(), 3)
        self.assertEqual(board.get_col_size(), 3)
    
    def test_player(self):
        player = logic.Player("P", "Player")
        self.assertEqual(player.get_symbol(), "P")
        self.assertEqual(player.get_type(), "Player")
    
    def test_human(self):
        player_x = logic.Human('X')
        self.assertEqual(player_x.get_symbol(), 'X')
        self.assertEqual(player_x.get_type(), 'Human')
    
    def test_bot(self):
        board = logic.Board()
        player_x = logic.Bot('O')
        self.assertEqual(player_x.get_symbol(), 'O')
        self.assertEqual(player_x.get_type(), 'Bot')
    
    def test_game(self):
        game = logic.Game(logic.Human('X'), logic.Human('O'))
        game.next_player()
        self.assertEqual(game.current_player, 'X')

if __name__ == '__main__':
    unittest.main()

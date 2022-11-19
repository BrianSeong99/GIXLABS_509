# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    if not board:
        raise ValueError("No inputs given.")

    if len(board) != 3 or len(board[0]) != 3:
        raise IndexError("Board does not conform to the right dimensions of a 3x3 matrix.")

    if not all([element in ["X", "O", '.'] for row in board for element in row]):
        raise ValueError("Board contains one or more entries that is neither 'X' nor 'O'.")

    winner = ""
    if board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
        return winner
    if board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
        return winner
    if board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
        return winner
    if board[0][0] == board[0][1] == board[0][2]:
        winner = board[0][0]
        return winner
    if board[1][0] == board[1][1] == board[1][2]:
        winner = board[1][1]
        return winner
    if board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
        return winner
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
    return winner

def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'X' if player == 'O' else 'O'

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

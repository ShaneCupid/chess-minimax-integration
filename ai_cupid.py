# This file imports the 
# Minimax functionality and uses it to determine the best move for the AI

import chess
from minimax_cupid import get_best_move

def get_ai_move(board, depth):
    """
    Get the best move for the AI.
    Args:
        board (ChessBoard): The current state of the chess board.
        depth (int): The depth to which the Minimax algorithm should explore.
    Returns:
        chess.Move: The best move found for the AI.
    """
    return get_best_move(board, depth)

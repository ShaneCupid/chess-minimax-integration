#This file contains the Minimax algorithm and the evaluation function
# Contains the Minimax algorithm and board evaluation function

import chess
import math

MAX, MIN = math.inf, -math.inf

def minimax(board, depth, alpha, beta, maximizingPlayer):
    """
    Minimax algorithm with alpha-beta pruning.
    Args:
        board (ChessBoard): The current state of the chess board.
        depth (int): The depth to which the algorithm should explore.
        alpha (float): The best value that the maximizing player can guarantee.
        beta (float): The best value that the minimizing player can guarantee.
        maximizingPlayer (bool): True if the current move is by the maximizing player.
    Returns:
        float: The evaluated value of the board.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if maximizingPlayer:
        maxEval = MIN
        for move in board.get_legal_moves():
            board.apply_move(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.undo_move()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = MAX
        for move in board.get_legal_moves():
            board.apply_move(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.undo_move()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def evaluate_board(board):
    """
    Evaluates the board state.
    Args:
        board (ChessBoard): The current state of the chess board.
    Returns:
        float: The evaluated score of the board.
    """
    evaluation = 0
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    for piece_type in piece_values:
        evaluation += len(board.board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        evaluation -= len(board.board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return evaluation

def get_best_move(board, depth):
    """
    Determines the best move using the Minimax algorithm.
    Args:
        board (ChessBoard): The current state of the chess board.
        depth (int): The depth to which the algorithm should explore.
    Returns:
        chess.Move: The best move found.
    """
    best_move = None
    maxEval = MIN
    for move in board.get_legal_moves():
        board.apply_move(move)
        moveEval = minimax(board, depth - 1, MIN, MAX, False)
        board.undo_move()
        if moveEval > maxEval:
            maxEval = moveEval
            best_move = move
    return best_move

# This file manages the game state and provides necessary methods for the AI and game modes

import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def reset_board(self):
        """
        Resets the chess board to the initial state.
        """
        self.board.reset()

    def make_move(self, move):
        """
        Makes a move if it is legal.
        Args:
            move (str): The move in UCI format.
        Returns:
            bool: True if the move is legal and made, False otherwise.
        """
        if chess.Move.from_uci(move) in self.board.legal_moves:
            self.board.push(chess.Move.from_uci(move))
            return True
        return False
    
    def get_legal_moves(self):
        """
        Gets all legal moves for the current board state.
        Returns:
            list: List of legal moves.
        """
        return list(self.board.legal_moves)
    
    def is_game_over(self):
        """
        Checks if the game is over.
        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.board.is_game_over()
    
    def get_game_results(self):
        """
        Gets the game results for the end of the game.
        Returns:
            tuple: A tuple containing the scores for white and black players and a message string.
        """
        if self.board.is_checkmate():
            if self.board.turn == chess.WHITE:
                message = "Checkmate! Black wins!"
                return (0, 1, message)
            else:
                message = "Checkmate! White wins!"
                return (1, 0, message)
        elif self.board.is_stalemate():
            message = "Stalemate!"
            return (0.5, 0.5, message)
        elif self.board.is_insufficient_material():
            message = "Draw due to insufficient material!"
            return (0.5, 0.5, message)
        elif self.board.is_seventyfive_moves():
            message = "Draw due to the seventy-five-move rule!"
            return (0.5, 0.5, message)
        elif self.board.is_fivefold_repetition():
            message = "Draw due to fivefold repetition!"
            return (0.5, 0.5, message)
        elif self.board.is_check():
            message = "Check"
            return (0.0, 0.0, message)
        else:
            message = " "
            return (0.0, 0.0, message)
    
    def get_player_move(self):
        """
        Get a move from the player via console input.
        Returns:
            chess.Move: The move inputted by the player.
        """
        move = input("Enter your move in UCI format: ")
        return chess.Move.from_uci(move)
    
    def apply_move(self, move):
        """
        Applies a move to the board.
        Args:
            move (chess.Move): The move to apply.
        """
        self.board.push(move)

    def undo_move(self):
        """
        Undoes the last move made.
        """
        self.board.pop()

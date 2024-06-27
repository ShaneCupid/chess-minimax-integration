# Added the player_vs_ai Method
# To allow a human player to play against an AI using the Minimax algorithm
# The AI moves are determined using the get_ai_move function from ai.py, which uses the Minimax algorithm


import chess
from board import ChessBoard
from chess_gui import ChessGUI
from AI_Player import get_ai_engine
from ai import get_ai_move

class GameModes:
    """
    A class to represent the game modes. This class contains methods to play a game of chess based on the selected game mode.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the GameModes object.

        Parameters:
        None

        Returns:
        None
        """
        self.board = ChessBoard()
        self.gui = ChessGUI(self.board.board)
        self.white_player = None
        self.black_player = None

    def player_vs_ai(self):
        """
        Plays a game of chess where a human plays against an AI.
        
        Parameters:
        None
        
        Returns:
        None
        """
        ai_turn = False  # Set this to True if AI starts first

        while not self.board.is_game_over():
            if ai_turn:
                best_move = get_ai_move(self.board, 3)  # Get the best move using Minimax
                self.board.apply_move(best_move)
            else:
                player_move = self.board.get_player_move()  # Get move from the player
                self.board.apply_move(player_move)

            ai_turn = not ai_turn
            self.gui.update_display()  # Update the GUI after each move

        results = self.board.get_game_results()
        print(results[2])  # Display the result message

    def move_ai(self, ai_name):
        """
        Moves the AI player using the Stockfish engine. Eventually, this will be replaced with the AI model.

        Parameters:
        ai_name (str): The name of the AI engine to use.

        Returns:
        None
        """
        ai_engine = get_ai_engine(ai_name, self.board.board)
        move = ai_engine.select_move()
        if move is not None:
            self.board.board.push(move)
            print(f'AI move: {move}')


    # Updated play_game Method - Includes the logic to determine whether the player is human or AI
    def play_game(self, white_player, black_player):
        """
        Plays a game of chess based on the selected game mode.

        Parameters:
        - white_player (str): The white player type ('human' or 'ai').
        - black_player (str): The black player type ('human' or 'ai').

        Returns:
        None
        """
        self.white_player = white_player
        self.black_player = black_player
        board = self.board.board

        while not board.is_game_over():  # Main game loop
            if board.turn == chess.WHITE:
                if self.white_player == 'human':
                    while not self.gui.move_human():
                        pass
                else:
                    self.move_ai(self.white_player)
            else:
                if self.black_player == 'human':
                    while not self.gui.move_human():
                        pass
                else:
                    self.move_ai(self.black_player)

            self.gui.update_display()

        white_player_score, black_player_score, message = self.board.get_game_results()
        print(message)
        print(white_player_score, black_player_score)
        self.gui.status_message = message
        self.gui.update_display()
        self.restart_game()

    def restart_game(self):
        """
        Restarts the game.

        Parameters:
        None

        Returns:
        None
        """
        self.board.reset_board()
        self.gui.board = self.board.board
        self.gui.status_message = ""
        self.gui.selected_piece = None
        self.gui.selected_pos = None
        self.gui.possible_moves = []
        self.play_game(self.white_player, self.black_player)

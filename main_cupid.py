from game_modes import GameModes
from chess_gui import game_start_menu

def main():
    """
    The main function that runs the game.
    """
    (white_player, black_player) = game_start_menu()  # Displays a player select menu and gets user input    
    GameModes().play_game(white_player, black_player)

if __name__ == "__main__":
    main()

import sys
from tic_tac_toe import play_tic_tac_toe, reset_game
from guess_number import play_Number_Guessing_Game
from word_scramble import play_word_scumble

# Menu options
menu_options = ["Quiz Game", "Hangman", "Tic-Tac-Toe", "Number Guessing Game", "Word Scramble", "Exit"]
global current_game
current_game = None


def display_welcome_message():
    print("-" * 50)
    print("Welcome to the Arcade!".center(50))
    print("-" * 50)


# Function to display menu options
def display_menu():
    print("Mini-games:")
    for i in range(len(menu_options)):
        print(f"{i + 1}) {menu_options[i]}")


# Function to select operation based on user input
def game_selection(op):
    match op:
        case "1" | "quizgame":
            pass
        case "2" | "hangman":
            pass
        case "3" | "tictactoe":
            global current_game
            current_game = "3"
            reset_game()
            return play_tic_tac_toe()
        case "4" | "numberguessinggame":
            current_game = "4"
            return play_Number_Guessing_Game()
        case "5" | "wordscramble":
            current_game = "5"
            return play_word_scumble()
        case "6" | "exit":
            print("Exiting the game. Goodbye!")
            sys.exit()
        case _:
            print("Invalid option. Please select a valid game.")
            return False
    return False


ret = False
while True:
    if not ret or current_game is None:
        display_welcome_message()
        display_menu()
        operation = input("Select a game from (1-5) or (6) for exit: ")
        user_input = operation.replace(" ", "").lower()
        ret = game_selection(user_input)
    else:
        ret = game_selection(current_game)

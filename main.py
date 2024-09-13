import sys

# Menu options
menu_options = ["Quiz Game", "Hangman", "Tic-Tac-Toe", "Number Guessing Game", "Word Scramble", "Exit"]


def display_welcome_message():
    print("-" * 50)  # Line of 50 dashes
    print("Welcome to the Arcade!".center(50))  # Center the message within 50 characters
    print("-" * 50)  # Another line of 50 dashes


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
            pass
        case "4" | "numberguessinggame":
            pass
        case "5" | "wordscramble":
            pass
        case "6" | "exit":
            print("Exiting the game. Goodbye!")
            sys.exit()
        case _:
            print("Invalid option. Please select a valid game.")
            return False
    return True


while True:
    display_welcome_message()
    display_menu()
    operation = input("Select a game from (1-5) or (6) for exit: ")
    user_input = operation.replace(" ", "").lower()

    if game_selection(user_input):
        break

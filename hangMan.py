import random
import os

# Function to choose a random word from a list
def choose_randomWord(word_list):
    random_word = random.choice(word_list).strip().lower()
    return random_word

# Function to draw the hangman based on the number of incorrect guesses
def draw(step):
    if step == 1:
        print("     -----")
    elif step == 2:
        print("-------")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
        print("     -----")
    elif step == 3:
        print("-------")
        print("|      |")
        print("       |")
        print("       |")
        print("       |")
    elif step == 4:
        print("-------")
        print("|      |")
        print("0      |")
        print("       |")
        print("     -----")

# Function to play the game
def play(words_list):
    steps = 0
    random_word = list(choose_randomWord(words_list))
    hidden_word = ['*' for _ in range(len(random_word))]

    while hidden_word != random_word and steps < 4:
        word = ''.join(hidden_word)
        print(word)
        input_char = input("Choose a letter: ").lower()

        if input_char in random_word:
            for ind, char in enumerate(random_word):
                if char == input_char:
                    hidden_word[ind] = input_char
        else:
            steps += 1
            draw(steps)
            if steps == 4:
                print("You lost! The word was:", ''.join(random_word))
                break

    if steps != 4:
        print("You won the game!")
    
    return game_end_options()

# Function to ask the player if they want to replay or return to the menu
def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True  # Play again
            elif option == 2:
                return False  # Go back to the menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

# Main game function with difficulty selection
def hangMan_game():
    base_dir = os.path.dirname(__file__)  # Get the current file's directory
    while True:
        print("(1) Easy")
        print("(2) Medium")
        print("(3) Hard")
        try:
            n = int(input("Choose difficulty (1, 2, 3): "))
            if n == 1:
                file_path = os.path.join(base_dir, 'EasyWords.txt')
            elif n == 2:
                file_path = os.path.join(base_dir, 'MediumWords.txt')
            elif n == 3:
                file_path = os.path.join(base_dir, 'HardWords.txt')
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            # Read words from the selected file
            with open(file_path, 'r') as file:
                words_list = [line.strip() for line in file]
            
            play_again = play(words_list)  # Get the result of the game (True/False)
            
            if not play_again:  # If the player chooses to go back to the menu
                return False  # Break out and return to the main menu

        except ValueError:
            print("That's not a valid number. Please try again.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

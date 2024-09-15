import numpy as np
import random
import os

# Leaderboard
LEADERBOARD_FILE = "tic_tac_toe_leaderboard.txt"

def load_leaderboard():
    leaderboard = {}
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    return leaderboard

def save_leaderboard(leaderboard):
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in sorted_leaderboard.items():
            file.write(f"{name}:{score}\n")


def update_leaderboard(player_name, score, leaderboard):
    if player_name in leaderboard:
        leaderboard[player_name] += score
    else:
        leaderboard[player_name] = score
    save_leaderboard(leaderboard)


# Function to reset the game state
def reset_game():
    print("----------------------------------------------------")
    xo = np.array([str(i) for i in range(1, 10)])  # Reset the board
    my_turn = random.choice([True, False])  # Randomize the first turn

    if my_turn:
        my_symbol = "X"
        pc_symbol = "O"
    else:
        my_symbol = "O"
        pc_symbol = "X"

    return xo, my_symbol, pc_symbol, my_turn


# Function to update the board
def update_board(xo, position, symbol):
    index = position - 1
    xo[index] = symbol


# Function to get the PC move
def get_pc_move(xo):
    available_positions = [i for i in range(1, 10) if xo[i - 1] not in ["X", "O"]]
    return random.choice(available_positions)


# Print the Tic-Tac-Toe board
def print_tic_tac_toe_board(array):
    print(f" {array[0]} | {array[1]} | {array[2]} ")
    print("---|---|---")
    print(f" {array[3]} | {array[4]} | {array[5]} ")
    print("---|---|---")
    print(f" {array[6]} | {array[7]} | {array[8]} ")


# Function to get valid position from the player
def get_valid_position(xo):
    while True:
        try:
            position = int(input("Enter a position between 1 and 9: "))
            if 1 <= position <= 9:
                if xo[position - 1] in [str(i) for i in range(1, 10)]:
                    return position
                else:
                    print("Position already taken. Please select another position.")
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to check the game status (win or draw)
def check_game_status(xo, my_symbol):
    # Diagonal check
    if (xo[0] == xo[4] == xo[8] and xo[0] in ["X", "O"]) or (xo[2] == xo[4] == xo[6] and xo[2] in ["X", "O"]):
        winner = xo[0] if xo[0] in ["X", "O"] else xo[2]
        print("You Won") if winner == my_symbol else print("PC Won")
        return True


    # Horizontal check
    for i in range(0, 9, 3):
        if xo[i] == xo[i+1] == xo[i+2] and xo[i] in ["X", "O"]:
            winner = xo[i]
            print("You Won") if winner == my_symbol else print("PC Won")
            return True

    # Vertical check
    for i in range(3):
        if xo[i] == xo[i + 3] == xo[i + 6] and xo[i] in ["X", "O"]:
            winner = xo[i]
            print("You Won") if winner == my_symbol else print("PC Won")
            return True

    # Check for draw
    if all(pos in ["X", "O"] for pos in xo):
        print("It's a draw!")
        return True

    return False


# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    xo, my_symbol, pc_symbol, my_turn = reset_game()  # Initialize/reset the game
    game_end = False

    while True:
        print_tic_tac_toe_board(xo)

        if my_turn:
            print(f"Enter number to place {my_symbol}")
            player_tile_position = get_valid_position(xo)
            update_board(xo, player_tile_position, my_symbol)
            if check_game_status(xo, my_symbol):
                break
        else:
            print("PC is making a move...")
            pc_tile_position = get_pc_move(xo)
            update_board(xo, pc_tile_position, pc_symbol)
            if check_game_status(xo, my_symbol):
                break

        # Toggle turn after one move
        my_turn = not my_turn

    return game_end_options()


# Function to display game end options with input validation
def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True  # Play again
            elif option == 2:
                return False  # Go back to menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


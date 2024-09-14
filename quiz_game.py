import os

LEADERBOARD_FILE = "leaderboard.txt"

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

questions = [
    ("What is the capital of France? ", "Paris"),
    ("What is the largest planet in the solar system? ", "Jupiter"),
    ("What is the square root of 64? ", "8"),
    ("Who wrote 'Hamlet'? ", "Shakespeare"),
    ("What is the chemical symbol for water? ", "H2O")
]

def run_quiz_game(input_fn):
    leaderboard = load_leaderboard()
    player_name = input_fn("Enter your name: ")

    score = 0
    for question, answer in questions:
        response = input_fn(question)
        if response.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}")

    print(f"{player_name}, you scored {score} out of {len(questions)}")
    update_leaderboard(player_name, score, leaderboard)

    print("Leaderboard:")
    for name, total_score in leaderboard.items():
        print(f"{name}: {total_score}")

    return game_end_options()

def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True
            elif option == 2:
                return False  # Go back to menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

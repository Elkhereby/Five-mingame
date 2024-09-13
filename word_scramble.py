import random
import os


LEADERBOARD_FILE = "word_scrumble_leaderboard.txt"

def load_leaderboard():
    leaderboard = {}
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    return leaderboard

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in leaderboard.items():
            file.write(f"{name}:{score}\n")

def update_leaderboard(player_name, score, leaderboard):
    if player_name in leaderboard:
        leaderboard[player_name] += score
    else:
        leaderboard[player_name] = score
    save_leaderboard(leaderboard)

word_list = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return "".join(word)

def play_word_scumble():
  
    print("Welcome to the Word Scramble Game!")
    print("How to play:")
    print("You have 3 guesses only.")
    print("If you guess correctly on the first try, you get 3 points.")
    print("On the second try, you get 2 points.")
    print("On the third try, you get 1 point.")
    
    player_name = input("Enter your name: ")

    leaderboard = load_leaderboard()

    if player_name in leaderboard:
        print(f"Welcome back, {player_name}! Your current score is {leaderboard[player_name]}.")
    else:
        print(f"Hello, {player_name}! This is your first time playing.")

    score = 0
    attempts = 3
        
    original_word = random.choice(word_list)
    scrambled_word = scramble_word(original_word)
        
    print(f"Unscramble the word: {scrambled_word}")
    
    while attempts > 0:
        guessed_word = input(f"Guess the word (You have {attempts} guesses left): ")
        if guessed_word.lower() == original_word:
            print("Correct! You guessed the word!")
            score = attempts
            break
        else:
            print("Wrong Word!!")
            
        attempts -= 1
        
    if score > 0:
        print(f"Your score = {score}")
    else:
        print(f"Sorry, you lost! The correct number was {original_word}.")
        print("Your score = 0")
        
    update_leaderboard(player_name, score, leaderboard)

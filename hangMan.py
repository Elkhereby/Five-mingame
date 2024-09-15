import random
def choose_randomWord(list):
    random_word = str(random.choice(list))
    random_word=random_word.lower()
    return random_word
    
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
        
def play(words_list):
    steps = 0
    random_word = list(choose_randomWord(words_list))
    print(''.join(random_word))
    hidden_word = ['*' for i in range(len(random_word))]
                
    while hidden_word != random_word and steps < 4:
        word = ''.join(hidden_word)
        print(word)
        input_char = input("choose a letter: ")
        if input_char in random_word:
            for ind,char in enumerate(random_word):
                if char == input_char:                            
                    hidden_word[ind] = input_char
                            
        else:
            steps += 1  
            draw(steps)
            if steps == 4:
                print("You lost! The word was:", ''.join(random_word))
                break
    if steps != 4:
        print("You won the game")  
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
                                  
def hangMan_game():
    while True:
        print("(1)- Easy")
        print("(2)- Medium")
        print("(3)- Hard")
        try:
            n = int(input("Choose difficulty (1, 2, 3): "))
            if n == 1:
                with open(r"C:\Users\ahmed emad\Desktop\python\project_1\Five-mingame\EasyWords.txt", 'r') as file:  # Use raw string for Windows paths
                    lines = file.readlines()
                
                words_list = [line.strip() for line in lines]
                play(words_list)         
                                
            elif n == 2:
                with open(r"C:\Users\ahmed emad\Desktop\python\project_1\Five-mingame\MediumWords.txt", 'r') as file:
                    lines = file.readlines()
                word_lists = [line.strip() for line in lines]
                play(word_lists)
                break

            elif n == 3:
                with open(r"C:\Users\ahmed emad\Desktop\python\project_1\Five-mingame\HardWords.txt", 'r') as file:
                    lines = file.readlines()
                word_lists = [line.strip() for line in lines]
                play(word_lists)
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            print("That's not a valid number. Please try again.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
    

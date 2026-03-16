import random

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    words = [
        "python", "algorithm", "computer", "science",
        "keyboard", "programming", "developer",
        "function", "variable", "internet"
    ]
    
    score = 0
    attempts_allowed = 3
    play_again = "yes"
    
    while play_again.lower() == "yes":
        original_word = random.choice(words)
        scrambled = scramble_word(original_word)
        
        print("\nScrambled word:", scrambled)
        attempts = attempts_allowed
        
        while attempts > 0:
            guess = input("Your guess: ").lower()
            
            if guess == original_word:
                print("Correct! You win this round.")
                score += 10
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Wrong guess. Attempts left:", attempts)
                else:
                    print("No attempts left.")
                    print("The correct word was:", original_word)
        
        print("Current Score:", score)
        play_again = input("Do you want to play again? (yes/no): ")
    
    print("Final Score:", score)
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
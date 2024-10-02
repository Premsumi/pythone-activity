import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range
    lower_bound = 1
    upper_bound = 100
    
    # Randomly choose a number within the range
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    # Give the player 5 attempts to guess the number
    attempts = 5
    
    while attempts > 0:
        try:
            # Ask the player for a guess
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            
            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number correctly. It was {number_to_guess}.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            
            attempts -= 1
            print(f"You have {attempts} attempts left.\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()


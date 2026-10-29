"""A basic command-line version of the Guess the Number game."""

import random


def play_game():
    """Play one game in the terminal."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 100.")

    while True:
        # input() always gives us text, so int() changes it into a number.
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number, such as 42.")
            continue

        # Check that the player uses a number in the game's range.
        if guess < 1 or guess > 100:
            print("Please choose a number from 1 to 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"You got it in {attempts} attempts! 🎉")
            break


def main():
    """Let the player choose whether to play another game."""
    while True:
        play_game()
        play_again = input("Would you like to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()

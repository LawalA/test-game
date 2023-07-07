import random

def play_game():
    number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Bravo! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing the guessing game!")

play_game()


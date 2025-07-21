import random

# Generate a random number between 1 and 10
"""secret_number = random.randint(1, 10)

# Welcome message
print("Welcome to the Number Guessing Game! You get 1 guess.")

# Guessing loop
while True:
    # Get user guess
    guess = int(input("Guess a number between 1 and 10: "))

    # Check guess and range
    if 1 <= guess <= 10:
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break  # Exit loop on correct guess
        else:
            print("Your guess is wrong. Try again.")
    else:
        print("Your guess is out of range. Please enter a number between 1 and 10.")

# Game over message (if loop exits)
print(f"The number was {secret_number}.")"""


max_value = int(input("give a large number:"))
def generate_random_number(max_value): print(random.randint(1, max_value))
generate_random_number(max_value)
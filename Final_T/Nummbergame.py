import random

# Computer picks a random number
secret_number = random.randint(1, 50)

# Intro
print("I'm thinking of a number between 1 and 50.")
print("Guess it!")

attempts = 0

while True:
    # Get user input
    guess_str = input("Your guess: ").strip()
    
    # Check input
    if not guess_str.isdigit():
        print("Enter a number.")
        continue
    
    guess = int(guess_str)
    if guess < 1 or guess > 50:
        print("Number must be between 1 and 50.")
        continue

    attempts += 1

    # Check guess
    if guess == secret_number:
        # Correct guess
        print("\nCorrect!")
        print("Attempts:", attempts)
        # Thumbs up prize
        print("  __   ")
        print(" (  )  ")
        print("  ||   ")
        print("  ||   ")
        print("  ||__ ")
        print("  |___)")
        break
    elif guess < secret_number:
        # Too low
        print("Too low!")
        diff = secret_number - guess
        if diff > 10:
            diff = 10
        # Show upward arrow
        for i in range(diff, 0, -1):
            print(" " * 10 + "|")
        print(" " * 10 + "^")
    else:
        # Too high
        print("Too high!")
        diff = guess - secret_number
        if diff > 10:
            diff = 10
        # Show downward arrow
        for i in range(diff):
            print(" " * 10 + "|")
        print(" " * 10 + "v")

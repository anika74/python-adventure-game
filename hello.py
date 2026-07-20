import random

# 1. Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

print("I have thought of a number between 1 and 100.")
print("You have 3 chances to guess it!")

# 2. Loop for 3 chances
for i in range(1, 6):
    guess = int(input("What is your guess? "))
    
    if guess == secret_number:
        print("Awesome! You guessed the correct number!")
        break  # Stop the loop if the guess is correct
    
    # If the secret number is larger than the guess
    elif secret_number > guess:
        print("Think of a bigger number.")
        
    # If the secret number is smaller than the guess
    elif secret_number < guess:
        print("Think of a smaller number.")
        
else:
    # This block runs only if the loop finishes 3 times without breaking (i.e., user lost)
    print(f"\nGame Over! The correct number was {secret_number}.")
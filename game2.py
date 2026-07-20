import random
secret_number = random.randint(1, 100)
print("guess a number between 1 and 100")
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("enter guess:"))
    attempts = attempts + 1
    if guess == secret_number:
        print("you won!")
    elif guess < secret_number:
        print("too low!")
    else:
        print("too high")
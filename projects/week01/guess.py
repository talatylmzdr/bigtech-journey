import random

def play():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Guessing Game!")
    
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")  
            
if __name__ == "__main__":
    play()
    
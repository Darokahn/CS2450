import random

print("Hello! I am going to guess your age. I'm warning you, I'm pretty good...")

result = None

name = input("first, your name: ")
guessCount = 0
while (result != 'y' and guessCount < 5):
    guess = random.randint(0, 99)
    result = input(f"is {guess} your age? ")
    if (result != 'y'):
        print("Rats.")
        guessCount += 1
if guessCount == 5:
    print("shoot. I ran out of guesses.")
else:
    print(f"{name} is {guess} years old.")

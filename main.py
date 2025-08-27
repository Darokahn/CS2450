import random

print("Hello! I am going to guess your age. Okay?")

result = None

name = input("first, your name: ")
while (result != 'y'):
    guess = random.randint(15, 30)
    result = input(f"is {guess} your age? ")
    if (result != 'y'):
        print("Rats.")
print(f"{name} is {guess} years old.")

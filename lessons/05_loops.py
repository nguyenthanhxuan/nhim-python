# Lesson 5: Loops - Repeating Actions 🔄

# Sometimes we want to repeat the same action many times
# Instead of writing the same code over and over, we use loops!

# FOR LOOPS - when we know how many times to repeat
print("=== Counting with a for loop ===")
for number in range(1, 6):  # Count from 1 to 5
    print(f"Count: {number}")

print("\n=== Saying hello 3 times ===")
for i in range(3):
    print("Hello there!")

# Let's make a multiplication table!
print("\n=== Multiplication Table for 5 ===")
for i in range(1, 11):  # 1 to 10
    result = 5 * i
    print(f"5 x {i} = {result}")

# WHILE LOOPS - repeat while a condition is true
print("\n=== Countdown with while loop ===")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown = countdown - 1  # This is the same as: countdown -= 1
print("Blast off! 🚀")

# Let's make a guessing game!
print("\n=== Number Guessing Game ===")
import random

secret_number = random.randint(1, 10)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 10!")

while guess != secret_number:
    guess = int(input("What's your guess? "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")

# Fun with patterns!
print("\n=== Making patterns ===")
for i in range(1, 6):
    stars = "*" * i  # This repeats the star i times
    print(stars)

print()
for i in range(5, 0, -1):  # Count backwards from 5 to 1
    stars = "*" * i
    print(stars)

# 🎯 Your turn!
# 1. Create a loop that prints your name 10 times
# 2. Make a program that asks for a number and prints all numbers from 1 to that number
# 3. Create a simple menu that keeps asking what the user wants to do until they choose "quit"
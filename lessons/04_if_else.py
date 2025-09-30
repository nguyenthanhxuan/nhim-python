# Lesson 4: Making Decisions with If/Else 🤔

# Sometimes we want our program to make decisions
# We use "if" statements to do this!

# Let's start with a simple example
age = 12

if age >= 13:
    print("You are a teenager!")
else:
    print("You are not a teenager yet.")

# We can also check multiple conditions
weather = "sunny"

if weather == "sunny":
    print("Let's go to the park!")
elif weather == "rainy":
    print("Let's stay inside and read.")
else:
    print("Let's see what the weather is like.")

# Let's make an interactive program!
print("\n=== Magic 8-Ball ===")
question = input("Ask me a yes or no question: ")

import random
answers = [
    "Yes, definitely!",
    "No way!",
    "Maybe...",
    "Ask again later",
    "I think so!",
    "Probably not",
    "Absolutely!"
]

magic_answer = random.choice(answers)
print("🎱 Magic 8-Ball says:", magic_answer)

# Age checker program
print("\n=== Age Checker ===")
user_age = int(input("How old are you? "))

if user_age < 5:
    print("You're just a little kid!")
elif user_age < 13:
    print("You're a kid!")
elif user_age < 20:
    print("You're a teenager!")
else:
    print("You're a grown-up!")

# Password checker
secret_password = "python123"
entered_password = input("\nEnter the secret password: ")

if entered_password == secret_password:
    print("🎉 Access granted! Welcome to the secret club!")
else:
    print("❌ Wrong password! Try again later.")

# 🎯 Your turn!
# 1. Create a program that checks if a number is positive, negative, or zero
# 2. Make a simple quiz with one question and check if the answer is correct
# 3. Create a program that suggests activities based on the time of day
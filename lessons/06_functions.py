# Lesson 6: Functions - Organizing Your Code 🔧

# Functions are like mini-programs inside your program!
# They help us organize code and avoid repeating ourselves

# Let's start with a simple function
def say_hello():
    print("Hello there!")
    print("Welcome to functions!")

# To use (call) a function, we write its name with parentheses
print("=== Calling our first function ===")
say_hello()

# Functions can take inputs (called parameters)
def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")

print("\n=== Functions with parameters ===")
greet_person("Alice")
greet_person("Bob")

# Functions can return values (give us something back)
def add_numbers(a, b):
    result = a + b
    return result

print("\n=== Functions that return values ===")
answer = add_numbers(5, 3)
print(f"5 + 3 = {answer}")

# Let's make a function that calculates area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area

print("\n=== Rectangle Area Calculator ===")
my_area = rectangle_area(10, 5)
print(f"A rectangle that is 10 by 5 has an area of {my_area}")

# Functions can have multiple parameters and do complex things
def create_password(name, birth_year, favorite_number):
    password = name.lower() + str(birth_year) + "!" + str(favorite_number)
    return password

print("\n=== Password Generator ===")
user_name = input("Enter your name: ")
user_year = int(input("Enter your birth year: "))
user_number = int(input("Enter your favorite number: "))

new_password = create_password(user_name, user_year, user_number)
print(f"Your generated password is: {new_password}")

# Let's make a fun math quiz function
def math_quiz():
    import random
    
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    
    print(f"\n🧮 Quick Math Quiz!")
    user_answer = int(input(f"What is {num1} + {num2}? "))
    
    if user_answer == correct_answer:
        print("🎉 Correct! Great job!")
        return True
    else:
        print(f"❌ Not quite. The answer is {correct_answer}")
        return False

# Let's play the quiz multiple times
print("\n=== Math Quiz Game ===")
score = 0
for i in range(3):
    print(f"\nQuestion {i + 1}:")
    if math_quiz():
        score += 1

print(f"\n🏆 Final Score: {score}/3")

# Function to draw ASCII art
def draw_box(width, height, character="*"):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(character * width)  # Top and bottom borders
        else:
            print(character + " " * (width - 2) + character)  # Sides

print("\n=== ASCII Art Box ===")
draw_box(10, 5)
print()
draw_box(8, 4, "#")

# 🎯 Your turn!
# 1. Create a function called 'double_number' that takes a number and returns it doubled
# 2. Make a function called 'is_even' that checks if a number is even (returns True/False)
# 3. Create a function that takes someone's age and tells them what grade they're probably in

print("\n🎯 Practice Time!")
print("Try creating your own functions above this line!")

# Bonus: Function to convert temperature
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("\n🌡️ Temperature Converter:")
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")
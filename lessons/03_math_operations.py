# Lesson 3: Math Operations - Python Calculator! 🧮

# Python can do math just like a calculator!
# Let's learn the basic math operations

# Addition (+)
result = 5 + 3
print("5 + 3 =", result)

# Subtraction (-)
result = 10 - 4
print("10 - 4 =", result)

# Multiplication (*)
result = 6 * 7
print("6 * 7 =", result)

# Division (/)
result = 15 / 3
print("15 / 3 =", result)

# Let's make a simple calculator!
print("\n=== Python Calculator ===")

# Get two numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Do all the math operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

# Show the results
print(f"\n{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")

# Fun with variables and math!
my_allowance = 10
candy_cost = 2
candies_i_can_buy = my_allowance / candy_cost
money_left = my_allowance % candy_cost  # % gives us the remainder

print(f"\nIf candy costs ${candy_cost} each:")
print(f"I can buy {int(candies_i_can_buy)} candies")
print(f"I'll have ${money_left} left over")

# 🎯 Your turn!
# 1. Calculate how many minutes are in a day (24 hours * 60 minutes)
# 2. Ask the user for their birth year and calculate their age
# 3. Create a tip calculator that calculates 15% tip on a meal
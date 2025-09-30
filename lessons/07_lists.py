# Lesson 7: Lists - Storing Multiple Things 📝

# Lists are like containers that can hold multiple items
# Think of them as a shopping list or a list of your friends!

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, True, 3.14]

print("=== Our first lists ===")
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed list:", mixed_list)

# Getting items from a list (indexing)
# Lists start counting from 0!
print("\n=== Getting items from lists ===")
print("First fruit:", fruits[0])  # apple
print("Second fruit:", fruits[1])  # banana
print("Last fruit:", fruits[-1])  # grape (negative index counts from end)

# Adding items to a list
print("\n=== Adding items ===")
fruits.append("strawberry")  # Add to the end
print("After adding strawberry:", fruits)

fruits.insert(1, "kiwi")  # Insert at position 1
print("After inserting kiwi:", fruits)

# Removing items from a list
print("\n=== Removing items ===")
fruits.remove("banana")  # Remove by value
print("After removing banana:", fruits)

removed_fruit = fruits.pop()  # Remove and return the last item
print(f"Removed {removed_fruit}, list now:", fruits)

# List operations
print("\n=== List operations ===")
print("Number of fruits:", len(fruits))
print("Is 'apple' in the list?", "apple" in fruits)
print("Is 'pizza' in the list?", "pizza" in fruits)

# Looping through lists
print("\n=== Looping through lists ===")
print("All fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Looping with index numbers
print("\nFruits with numbers:")
for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")

# List of favorite things
print("\n=== Personal Lists ===")
favorite_colors = []  # Start with empty list

print("Let's build your favorite colors list!")
for i in range(3):
    color = input(f"Enter favorite color #{i + 1}: ")
    favorite_colors.append(color)

print("Your favorite colors are:", favorite_colors)

# Sorting lists
numbers = [5, 2, 8, 1, 9, 3]
print(f"\nOriginal numbers: {numbers}")

numbers.sort()  # Sort in place
print(f"Sorted numbers: {numbers}")

fruits_copy = fruits.copy()  # Make a copy
fruits_copy.sort()
print(f"Original fruits: {fruits}")
print(f"Sorted fruits: {fruits_copy}")

# List slicing (getting parts of a list)
print("\n=== List slicing ===")
alphabet = ["a", "b", "c", "d", "e", "f", "g"]
print("Full alphabet:", alphabet)
print("First 3 letters:", alphabet[0:3])  # or alphabet[:3]
print("Last 3 letters:", alphabet[-3:])
print("Every other letter:", alphabet[::2])

# Fun with lists: Creating a simple inventory
print("\n=== Backpack Inventory Game ===")
backpack = ["water bottle", "snacks", "notebook"]

print("You start with these items in your backpack:")
for i, item in enumerate(backpack, 1):
    print(f"{i}. {item}")

while True:
    action = input("\nWhat do you want to do? (add/remove/view/quit): ").lower()
    
    if action == "add":
        new_item = input("What item do you want to add? ")
        backpack.append(new_item)
        print(f"Added {new_item} to your backpack!")
        
    elif action == "remove":
        if len(backpack) == 0:
            print("Your backpack is empty!")
        else:
            print("Current items:")
            for i, item in enumerate(backpack, 1):
                print(f"{i}. {item}")
            try:
                choice = int(input("Which item number to remove? ")) - 1
                removed = backpack.pop(choice)
                print(f"Removed {removed} from your backpack!")
            except:
                print("Invalid choice!")
                
    elif action == "view":
        if len(backpack) == 0:
            print("Your backpack is empty!")
        else:
            print("Current backpack contents:")
            for i, item in enumerate(backpack, 1):
                print(f"{i}. {item}")
                
    elif action == "quit":
        print("Thanks for playing!")
        break
    else:
        print("I don't understand that command.")

# 🎯 Your turn!
print("\n🎯 Practice Time!")
# 1. Create a list of your 5 favorite movies
# 2. Add a new movie to the list
# 3. Print each movie with its position number
# 4. Remove your least favorite movie from the list

# Bonus: List comprehensions (advanced!)
print("\n🌟 Bonus: List Comprehensions")
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]  # Create new list with each number doubled
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]  # Even numbers from 1-10
print(f"Even numbers 1-10: {even_numbers}")
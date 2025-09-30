# Fun Example: Name Art Generator 🎨
# This program creates cool ASCII art with your name!

name = input("What's your name? ").upper()

print("\n" + "="*50)
print("✨ WELCOME TO THE NAME ART GENERATOR! ✨")
print("="*50)

# Create a banner with the name
print("\n" + "*" * (len(name) + 4))
print("* " + name + " *")
print("*" * (len(name) + 4))

# Create a pyramid with the first letter
first_letter = name[0]
print(f"\n🎯 Pyramid for '{first_letter}':")
for i in range(1, 6):
    spaces = " " * (5 - i)
    letters = first_letter * (2 * i - 1)
    print(spaces + letters)

# Count the letters in the name
print(f"\n📊 Your name '{name}' has {len(name)} letters!")

# Show each letter with a number
print("\n🔤 Letter breakdown:")
for i, letter in enumerate(name, 1):
    print(f"Letter {i}: {letter}")

# Create a fun pattern
print(f"\n🌟 Fun pattern with your name:")
for i in range(1, 4):
    pattern = (name + " ") * i
    print(pattern)

print("\nThanks for using the Name Art Generator! 🎉")
# Project 1: Personal Information Card Generator 🆔

print("🎨 Personal Information Card Generator")
print("="*50)
print("Let's create a cool personal info card!")
print()

# Collect information from the user
name = input("What's your name? ")
age = int(input("How old are you? "))
favorite_color = input("What's your favorite color? ")
favorite_animal = input("What's your favorite animal? ")
favorite_food = input("What's your favorite food? ")
hobby = input("What's your favorite hobby? ")

# Calculate some fun facts
current_year = 2024
birth_year = current_year - age
next_birthday_age = age + 1

# Create the information card
print("\n" + "="*60)
print("🌟" + " PERSONAL INFORMATION CARD ".center(56) + "🌟")
print("="*60)
print(f"📛 Name: {name}")
print(f"🎂 Age: {age} years old")
print(f"📅 Born in: {birth_year}")
print(f"🎈 Next birthday age: {next_birthday_age}")
print(f"🎨 Favorite Color: {favorite_color}")
print(f"🐾 Favorite Animal: {favorite_animal}")
print(f"🍕 Favorite Food: {favorite_food}")
print(f"🎮 Favorite Hobby: {hobby}")
print("="*60)

# Add some fun predictions
print("\n🔮 Fun Predictions:")

if age < 10:
    print("• You're still a little kid with lots of growing to do!")
elif age < 13:
    print("• You're a kid who's getting ready to be a teenager!")
elif age < 18:
    print("• You're a teenager with exciting years ahead!")
else:
    print("• You're growing up fast!")

# Create a fun username suggestion
username_suggestion = (name.lower().replace(" ", "") + 
                      str(birth_year) + 
                      favorite_animal.lower()[:3])
print(f"• Suggested username: {username_suggestion}")

# Create a personalized message
print(f"\n💌 Personal Message:")
print(f"Hi {name}! It's amazing that you're {age} years old and love {favorite_color}!")
print(f"I bet you'd look great in {favorite_color} while doing {hobby}!")
print(f"Maybe you can share some {favorite_food} with a {favorite_animal} someday! 🤗")

# Add some ASCII art with their initial
initial = name[0].upper()
print(f"\n🎨 Your Initial Art:")
print("  ***  ")
print(f" * {initial} * ")
print("  ***  ")

print(f"\n🎉 Thanks for creating your personal card, {name}!")
print("Save this program and run it again anytime to make a new card!")

# Optional: Ask if they want to see their info in different formats
show_more = input("\nWould you like to see your info in a different format? (yes/no): ").lower()

if show_more == "yes":
    print(f"\n📋 List Format:")
    info_list = [name, age, favorite_color, favorite_animal, favorite_food, hobby]
    for i, info in enumerate(info_list, 1):
        print(f"{i}. {info}")
    
    print(f"\n📊 Quick Stats:")
    print(f"• Name length: {len(name)} characters")
    print(f"• Years until 18: {max(0, 18 - age)}")
    print(f"• Born in the {'2010s' if birth_year >= 2010 else '2000s'}")

print("\n✨ Come back anytime to make another card! ✨")
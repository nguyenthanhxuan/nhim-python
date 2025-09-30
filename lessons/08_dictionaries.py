# Lesson 8: Dictionaries - Storing Key-Value Pairs 🔑

# Dictionaries store information in key-value pairs
# Think of them like a real dictionary: word -> definition
# Or like a phone book: name -> phone number

# Creating dictionaries
person = {
    "name": "Alex",
    "age": 12,
    "favorite_color": "blue",
    "pets": ["dog", "cat"]
}

print("=== Our first dictionary ===")
print("Person info:", person)

# Getting values from a dictionary
print("\n=== Getting values ===")
print("Name:", person["name"])
print("Age:", person["age"])
print("Favorite color:", person["favorite_color"])

# Adding new key-value pairs
print("\n=== Adding new information ===")
person["hobby"] = "reading"
person["grade"] = 7
print("Updated person:", person)

# Changing existing values
print("\n=== Updating information ===")
person["age"] = 13  # Happy birthday!
print("After birthday:", person)

# Checking if a key exists
print("\n=== Checking for keys ===")
if "name" in person:
    print(f"We know this person's name: {person['name']}")

if "height" in person:
    print(f"Height: {person['height']}")
else:
    print("We don't know their height yet")

# Getting all keys and values
print("\n=== All keys and values ===")
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Looping through dictionaries
print("\n=== Looping through dictionary ===")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary of student grades
print("\n=== Student Grade Book ===")
grades = {
    "math": 95,
    "science": 87,
    "english": 92,
    "history": 88
}

print("Current grades:")
for subject, grade in grades.items():
    print(f"{subject.title()}: {grade}")

# Calculate average
total = sum(grades.values())
average = total / len(grades)
print(f"\nAverage grade: {average:.1f}")

# Interactive dictionary: Personal profile builder
print("\n=== Personal Profile Builder ===")
profile = {}

profile["name"] = input("What's your name? ")
profile["age"] = int(input("How old are you? "))
profile["city"] = input("What city do you live in? ")
profile["favorite_food"] = input("What's your favorite food? ")

# Build hobbies list
hobbies = []
print("\nLet's add some hobbies (press enter with empty input to stop):")
while True:
    hobby = input("Enter a hobby: ")
    if hobby == "":
        break
    hobbies.append(hobby)

profile["hobbies"] = hobbies

print("\n🎉 Your Profile:")
print("=" * 30)
for key, value in profile.items():
    if key == "hobbies":
        print(f"{key.title()}: {', '.join(value)}")
    else:
        print(f"{key.title()}: {value}")

# Nested dictionaries (dictionaries inside dictionaries!)
print("\n=== Nested Dictionaries: Class Roster ===")
classroom = {
    "student1": {
        "name": "Emma",
        "age": 12,
        "grades": {"math": 90, "science": 95}
    },
    "student2": {
        "name": "Liam",
        "age": 13,
        "grades": {"math": 85, "science": 88}
    }
}

print("Class roster:")
for student_id, student_info in classroom.items():
    print(f"\n{student_id.title()}:")
    print(f"  Name: {student_info['name']}")
    print(f"  Age: {student_info['age']}")
    print("  Grades:")
    for subject, grade in student_info['grades'].items():
        print(f"    {subject}: {grade}")

# Dictionary methods
print("\n=== Useful Dictionary Methods ===")
sample_dict = {"a": 1, "b": 2, "c": 3}

# Get with default value
print("Value for 'd':", sample_dict.get("d", "Not found"))

# Remove items
removed_value = sample_dict.pop("b", "Not found")
print(f"Removed 'b': {removed_value}")
print("After removal:", sample_dict)

# Simple word counter
print("\n=== Word Counter ===")
sentence = input("Enter a sentence: ").lower()
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

# 🎯 Your turn!
print("\n🎯 Practice Time!")
# 1. Create a dictionary with information about your favorite book
# 2. Create a dictionary that maps day names to your activities
# 3. Build a simple phone book with names and phone numbers

# Bonus: Dictionary comprehension
print("\n🌟 Bonus: Dictionary Comprehension")
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(f"Numbers and their squares: {squares}")

# Convert two lists into a dictionary
fruits = ["apple", "banana", "orange"]
colors = ["red", "yellow", "orange"]
fruit_colors = {fruit: color for fruit, color in zip(fruits, colors)}
print(f"Fruit colors: {fruit_colors}")
# Advanced Exercise: Data Analysis with Lists and Dictionaries 📊

print("📊 Exercise 3: Working with Data")
print("=" * 45)
print("Let's practice analyzing data using lists and dictionaries!")

# Sample data: student information
students_data = [
    {"name": "Alice", "age": 12, "grade": 7, "subjects": {"math": 95, "science": 87, "english": 92}},
    {"name": "Bob", "age": 13, "grade": 8, "subjects": {"math": 78, "science": 92, "english": 85}},
    {"name": "Carol", "age": 12, "grade": 7, "subjects": {"math": 88, "science": 94, "english": 90}},
    {"name": "David", "age": 14, "grade": 9, "subjects": {"math": 92, "science": 89, "english": 87}},
    {"name": "Emma", "age": 13, "grade": 8, "subjects": {"math": 85, "science": 91, "english": 94}}
]

print("🎓 Student Database:")
print("Here's our sample data to work with:")
for student in students_data:
    print(f"  {student['name']} (Age {student['age']}, Grade {student['grade']})")

print("\n" + "="*50)
print("📝 YOUR TASKS:")
print("Complete the following exercises by writing code below each task.")

# Task 1: Basic Data Access
print("\n1. 📋 BASIC DATA ACCESS")
print("   Find and print the name of the oldest student")
print("   Your code here:")

# TODO: Write code to find the oldest student


print("\n2. 🔢 CALCULATING AVERAGES")
print("   Calculate and print each student's average grade across all subjects")
print("   Your code here:")

# TODO: Write code to calculate each student's average


print("\n3. 📈 SUBJECT ANALYSIS")
print("   Find which subject has the highest class average")
print("   Your code here:")

# TODO: Write code to find the subject with highest average


print("\n4. 🏆 TOP PERFORMER")
print("   Find the student with the highest overall average")
print("   Your code here:")

# TODO: Write code to find the top performing student


print("\n5. 📊 GRADE DISTRIBUTION")
print("   Create a dictionary showing how many students are in each grade level")
print("   Your code here:")

# TODO: Write code to count students per grade


print("\n6. 🎯 FILTERING DATA")
print("   Find all students who scored above 90 in math")
print("   Your code here:")

# TODO: Write code to filter students by math score


print("\n7. 🔍 SEARCH FUNCTION")
print("   Write a function that takes a student name and returns their information")
print("   Your code here:")

def find_student(name):
    # TODO: Write this function
    pass

# Test your function
# print(find_student("Alice"))


print("\n8. ➕ ADD NEW STUDENT")
print("   Add a new student to the database with user input")
print("   Your code here:")

# TODO: Write code to add a new student


print("\n" + "="*50)
print("🌟 BONUS CHALLENGES:")

print("\n🏅 BONUS 1: IMPROVEMENT TRACKER")
print("   Add a 'previous_grades' field to track student improvement")
print("   Calculate who improved the most")

print("\n🏅 BONUS 2: GRADE PREDICTOR")
print("   Based on current grades, predict next semester's grades")
print("   (Add or subtract a random amount between -5 and +5)")

print("\n🏅 BONUS 3: REPORT CARD GENERATOR")
print("   Create a function that generates a formatted report card for any student")

def generate_report_card(student_name):
    # TODO: Write this function
    pass

print("\n🏅 BONUS 4: CLASS STATISTICS")
print("   Calculate comprehensive class statistics:")
print("   - Highest and lowest score in each subject")
print("   - Standard deviation of grades")
print("   - Grade distribution (A, B, C, etc.)")

# Grading scale for reference:
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60

print("\n" + "="*50)
print("💡 HELPFUL HINTS:")
print("• Use loops to go through lists")
print("• Use max() and min() functions for finding extremes")
print("• Use sum() and len() for calculating averages")
print("• Remember that dictionaries use [key] to access values")
print("• You can use list comprehensions for filtering")
print("• Don't forget to test your code as you write it!")

print("\n✅ When you're done, run the program to test your solutions!")
print("    Good luck and have fun with data analysis! 🚀")
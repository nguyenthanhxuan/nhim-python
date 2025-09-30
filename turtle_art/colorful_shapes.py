# Turtle Art: Drawing Fun Shapes! 🐢🎨

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background
screen.title("Turtle Art Fun!")

# Create a turtle
artist = turtle.Turtle()
artist.speed(5)  # Medium speed
artist.color("cyan")

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        artist.forward(size)
        artist.right(90)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        artist.forward(size)
        artist.right(144)

# Function to draw a colorful spiral
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(36):
        artist.color(colors[i % 6])
        artist.forward(i * 2)
        artist.right(91)

# Draw some cool shapes!
print("🎨 Drawing a colorful spiral...")
draw_spiral()

# Move to a new position
artist.penup()
artist.goto(-100, 100)
artist.pendown()

print("⭐ Drawing a star...")
artist.color("yellow")
draw_star(100)

# Move to another position
artist.penup()
artist.goto(100, -100)
artist.pendown()

print("🟦 Drawing squares...")
colors = ["red", "green", "blue", "orange"]
for i, color in enumerate(colors):
    artist.color(color)
    draw_square(50 + i * 10)
    artist.right(10)

# Draw a flower pattern
artist.penup()
artist.goto(0, -150)
artist.pendown()

print("🌸 Drawing a flower...")
artist.color("pink")
for _ in range(36):
    draw_square(50)
    artist.right(10)

print("🎉 Turtle art complete! Close the window when you're done admiring your art!")

# Keep the window open
screen.exitonclick()  # Click to close
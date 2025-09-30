# Fun Project: Turtle Art Gallery 🎨🐢

import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎨 Turtle Art Gallery - Amazing Creations!")
screen.setup(800, 600)

# Create our artist turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed

def draw_rainbow_spiral():
    """Draw a colorful rainbow spiral"""
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    artist.penup()
    artist.goto(-200, 100)
    artist.pendown()
    
    for i in range(100):
        artist.color(colors[i % len(colors)])
        artist.forward(i * 2)
        artist.right(91)

def draw_flower(x, y, petals=8, size=50):
    """Draw a flower at specified coordinates"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    
    # Draw petals
    for _ in range(petals):
        artist.color("pink")
        artist.circle(size)
        artist.right(360 / petals)
    
    # Draw center
    artist.color("yellow")
    artist.begin_fill()
    artist.circle(size // 3)
    artist.end_fill()

def draw_mandala(x, y, size=100):
    """Draw a beautiful mandala pattern"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    
    colors = ["purple", "blue", "cyan", "green", "yellow", "orange", "red"]
    
    for i in range(36):
        artist.color(colors[i % len(colors)])
        artist.circle(size)
        artist.right(10)

def draw_star_field():
    """Draw a field of random stars"""
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(5, 20)
        
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        
        artist.color("white")
        artist.begin_fill()
        for _ in range(5):
            artist.forward(size)
            artist.right(144)
        artist.end_fill()

def draw_geometric_pattern():
    """Draw a complex geometric pattern"""
    artist.penup()
    artist.goto(0, -200)
    artist.pendown()
    
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    
    for i in range(6):
        artist.color(colors[i])
        for _ in range(4):
            artist.forward(100)
            artist.right(90)
        artist.right(60)

def draw_fractal_tree(x, y, length, depth):
    """Draw a fractal tree (recursive art!)"""
    if depth == 0:
        return
    
    artist.penup()
    artist.goto(x, y)
    artist.setheading(90)  # Point up
    artist.pendown()
    
    # Draw trunk
    artist.color("brown")
    artist.forward(length)
    
    # Draw branches
    current_x, current_y = artist.xcor(), artist.ycor()
    
    # Left branch
    artist.setheading(135)  # 45 degrees left
    artist.color("green")
    draw_fractal_tree(current_x, current_y, length * 0.7, depth - 1)
    
    # Right branch
    artist.setheading(45)   # 45 degrees right
    artist.color("green")
    draw_fractal_tree(current_x, current_y, length * 0.7, depth - 1)

def draw_colorful_squares():
    """Draw overlapping colorful squares"""
    artist.penup()
    artist.goto(200, 100)
    artist.pendown()
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i, color in enumerate(colors):
        artist.color(color)
        artist.begin_fill()
        for _ in range(4):
            artist.forward(100 - i * 10)
            artist.right(90)
        artist.end_fill()
        artist.right(15)

def create_art_gallery():
    """Create the complete art gallery"""
    print("🎨 Creating your Turtle Art Gallery...")
    print("🐢 The turtle is hard at work creating masterpieces!")
    
    # Clear the screen
    artist.clear()
    
    # Draw different artworks
    print("🌈 Drawing rainbow spiral...")
    draw_rainbow_spiral()
    
    print("🌸 Drawing flowers...")
    draw_flower(-100, -100, 6, 30)
    draw_flower(150, -50, 8, 25)
    draw_flower(-150, 50, 10, 20)
    
    print("🔮 Drawing mandala...")
    draw_mandala(100, 150, 60)
    
    print("⭐ Drawing star field...")
    draw_star_field()
    
    print("🔶 Drawing geometric pattern...")
    draw_geometric_pattern()
    
    print("🟦 Drawing colorful squares...")
    draw_colorful_squares()
    
    # Add a title
    artist.penup()
    artist.goto(-300, 250)
    artist.pendown()
    artist.color("white")
    artist.write("🎨 TURTLE ART GALLERY 🐢", font=("Arial", 20, "bold"))
    
    print("✨ Art gallery complete!")
    print("🖼️ Enjoy your beautiful creations!")

def interactive_drawing():
    """Let the user create their own art interactively"""
    print("\n🎮 Interactive Drawing Mode!")
    print("Click anywhere on the screen to draw a flower!")
    print("Press 's' for stars, 'm' for mandala, 'c' to clear")
    
    def draw_at_click(x, y):
        draw_flower(x, y, random.randint(5, 12), random.randint(20, 40))
    
    def draw_star_at_click(x, y):
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        artist.color(random.choice(["yellow", "white", "cyan"]))
        artist.begin_fill()
        for _ in range(5):
            artist.forward(random.randint(10, 30))
            artist.right(144)
        artist.end_fill()
    
    def draw_mandala_at_click(x, y):
        draw_mandala(x, y, random.randint(30, 80))
    
    def clear_screen():
        artist.clear()
    
    # Set up click events
    screen.onclick(draw_at_click)
    screen.onkey(lambda: screen.onclick(draw_star_at_click), 's')
    screen.onkey(lambda: screen.onclick(draw_mandala_at_click), 'm')
    screen.onkey(clear_screen, 'c')
    screen.listen()

def main():
    """Main function to run the art gallery"""
    choice = input("What would you like to do?\n1. Create full art gallery\n2. Interactive drawing\nChoice (1 or 2): ")
    
    if choice == "1":
        create_art_gallery()
    elif choice == "2":
        interactive_drawing()
        print("Interactive mode activated! Start clicking and pressing keys!")
    else:
        print("Creating default art gallery...")
        create_art_gallery()
    
    print("\n🎯 Art gallery features:")
    print("• Rainbow spirals with color gradients")
    print("• Procedural flowers with random variations")
    print("• Complex mandala patterns")
    print("• Random star fields")
    print("• Geometric overlapping shapes")
    print("• Interactive drawing capabilities")
    
    print("\n💡 Ideas to extend this project:")
    print("• Add more drawing patterns")
    print("• Save artwork to image files")
    print("• Create animation sequences")
    print("• Add user-controlled drawing tools")
    print("• Make a drawing game or contest")
    
    print("\nClick the window to close when you're done admiring the art! 🎨")
    screen.exitonclick()

if __name__ == "__main__":
    main()

# 🎯 This project demonstrates:
# - Functions for organizing code
# - Loops for creating patterns
# - Lists for storing colors and coordinates
# - Random numbers for variations
# - User interaction with mouse and keyboard
# - Complex graphics programming concepts

# 🚀 Advanced features:
# - Recursive drawing (fractal tree)
# - Event-driven programming (mouse clicks)
# - Procedural generation (random stars)
# - Mathematical patterns (spirals, mandalas)
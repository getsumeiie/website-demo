import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#8B008B")  # Changed background to dark pink
screen.title("Mesmerizing Flower Art")

# Create a turtle named 'artist'
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed
artist.hideturtle()

# Function to draw a petal with gradient effect
def draw_petal(size, angle, color1, color2):
    artist.color(color1)
    artist.begin_fill()
    artist.circle(size, angle)
    artist.left(180 - angle)
    artist.circle(size, angle)
    artist.end_fill()
    artist.color(color2)
    artist.circle(size, angle)
    artist.left(180 - angle)
    artist.circle(size, angle)

def draw_flower(petals, size, x, y):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    colors = ["#00aaff", "#66ccff", "#3399ff"]  # Blue shades
    for i in range(petals):
        draw_petal(size, 60, random.choice(colors), random.choice(colors))
        artist.right(360 / petals)

# Function to draw the flower center with a glow effect
def draw_center(radius, x, y):
    artist.penup()
    artist.goto(x, y - radius)
    artist.pendown()
    artist.color("yellow")
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Function to draw a curved leaf
def draw_leaf(x, y):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color("#32CD32")  # Brighter green for better contrast
    artist.begin_fill()
    artist.circle(70, 60)
    artist.left(120)
    artist.circle(70, 60)
    artist.end_fill()

# Function to draw a glowing stem
def draw_stem(length):
    artist.color("#228B22")  # Deep green for better depth
    artist.pensize(12)
    artist.right(90)
    for _ in range(10):
        artist.forward(length / 10)
        artist.pensize(artist.pensize() - 0.5)

# Function to add small flowers in the background
def draw_small_flowers():
    for _ in range(5):  # Draw 5 small flowers
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(20, 40)
        draw_flower(6, size, x, y)
        draw_center(size // 5, x, y)

# Draw the main flower
draw_flower(12, 100, 0, 0)
draw_center(20, 0, 0)
draw_stem(200)

draw_leaf(0, -100)
draw_leaf(0, -150)

# Draw small background flowers
draw_small_flowers()

# Hide the turtle and display the window
artist.hideturtle()
turtle.done()
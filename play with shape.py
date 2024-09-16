import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.speed(3)  # Set turtle speed

# Function to draw an equilateral triangle
def draw_triangle(side_length, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)  # Each angle of an equilateral triangle is 120 degrees
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(width, height, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a hexagon
def draw_hexagon(side_length, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.left(60)  # Each angle of a hexagon is 60 degrees
    t.end_fill()

# Move turtle to position without drawing
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw the polygons
move_to(-150, 100)
draw_triangle(100, "yellow")

move_to(50, 100)
draw_rectangle(150, 80, "green")

move_to(-50, -100)
draw_hexagon(70, "red")

# Hide turtle and display
t.hideturtle()
screen.mainloop()  # Keep the window open until closed manually

import turtle
import time
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Clock")

# Create a turtle for drawing the clock hands
clock_hands = turtle.Turtle()
clock_hands.speed(0)  # Set the drawing speed to the fastest
clock_hands.color("white")  # Set the color of the clock hands
clock_hands.width(2)  # Set the width of the clock hands

# Create a turtle for drawing the clock numbers
clock_numbers = turtle.Turtle()
clock_numbers.speed(0)
clock_numbers.color("white")
clock_numbers.penup()

# Define a function to draw the clock hands
def draw_hand(length, angle):
    clock_hands.penup()
    clock_hands.goto(0, 0)
    clock_hands.setheading(90)
    clock_hands.right(angle)
    clock_hands.pendown()
    clock_hands.forward(length)
    clock_hands.penup()
    clock_hands.goto(0, 0)

# Define a function to draw the clock numbers
def draw_number(num, angle):
    clock_numbers.penup()
    clock_numbers.goto(5, -10)
    clock_numbers.color("white")
    clock_numbers.setheading(90)
    clock_numbers.right(angle)
    clock_numbers.forward(150)
    clock_numbers.write(num, align="center", font=("Arial", 8, "normal"))
    clock_numbers.hideturtle()

# Draw the clock boundaries
def draw_boundary(size,x,y,color):
    clock_numbers.penup()
    clock_numbers.goto(x,y)
    clock_numbers.color(color)
    clock_numbers.begin_fill()
    clock_numbers.pendown()
    clock_numbers.circle(size)
    clock_numbers.end_fill()
    
draw_boundary(200,5,-190,"white")

draw_boundary(170,5,-160,"black")

# Draw the clock numbers

for i in range(12, 0, -1):
    angle = math.radians((i-12) * 30)
    draw_number(i, math.degrees(angle))

#for i in range(12):
#    angle = math.radians(i * 30)
#    draw_number(i - 1, math.degrees(angle))

# Main loop to animate the clock
while True:
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate the angles for the clock hands
    hour_angle = (hour % 12) * 30 + minute / 2
    minute_angle = minute * 6 + second / 10
    second_angle = second * 6

    # Clear the previous drawings
    clock_hands.clear()

    # Draw the clock hands
    draw_hand(80, hour_angle)
    draw_hand(120, minute_angle)
    draw_hand(140, second_angle)

    # Update the screen
    screen.update()

    # Delay for one second
    time.sleep(0.5)

# Keep the window open
screen.mainloop()
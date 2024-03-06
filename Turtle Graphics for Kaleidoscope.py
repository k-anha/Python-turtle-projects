import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Kaleidoscope with Changing Colors")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest

# Define the number of sides for the polygon
sides = 8

# Define the radius and angle for the kaleidoscope
radius = 100
angle = 360 / sides




# Define the number of frames for the animation
frames = 80

# Making Kaleidoscope in white color
#one more thing you can adjust number of sides and frames as you want so i can change frame from 360 to 80. just to make a quick code 
#Now lets continue
#First our tyrtle will draw white kaleidoscope and then colored under the white kaleidoscope
t.penup()
t.goto(0,200)
t.pendown()
#This will make turtle go to the given coordinates. Now lets start drawing for kaleidoscope
t.color("white")
#initiate a loop
for _ in range(frames):
    for _ in range(sides):
        t.forward(radius)
        t.right(angle)
    t.right(5)
    
#Now we have to make code.for colourful kaleidoscope. So first make an array of colours you want to have.
colours =["red","orange","yellow","green","blue","purple","violet"]
#you can use as much as you want there is no restriction but i suggest it to be no more that 10.
#Now lets move our turtle to the designated position
#I suggest you try to write code for it.
t.penup()
t.goto(0,-200)
t.pendown()
#hope you tried and its ok to be wrong bcz you will learn like this.

for i in range(frames):
    for j in range(sides):
        t.color(colours[(i+j)%len(colours)])
        #This allows turtle to change color dynamically
        #now move tyrtle as in upper code
        t.forward(radius)
        t.right(angle)
    t.right(5)
    #and thats it Its done. Now just hide your turtle 
t.hideturtle()
#and open your screen
screen.mainloop()
#lets see the final output 



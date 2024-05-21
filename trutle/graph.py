import turtle 

# Set up the turtle screen and set the background color to white 
screen = turtle.Screen() 
screen.bgcolor("green") 

# Create a new turtle and set its speed to the fastest possible 
pen = turtle.Turtle() 
pen.speed(2) 

# Set the fill color to red 
pen.fillcolor("red") 
pen.begin_fill() 

# Draw the any graph using co-ordinate system
pen.forward(100)
pen.right(120)
pen.forward(100)
# pen.end_fill() 
# pen.hideturtle() 
pen.right(120)
pen.forward(100)
pen.right(120)





# End the fill and stop drawing 
# pen.end_fill() 
# pen.hideturtle() 

# Keep the turtle window open until it is manually closed 
turtle.done() 

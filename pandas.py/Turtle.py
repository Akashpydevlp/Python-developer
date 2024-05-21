# import turtle  

# my_turtle = turtle.Turtle()
# my_turtle.forward(100)  # distance
# my_turtle.right(90)  # angel  
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# turtle.done()


# import turtle library
# import turtle  

# create a colour full graphical screen         #    
# my_window = turtle.Screen() 
# my_window.bgcolor("green")   # creates a graphics window
 
 
 
 
 
# # create a graphical pen 
# my_pen = turtle.Turtle() 
      
# my_pen.forward(150)  
# my_pen.color("white")         
# my_pen.left(90)               
# my_pen.forward(75)
#     #  for arrow



# turtle.done()


# import turtle library
# import turtle             
# my_pen = turtle.Turtle()      
# for i in range(4):
#    my_pen.forward(50)           
#    my_pen.left(90)               
# turtle.done()


# import turtle library
# import turtle             
# polygon = turtle.Turtle()
# my_num_sides = 3
# my_side_length = 20
# my_angle = 360.0 / my_num_sides
# for i in range(my_num_sides):
#    polygon.forward(my_side_length)           
#    polygon.right(my_angle) 
# turtle.done()


# import turtle 
# x=turtle.Turtle()
# x=turtle.Screen()

# x.bgcolor("green")

# # for Trangle 
# x.forward(100)
# x.left(120)
# x.forward(100)
# x.left(120)
# x.forward(100)


# x.goto(100,-100)
# x.goto(200,0)
# x.goto(100,100)
# x.goto(0,0)



# turtle.done()








import turtle 

# Set up the turtle screen and set the background color to white 
screen = turtle.Screen() 
screen.bgcolor("white") 

# Create a new turtle and set its speed to the fastest possible 
pen = turtle.Turtle() 
pen.speed(0) 

# Set the fill color to red 
pen.fillcolor("red") 
pen.begin_fill() 

# Draw the circle with a radius of 100 pixels 
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)


# End the fill and stop drawing 
pen.end_fill() 
pen.hideturtle() 

# Keep the turtle window open until it is manually closed 
turtle.done() 

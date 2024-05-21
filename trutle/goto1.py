import turtle

pen=turtle.Turtle()
screen = turtle.Screen() 
screen.bgcolor("green") 

pen.fillcolor("red") 
pen.begin_fill()

pen.goto(-60,-60)
pen.goto(60,-60)
pen.goto(0,0)
pen.end_fill() 
pen.hideturtle() 
pen.fillcolor("yellow") 
pen.begin_fill()
pen.goto(0,40)
pen.goto(60,-60)
pen.goto(0,0)
pen.end_fill() 
pen.hideturtle() 

pen.fillcolor("blue") 
pen.begin_fill()
pen.goto(0,40)
pen.goto(-60,-60)
pen.goto(0,0)
pen.end_fill() 
pen.hideturtle() 

turtle.done()





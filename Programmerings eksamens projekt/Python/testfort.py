import turtle as t

# create turtle

# turtle_one = t.Turtle()
# turtle_four = t.Turtle()
# turtle_three = t.Turtle()
# x, y = turtle_one.position()
# turtle_four.penup()
# turtle_four.goto(x,y-10)
# turtle_four.pendown()
# turtle_three.penup()
# turtle_three.goto(x,y+10)
# turtle_three.pendown()

# turtle_one.penup()
# turtle_one.forward(50)
# turtle_one.pendown()

# turtle_four.forward(50)
# turtle_three.forward(50)



# # Drawing the AND operator
# circle_radius = 50
# turtle_one.right(90)
# turtle_one.forward(50)
# turtle_one.left(90)
# turtle_one.forward(25)
# turtle_one.circle(circle_radius, extent=180)
# turtle_one.forward(25)
# turtle_one.left(90)
# turtle_one.forward(50)
# turtle_one.penup()
# turtle_one.left(90)
# turtle_one.forward(75)
# turtle_one.pendown()
# turtle_one.forward(50)


# Drawing the OR operator

turtle = t.Turtle()
turtle_five = t.Turtle()
turtle_six = t.Turtle()
# turtle_two.hideturtle()

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()

turtle.forward(61.60)
circle_radius_two = 86.6025403784385
turtle.left(180)
turtle.forward(11.60)
turtle.penup()
turtle.left(90)
turtle.forward(43.3)
turtle.pendown()
turtle.left(90)

# Drawing the ellipse shapes
turtle.circle(circle_radius_two, extent = 60)
turtle.left(60)
turtle.circle(circle_radius_two, extent=60)

# Drawing the final part

turtle.left(90)
turtle.penup()
turtle.forward(86.6)
turtle.left(150)
turtle.pendown()
turtle.circle(circle_radius_two, extent=60)
turtle.setheading(90)
turtle.left(180)
turtle.penup()
turtle.forward(86.60254037844385/2)
turtle.left(90)
turtle.forward(75.00000000000001)
turtle.pendown()
turtle.forward(50)


t.mainloop()
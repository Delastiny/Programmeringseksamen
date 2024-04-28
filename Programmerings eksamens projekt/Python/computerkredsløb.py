# Importing turtle as t for documentation of inbuilt functions of turtle
import turtle as t
import random
# importing everything from logic.py
from logic import *


# Purpose of function: Turtle draws the beginning of a circuit
def drawBeginning(turtle_one, turtle_two, turtle_three, x,y):

    # Turtles start position for the first input
    turtle_one.penup()
    turtle_one.goto(x, y)
    turtle_one.pendown()

    turtle_two.penup()
    turtle_two.goto(x, y)
    turtle_two.pendown()

    #Drawing the beginning
    drawForward(turtle_one, 1)
    turnAround(turtle_one, 1)
    drawForward(turtle_one, 1)
    turnAround(turtle_one, 3)
    drawForward(turtle_one, 1)

    # turlte two start of circuit
    drawForward(turtle_two, 1)
    turnAround(turtle_two, 3)
    drawForward(turtle_two, 1)
    turnAround(turtle_two, 1)
    drawForward(turtle_two, 1)
    
    #Drawing the starting value
    the_Value = randomInput()
    turtle_three.penup()
    turtle_three.goto(x-10,y-7)
    turtle_three.write(str(the_Value), font=("Arial", 10, "normal"))

    return the_Value


# Draw second continuation
def drawContinuationSec(turtle_one, turtle_two):
    drawForward(turtle_one, 2)
    turnAround(turtle_one, 1)
    drawForward(turtle_one, 3)
    turnAround(turtle_one, 3)
    drawForward(turtle_one, 2)

    drawForward(turtle_two, 1)
    turnAround(turtle_two, 3)
    drawForward(turtle_two, 5)
    turnAround(turtle_two, 1)
    drawForward(turtle_two, 3)

#Draw third continuation
def drawContinuationThird(turtle_one, turtle_two):
        turnAround(turtle_one, 3)
        drawForward(turtle_one,2)
        turtle_one.forward(20)
        turnAround(turtle_one, 1)
        drawForward(turtle_one, 2)
        turnAround(turtle_two, 1)
        drawForward(turtle_two, 2)
        turtle_two.forward(20)
        turnAround(turtle_two, 3)
        drawForward(turtle_two, 2)

# Purpose of function: Turtle draws a NOT gate:
def drawNOT(turtlecoor,turtle, A):
    # Finding the start coordinates
    x, y = turtlecoor.position()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


    drawForward(turtle, 2)


    turtle.left(90)
    turtle.forward(25)
    for _ in range(2):
        # Drejer den med 120 grader for at sikre at hver vinkel er 60 grader
        turtle.right(120)
        # Længde af 50 for hver side
        turtle.forward(50)

    turtle.right(120)
    turtle.forward(25)

    turtle.right(90)
    turtle.penup()
    #Lavet udregninger via pythagorous sætning for at finde frem til at når a = 25, b er ukendt og c = 50, hvor sætningen lyder a^2+b^2=c^2, er b = 43,301270189221932338186158537647
    turtle.forward(43.301270189221932338186158537647)
    turtle.pendown()

    drawCircle(3.9, turtle)

    # Return the notgate value
    return notGate(A)

#Purpose of function: Turtle draws an AND gate
def drawAND(turtle, turtle_var, A, B, condition = True):
    x, y = turtle_var.position()
    turtle.penup()
    turtle.goto(x,y-10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()

    circle_radius = 50
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.circle(circle_radius, extent=180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(75)
    turtle.pendown()

    if condition:
        turtle.forward(50)

    # Return andgate value
    return andGate(A,B)

# draw AND NOT

def drawANDNOT(turtle, turtle_var, A, B):
    drawAND(turtle, turtle_var, A, B, False)
    drawCircle(3.9, turtle)

    return notGate(andGate(A,B))


def drawOR(turtle, turtle_var, A, B,condition=True):
    x, y = turtle_var.position()
    turtle.penup()
    turtle.goto(x,y-30)
    turtle.forward(5)
    turtle.pendown()

    circle_radius_two = 86.6025403784385
    turtle.left(180)
    turtle.penup()
    turtle.forward(11.60)
    turtle.pendown()
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

    if condition:
        drawForward(turtle, 1)

    # Return or gate value
    return orGate(A,B)


# draw OR NOT

def drawORNOT(turtle, turtle_var, A, B):
    drawOR(turtle, turtle_var,A, B, False)
    drawCircle(3.9, turtle)
    
    return notGate(orGate(A,B))

# Draw a circle
def drawCircle(r, turtle_one):
    circle_radius = r
    turtle_one.penup()
    turtle_one.forward(circle_radius)
    turtle_one.right(90)
    turtle_one.forward(circle_radius)
    turtle_one.left(90)
    turtle_one.pendown()
    turtle_one.circle(circle_radius)

    turtle_one.penup()
    turtle_one.circle(circle_radius, extent=90)
    turtle_one.right(90)
    turtle_one.pendown()
    turtle_one.forward(50)


# an attempt at drawing a boolean circuit
# setting up some functions first to make it easier

def drawForward(turtle_var,number):
    for i in range (0, number):
        turtle_var.forward(50)

def turnAround(turtle_var, number):
    for i in range (0, number):
        turtle_var.left(90)

# Creating turtles
turtle_one = t.Turtle()
turtle_two = t.Turtle()
turtle_three = t.Turtle()
turtle_four = t.Turtle()
turtle_five = t.Turtle()
turtle_six = t.Turtle()
# Turtles used for values
turtle_seven = t.Turtle()
turtle_eight = t.Turtle()

turtle_nine = t.Turtle()
turtle_ten = t.Turtle()

# Five extra turtles for the demo questions
turtle_eleven = t.Turtle()
turtle_twelve = t.Turtle()
turtle_thirteen = t.Turtle()
turtle_fourteen = t.Turtle()
turtle_fifteen = t.Turtle()

# function for hiding the turtle and speeding them up
def hidingTheTurtles(turtle_list):
    a = 0
    for i in range(0, len(turtle_list)):
        turtle_list[a].hideturtle() #Hides each of the turtles in the list
        turtle_list[a].speed(0) # set to 0 to speed it up as fast as possible and ignore the animation
        a += 1 # variable to iterate through the list

list_of_turtles = [turtle_one, turtle_two, turtle_three, turtle_four, turtle_five, turtle_six, turtle_seven, turtle_eight,turtle_nine, turtle_ten, turtle_eleven, turtle_twelve, turtle_thirteen, turtle_fourteen, turtle_fifteen]
hidingTheTurtles(list_of_turtles)

# Text variables for the questions
question_One = "Hvad sker der med værdien ved hver operator i dette kredsløb?"
question_Two = "Hvad er det endelige output af dette kredsløb i booleansk værdi?"
list_of_questions = [question_One, question_Two]

random_question = random.choice(list_of_questions)

#Writing out the question
turtle_three.penup()
turtle_three.goto(-300, 250)
turtle_three.pendown()
turtle_three.write(random_question, font=("Arial", 15, "normal"))


# If question one
def question_one_demo(turtle_one, turtle_two, turtle_three, value_one=None, value_two=None, value_three= None, value_four =None, value_five =None):
    turtle_eleven.penup()
    turtle_twelve.penup()
    turtle_thirteen.penup()
    turtle_fourteen.penup()
    turtle_fifteen.penup()

    x_one, y_one = turtle_one.position()
    x_two, y_two = turtle_two.position()
    x_three, y_three = turtle_three.position()

    turtle_eleven.goto(x_one - 100, y_one+35)
    turtle_eleven.write("1", font=("Arial", 10, "normal"))
    turtle_twelve.goto(x_two - 100, y_two + 35)
    turtle_twelve.write("2", font=("Arial", 10, "normal"))
    turtle_thirteen.goto(x_one + 30, y_one + 35)
    turtle_thirteen.write("3", font=("Arial", 10, "normal"))
    turtle_fourteen.goto(x_two  +30, y_two + 35)
    turtle_fourteen.write("4", font=("Arial", 10, "normal"))
    turtle_fifteen.goto(x_three +20, y_three+30)
    turtle_fifteen.write("5", font=("Arial", 10, "normal"))

    correct_value_one = False
    correct_value_two = False
    correct_value_three = False
    correct_value_four = False
    correct_value_five = False

    while correct_value_one == False:
        question_value_one = input("Hvad er værdien efter nr. 1 operator?")
        if int(question_value_one) == value_one:
            print("Det er korrekt!")
            correct_value_one = True
    
    while correct_value_two == False:
        question_value_two = input("Hvad er værdien efter nr. 2 operator?")
        if int(question_value_two) == value_two:
            print("Det er korrekt!")
            correct_value_two = True

    while correct_value_three == False:
        question_value_three = input("Hvad er værdien efter nr. 3 operator?")
        if int(question_value_three) == value_three:
            print("Det er korrekt!")
            correct_value_three = True

    while correct_value_four == False:
        question_value_four = input("Hvad er værdien efter nr. 4 operator?")
        if int(question_value_four) == value_four:
            print("Det er korrekt!")
            correct_value_four = True

    while correct_value_five == False:
        question_value_five = input("Hvad er værdien efter nr. 5 operator?")
        if int(question_value_five) == value_five:
            print("Det er korrekt!")
            correct_value_five = True
    

# if question two
def question_two_demo(final_output_value):
    converseionOfBoolean(final_output_value)
    correct_answer = False

    while correct_answer == False:
        question_for_final_output = input("Hvad er det endelige output i booleansk værdi?").lower()
        if question_for_final_output == "false":
            question_for_final_output = False
        elif question_for_final_output == "true":
            question_for_final_output = True
        else:
            question_for_final_output = None
        
        if int(question_for_final_output) == final_output_value:
            print("Det er korrekt!")
            correct_answer = True
        else:
            print("Det er forkert, prøv igen")
    
#lists beginning with drawAND
list_one = [drawBeginning, drawNOT, drawContinuationSec, drawAND,  drawContinuationThird,drawOR]
list_two = [drawBeginning, drawNOT, drawContinuationSec, drawAND, drawContinuationThird, drawAND]
list_three = [drawBeginning, drawNOT, drawContinuationSec, drawAND, drawContinuationThird, drawANDNOT]
list_five = [drawBeginning, drawNOT, drawContinuationSec, drawAND, drawContinuationThird, drawORNOT]

#lists beginning with drawANDNOT
list_four = [drawBeginning, drawNOT, drawContinuationSec, drawANDNOT, drawContinuationThird, drawAND]
list_five = [drawBeginning, drawNOT, drawContinuationSec, drawANDNOT, drawContinuationThird, drawANDNOT]
list_six = [drawBeginning, drawNOT, drawContinuationSec, drawANDNOT, drawContinuationThird, drawOR]
list_seven = [drawBeginning, drawNOT, drawContinuationSec, drawANDNOT, drawContinuationThird, drawORNOT]

#lists beginning with #drawOR
list_eight = [drawBeginning, drawNOT, drawContinuationSec, drawOR, drawContinuationThird, drawAND]
list_nine = [drawBeginning, drawNOT, drawContinuationSec, drawOR, drawContinuationThird, drawANDNOT]
list_ten = [drawBeginning, drawNOT, drawContinuationSec, drawOR, drawContinuationThird, drawOR]
list_eleven = [drawBeginning, drawNOT, drawContinuationSec, drawOR, drawContinuationThird, drawORNOT]

# lists beginning with drawORNOT
list_twelve = [drawBeginning, drawNOT, drawContinuationSec, drawORNOT, drawContinuationThird, drawOR]
list_thirteen = [drawBeginning, drawNOT, drawContinuationSec, drawORNOT, drawContinuationThird, drawANDNOT]
list_fourteen = [drawBeginning, drawNOT, drawContinuationSec, drawORNOT, drawContinuationThird, drawAND]
list_fifteen = [drawBeginning, drawNOT, drawContinuationSec, drawORNOT, drawContinuationThird, drawORNOT]





total_list = [list_one, list_two,list_three, list_four, list_five, list_six, list_seven, list_eight, list_nine, list_ten, list_eleven, list_twelve, list_thirteen,list_fourteen, list_fifteen]

chosen_list = random.choice(total_list)
print(chosen_list)


def randomizedCircuit(list):
    

    iterable_Variable_For_List = 0
    for i in range(0, len(list)):
        match iterable_Variable_For_List:
            case 0:
                #Draws the beginning
                value_input = list[iterable_Variable_For_List](turtle_one, turtle_two, turtle_seven, -300, 100)
                value_input_two = list[iterable_Variable_For_List](turtle_five, turtle_six, turtle_eight, -300, -100)
                #print("Value_input", value_input)
                #print("Value_input_two", value_input_two)
                iterable_Variable_For_List +=1
            case 1:
                #Draws the not operator
                A = list[iterable_Variable_For_List](turtle_one, turtle_one, value_input)
                C = list[iterable_Variable_For_List](turtle_six, turtle_six, value_input_two)
                #print("A", A)
                #print("C", C)
                iterable_Variable_For_List += 1
            case 2:
                #Draws the continuation
                list[iterable_Variable_For_List](turtle_five, turtle_two)
                iterable_Variable_For_List += 1
            case 3:
                #Draws the ?? operator
                B = list[iterable_Variable_For_List](turtle_four, turtle_one, A, value_input_two)
                D = list[iterable_Variable_For_List](turtle_nine, turtle_six, C, value_input)
                #print("B", B)
                #print("D", D)
                iterable_Variable_For_List += 1
            case 4:
                #Draws the third continuation
                list[iterable_Variable_For_List](turtle_four, turtle_nine)
                iterable_Variable_For_List+= 1
            case 5:
                final = list[iterable_Variable_For_List](turtle_ten, turtle_four, B, D)
                #print("Final",  final)


    if random_question == question_One:
        question_one_demo(turtle_one, turtle_six, turtle_four, A, C, B, D, final)
    elif random_question == question_Two:
        question_two_demo(final)


randomizedCircuit(chosen_list)

t.mainloop()
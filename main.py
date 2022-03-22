'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(darty, width,top_left_x, top_left_y):
  darty.up()
  darty.goto(top_left_x, top_left_y)
  darty.down()
  for i in range(4):
    darty.forward(width)
    darty.right(90)
"""
This function draws a square
darty(object)the object drawing the square
width(integer)the size of the squaee
top_left_x(integer)the x coordinate of the top left corner
top_left_y(integer)the y coordinate of the top left corner
"""

def drawLine(darty, x_start, y_start, x_end, y_end):
  darty.up()
  darty.goto(x_start, y_start)
  darty.down()
  darty.goto(x_end, y_end)
"""
The function draws a straight line
darty(object)the object that draws the line
x_start(integer)the x coordinate where the line starts
y_start(integer)the y coordinate where the line starts
x_end(integer)the x coordinate where the line ends
y_end(integer)the y coordinate where the line ends
"""

def drawCircle(darty, radius):
  darty.up()
  darty.goto(0,-radius)
  darty.down()
  darty.circle(radius,steps=360) 
"""
the function draws a circle
darty(object)the object drawing the circle
radius(integer)the radius of the cirdle
"""

def setUpDartboard(window, darty):
  window.setworldcoordinates(-2, -2, 2, 2)
  drawSquare(darty, 2, -1, 1)
  drawLine(darty,-1,0,1,0)
  drawLine(darty,0, -1, 0, 1)
  drawCircle(darty,-1)
"""
the function draws a dartboard by calling the previous functions
window(object)the screen that the dartboard is on
darty(object)the object the draws the dartboard
"""

def throwDart(darty):
  x_coordinate=random.uniform(-1,1)
  y_coordinate=random.uniform(-1,1)
  darty.up()
  darty.goto(x_coordinate, y_coordinate)
  if darty.distance(0,0)<1:
    darty.color("green")
  elif darty.distance(0,0)>1:
    darty.color('red')
  darty.dot()
  darty.color("black")
"""
the function throws virtual darts at the dartborad and colors the dots based on where they hit
darty(object)the object that is used to make the dots where the darts hit
"""

def isInCircle(darty):
  if darty.distance(0,0)<1:
    return True
  elif darty.distance(0,0)>1:
    return False 
"""
The function returns a statment based on a conditional
darty(object)makes the dots on the dartboard
True(statement)given if the darts are in the circle
False(statement)given if the the darts are out of the circle
"""

def playDarts(darty):
  player1_points = 0
  player2_points = 0
  player1=throwDart
  player2=throwDart
  for i  in range(10):
    player1(darty)
    if isInCircle(darty):
      player1_points += 1
    player2(darty)
    if isInCircle(darty):
      player2_points += 1
    print("player 1 score: " + str(player1_points))
    print("player 2 score: " + str(player2_points))
  if player1_points > player2_points:
    print("player 1 wins")
  elif player1_points < player2_points:
    print("player 2 wins")
  elif player1_points == player2_points:
    print("tie")
"""
simulates a dart game between two players and keeps track of each ones score
darty(object)makes the dots simulating the visual darts
"""
    
def montePi(darty,number_darts):
  pi_estimation=0
  pi=throwDart
  for i in range(number_darts):
    pi(darty)
    if isInCircle(darty):
      pi_estimation += 1
  return pi_estimation/number_darts*4
"""
the function estimates the value of pi by caluclating the ratio of amount of darts in the circle to total darts thrown
darty(object)makes the dots that simulate as darts
number_darts(integr)the number of darts being thrown
pi_estimation/number_darts*4(float)the approximation of pi
"""
    
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()

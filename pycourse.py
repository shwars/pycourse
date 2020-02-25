# Functions for Introduction to Python Course

## Turtle Graphics
import jturtle as turtle

def square(x):
  """
  Draw a square with side x
  """
  for t in range(4):
      turtle.forward(x)
      turtle.right(90)
        
def house(size):
  """
  Draw a house of specified size
  """
  square(size)
  turtle.forward(size)
  turtle.right(30)
  turtle.forward(size)
  turtle.right(120)
  turtle.forward(size)
  turtle.right(30)

  turtle.penup()
  turtle.forward(2*size/3)
  turtle.right(90)
  turtle.forward(size/3)
  turtle.pendown()

  square(size/3)
  turtle.penup()
  turtle.forward(2*size/3)
  turtle.left(90)
  turtle.forward(size/3)
  turtle.left(180)
  turtle.pendown()

  
# Quadratic Equations
import math
import random

def solve(a,b,c):
    d = b*b-4*a*c
    if d>=0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return (x1,x2)
    else:
        return None

def coef(a,x):
    if a==0:
        return ""
    elif a==1:
        return "+"+x
    elif a==-1:
        return "-"+x
    elif a<0:
        return "-"+str(-a)+x
    else:
        return "+"+str(a)+x


def equation(a,b,c):
    s = coef(a,"x^2")+coef(b,"x")+coef(c,"")
    if s[0] == "+":
        return s[1:]
    else:
        return s
      
def random_equation():
    a = random.randint(1,5)*random.choice([-1,1])
    b = random.randint(-10,10)
    c = random.randint(-20,20)
    return (a,b,c)

      
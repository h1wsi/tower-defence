
import turtle

turtle.speed(0)
turtle.bgcolor("white")
turtle.bgpic("src/space.png")
turtle.setundobuffer(1)
turtle.ht()

class Screen(turtle.Turtle):
	def __init__(self, object, color, x0, y0):
		turtle.Turtle.__init__(self, shape = object)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(x0, y0)
		self.speed = 0

prn = input("")
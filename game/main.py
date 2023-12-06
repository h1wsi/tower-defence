
import turtle

turtle.speed(0)
turtle.bgcolor("white")
turtle.bgpic("src/space.png")
turtle.setundobuffer(1)
turtle.ht()

class Screen(turtle.Turtle):

	# Инициализация игровой области (экрана)
	def __init__(self, object, color, x0, y0):
		turtle.Turtle.__init__(self, shape = object)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(x0, y0)
		self.speed = 1
	
	# При столкновении с границами экрана поворот объекта на 60 градусов
	# и возвращение его внутрь игровой области 
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() < -300:
			self.rt(60)
			self.setx(-300)
			
		elif self.xcor() > 300:
			self.rt(60)
			self.setx(300)
			
		if self.ycor() < -300:
			self.rt(60)
			self.sety(-300)		
		
		elif self.ycor() > 300:
			self.rt(60)
			self.sety(300)

class Player(Screen):

	# Определение вида модели игрока и его характеристик
	def __init__(self, object, color, x0, y0):
		Screen.__init__(self, object, color, x0, y0)
		self.speed = 0
		self.lives = 5
		self.shapesize(stretch_wid=0.8, stretch_len=1.3, outline=None)
	 
	def left(self):
		self.lt(60)
		
	def right(self):
		self.rt(60)
				
	def boost(self):
		self.speed += 2
		
	def deboost(self):
		self.speed -= 1

# Создание объектов
player = Player("circle", "yellow", 0.0, 0.0)

# Считывание событий клавиатуры (стрелки)
turtle.onkey(player.left, "Left")
turtle.onkey(player.right, "Right")
turtle.onkey(player.boost, "Up")
turtle.onkey(player.deboost, "Down")
turtle.listen()

while True:
	player.move()

# prn = input("")
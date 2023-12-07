
import turtle
import random

turtle.speed(0)
turtle.bgcolor("black")
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

	# функция для обнаружения столкновений между объектами через проверку расстояния между их центрами
	def bump(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and (self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() - 20)) and (self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False

class Game():
	def __init__(self):
		
		self.score = 0
		self.state = "play"
		self.pen = turtle.Turtle()
		self.lives = 5
		
	def frame(self):
		# установка скорости, толщины пера, и перенос pen в верхний левый угол
		self.pen.speed(0)
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		
		# pen рисует рамку, поворачивая на 90 градусов после каждой стороны
		for _ in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()
	
	def scoreboard(self):

		# Создание борды с очками и оставшимися жизнями
		self.pen.undo()
		if game.lives > 0:
			message = f"Lives: {self.lives} Score: {self.score}"		
		else: 
			message = f"Score: {self.score}"

		self.pen.penup()
		self.pen.color("white")
		self.pen.goto(-300, 310)
		self.pen.write(message, font=("Conslolas", 14, "normal"))
		self.pen.ht()

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

class Enemy(Screen):
	def __init__(self, object, color, x0, y0):
		Screen.__init__(self, object, color, x0, y0)

		self.speed = 2
		self.setheading(random.randint(0,360))

# Создание объектов
game = Game()
game.frame()
game.scoreboard()

player = Player("triangle", "yellow", 0.0, 0.0)
enemy = Enemy("circle", "red", -100, 0)

# Считывание событий клавиатуры (стрелки)
turtle.onkey(player.left, "Left")
turtle.onkey(player.right, "Right")
turtle.onkey(player.boost, "Up")
turtle.onkey(player.deboost, "Down")
turtle.listen()

# Цикл для работы игры
while True:

	player.move()
	enemy.move()

	if player.bump(enemy):
		
		x = random.randint(-200, 200)
		y = random.randint(-200, 200)
		enemy.goto(x, y)
		enemy.speed += 1
		game.lives -= 1
		game.scoreboard()
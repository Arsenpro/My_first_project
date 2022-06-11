import pygame

#устанавливаем пайгейм
pygame.init()

#создаем игровое окно размерами 500 на 500 пикселей
win = pygame.display.set_mode((500, 500))

#напишем название игры, которое будет отображаться в открытом окне
pygame.display.set_caption('Cubes Game')

#ниже мы загружаем изображения игрока, которые лежат у нас в папке с игрой (если бы лежали в другом месте, нужно было прописать путь)
walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
pygame.image.load('right_4.png'), pygame.image.load('right_5.png'),
pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png'), pygame.image.load('left_5.png'),
pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg') #это фон игрового поля
playerStand = pygame.image.load('idle.png')


clock = pygame.time.Clock()

#заранее прописываем параметры нашего игрока
x = 50
y = 425
widht = 60 #ширина согласно размеру изображению игрока
height = 71 #высота согласно размеру изображению игрока
speed = 10

#добавляем переменные для прыжков 
isJump = False
jumpCount = 10 

left = False # переменная говорит о том что вначале игры игрок не двигается
right = False # переменная говорит о том что вначале игры игрок не двигается
animCount = 0
lastMove = "right"


class snaryad(): #создаем класс снаряда, которым будет стрелять игрок
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y 
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing #напрваление полета снаряда

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
	global animCount
	win.blit(bg, (0, 0)) #подгружаем изображение для фона, начинает прорисовываться с начальных координат 0, 0

	if animCount + 1 >= 30:
		animCount = 0

	if left:
		win.blit(walkLeft[animCount // 5], (x,y))
		animCount += 1
	elif right:
		win.blit(walkRight[animCount // 5], (x,y))
		animCount += 1
	else:
		win.blit(playerStand, (x,y))

	for bullet in bullets:
		bullet.draw(win)

		
	pygame.display.update() #необходимо постоянное обновление окна, что бы что то отображалось	

# Создаем цикл, благодаря которому игра будет запущена до тех пор, пока run = True
run = True

bullets =[]

while run:
	clock.tick(30)

	for even in pygame.event.get(): #перебираем массив, все те события которые вообще могут происходить и если это событие приводит к тому что приложение закрывается, то значение run = False
		if even.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed() #создаем список в который мы помещаем все кнопки которые жмем (вместе и по отдельности)

	if keys[pygame.K_f]:
		if lastMove == "right":
			facing = 1
		else: 
			facing = -1


		if len(bullets) < 5:
			bullets.append(snaryad(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), facing))

	if keys[pygame.K_LEFT] and x > 10: #дополнительное условие после and создает границы окна, за которые игрок не сможет выйти
		x -= speed
		left = True
		right = False
		lastMove = "left"

	elif keys[pygame.K_RIGHT] and x < 450:
		x += speed
		left = False
		right = True
		lastMove = "right"

	else:
		left = False
		right = False
		animCount = 0

	if not(isJump): #проверка, если игрок не прыгает, тогда перемещаем игрока вверх вниз или прыгаем
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:
				y -= (jumpCount ** 2) / 2  
			jumpCount -= 1 

		else: 
			isJump = False
			jumpCount = 10								
	
	drawWindow()
		

pygame.quit()

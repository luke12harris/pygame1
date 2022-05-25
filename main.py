import pygame

#initialise the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((420, 420))

#name and icon
icon = pygame.image.load("Big_Chungus_Logo.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Not Mario")

#chungus
chungusImage = pygame.image.load("chungus_character_small.png")
chungusX = 69
chungusY = 69
chungusXChange = 0
chungusYChange = 0


def player(x, y):  #draws chungus
    screen.blit(chungusImage, (x, y))

def movement(direction):
    pass

running = True
speed = 0.2
#the game loop
while running:
    pygame.time.delay(1)

    #screen color
    screen.fill(("red"))

    for event in pygame.event.get():  #an event is any action within the window

        #quit
        if event.type == pygame.QUIT:
            running = False

        #player movement
        if event.type == pygame.KEYDOWN:  #pressed key

            if event.key == pygame.K_LEFT:
                chungusXChange -= speed

            if event.key == pygame.K_RIGHT:
                chungusXChange += speed

            if event.key == pygame.K_UP:
                chungusYChange -= speed

            if event.key == pygame.K_DOWN:
                chungusYChange += speed

        if event.type == pygame.KEYUP: #released key
            if event.key == pygame.K_LEFT:
                chungusXChange += speed

            if event.key == pygame.K_RIGHT:
                chungusXChange -= speed

            if event.key == pygame.K_UP:
                chungusYChange += speed

            if event.key == pygame.K_DOWN:
                chungusYChange -= speed

    chungusX+=chungusXChange
    chungusY+=chungusYChange

    for i in range (0,420,60):
        pygame.draw.line(screen, 'white', (1,i), (600,i), 2)
        pygame.draw.line(screen, 'white', (i,1), (i,600), 2)

    #creates a boarder, chungus can't leave!
    if chungusX < 20:
        chungusX = 20

    if chungusY < 5:
        chungusY = 5

    if chungusX > 300:
        chungusX=300

    if chungusY > 280:
        chungusY = 280

    player(chungusX, chungusY)  #updates position

    pygame.display.update()

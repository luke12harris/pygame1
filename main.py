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


running = True
#the game loop
while running:

    #screen color
    screen.fill(("red"))

    for event in pygame.event.get():  #an event is any action within the window

        #quit
        if event.type == pygame.QUIT:
            running = False

        #player movement
        if event.type == pygame.KEYDOWN:  #pressed key

            if event.key == pygame.K_LEFT:
                chungusXChange = -0.5

            if event.key == pygame.K_RIGHT:
                chungusXChange = +0.5

            if event.key == pygame.K_UP:
                chungusYChange = -0.5

            if event.key == pygame.K_DOWN:
                chungusYChange = +0.5

        if event.type == pygame.KEYUP:  #released key
            chungusXChange = 0
            chungusYChange = 0

    chungusX += chungusXChange
    chungusY += chungusYChange

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

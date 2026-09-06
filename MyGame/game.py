import pygame

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0,255,0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A race")
clock = pygame.time.Clock()

shippImg = pygame.image.load('spaceShip.png')
widthImg = 170
heightImg = 170

ship = pygame.transform.scale(shippImg, (widthImg,heightImg))

def spaceShip(x,y):
    gameDisplay.blit(ship,(x,y))


def game_loop():
    x = (display_width * 0.38)
    y = (display_height * 0.7)

    x_sum = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_sum = -5
                else:
                    x_sum = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_sum = 0

            print(event)
        x += x_sum

        gameDisplay.fill(black)
        spaceShip(x,y)

        if x > display_width - widthImg or x < 0:
            gameExit = True

        pygame.display.update() #Updates the parameters on the method
        clock.tick(60) #fps (frames per second)

game_loop()
pygame.quit()
quit()
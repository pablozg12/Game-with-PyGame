import pygame
import time
import random

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0,255,0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A Space Adventure")
clock = pygame.time.Clock()

shippImg = pygame.image.load('Img/spaceShip.png')
widthImg = 100
heightImg = 185

explodedImg = pygame.image.load('Img/boom.png')
exWImg = 200
exHImg = 200

alienImg = pygame.image.load('Img/alien.png')
alienWImg = 170
alienHImg = 120

crashed = False

ship = pygame.transform.scale(shippImg, (widthImg,heightImg))
explode = pygame.transform.scale(explodedImg,(exWImg, exHImg))
alienB = pygame.transform.scale(alienImg,(alienWImg, alienHImg))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count),True, white)
    gameDisplay.blit(text,(0,0))

def stars(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def blast(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def alien(thingx, thingy):
    gameDisplay.blit(alienB,(thingx,thingy))

def spaceShip(x,y):
    gameDisplay.blit(ship,(x,y))

def explotion(x,y):
    gameDisplay.blit(explode,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def crash():
    message_display('You Crashed!!!')    

def game_loop():
    x = (display_width * 0.42)
    y = (display_height * 0.7)

    x_sum = 0

    num_stars = 50 #Number of stars
    stars_List = [] #Star's list
    for _ in range(num_stars):
        star_x = random.randrange(0,display_width)
        star_y = random.randrange(0, display_height)
        star_speed = random.randint(5,9) #Different speed
        stars_List.append([star_x,star_y, star_speed])

    thing_width = 5
    thing_height = 5

    blasts_List = []
    blast_width = 5
    blast_height = 15
    blastSpeed = 10

    alien_speed = 7
    alien_startx = random.randrange(0,display_width)
    alien_starty = -600
    alien_width = 150
    alien_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_sum = -5
                elif event.key == pygame.K_RIGHT:
                    x_sum = 5
                elif event.key == pygame.K_UP:
                    bullet_x = x + (widthImg / 2) - (blast_width/2)
                    bullet_y = y
                    blasts_List.append([bullet_x,bullet_y])
                else:
                    x_sum = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_sum = 0

            print(event)
        x += x_sum

        gameDisplay.fill(black)

        for bullet in blasts_List[:]:
            blast(bullet[0], bullet[1], blast_width, blast_height, red)
            bullet[1] -= blastSpeed

            if bullet[1] < 0 - blast_height:
                blasts_List.remove(bullet)

        alien(alien_startx, alien_starty)
        alien_starty += alien_speed

        #Loop for the stars on the background
        for star in stars_List:
            stars(star[0],star[1], thing_width, thing_height, white)

            star[1] += star[2]

            if star[1] > display_height:
                star[1] = 0 - thing_height
                star[0] = random.randrange(0, display_width)

        if alien_starty > display_height:
            alien_starty = 0 - alien_height
            alien_startx = random.randrange(0, display_width)
            dodged +=1

        if y < alien_starty+alien_height:
            if x > alien_startx and x < alien_startx + alien_width or x + widthImg > alien_startx and x + widthImg < alien_startx+alien_width:
                explotion(x,y)
                crash()

        spaceShip(x,y)
        things_dodged(dodged)

        if x > display_width - widthImg or x < 0:
            explotion(x,y)
            crash()

        pygame.display.update() #Updates the parameters on the method
        clock.tick(60) #fps (frames per second)

game_loop()
pygame.quit()
quit()
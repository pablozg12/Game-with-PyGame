import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("A race")
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update() #Updates the parameters on the method
    clock.tick(60) #fps (frames per second)

pygame.quit()
quit()
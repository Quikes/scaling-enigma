import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)



pixAR = pygame.PixelArray(gameDisplay)

pixAR[10][20] = green

pygame.draw.line(gameDisplay,blue, (150,200),(300,450),20)
pygame.draw.rect(gameDisplay,red,(500,200,100,200))
pygame.draw.circle(gameDisplay,green,(50,100),25)
pygame.draw.polygon(gameDisplay,white,((250,13),(225,600),(15,15),(77,15),(50,250)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
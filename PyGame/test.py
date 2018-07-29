import pygame
import time
import random
pygame.init()

display_width = 1200
display_height = 800
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
brown = (218,165,32)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Boaty Mc BoatFace')
clock=pygame.time.Clock()

boatIMG=pygame.image.load('boat.png')
boat_width=130
boat_height=173
def boat(x,y):
    gameDisplay.blit(boatIMG,(x,y))
def stones(stone_x,stone_y,stone_w,stone_h,color):
    pygame.draw.rect(gameDisplay,color,[stone_x,stone_y,stone_w,stone_h])

def score(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged:"+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def text_objects(text,font):
    textsurface = font.render(text,True, green, black)    
    return textsurface, textsurface.get_rect() 
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf', 60)
    textsurf, textrect = text_objects(text,largeText)
    textrect.center = ((display_width*0.5),(display_height*0.5))
    gameDisplay.blit(textsurf,textrect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message_display('Oops! You Crashed!')

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.5)


    stone_start_x = int(random.randrange(0,display_width))
    stone_start_y = -200
    stone_speed = 7
    stone_width = int(random.randrange(boat_width,200))
    stone_height = int(random.randrange(boat_height,200))


    GameExit = False
    KeyMap = [False,False,False,False]
    dodged=0
    while not GameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    KeyMap[0] = True
                elif event.key == pygame.K_RIGHT:
                    KeyMap[1] = True
                elif event.key == pygame.K_DOWN:
                    KeyMap[2] = True
                elif event.key == pygame.K_UP:
                    KeyMap[3] = True

            if event.type == pygame.KEYUP:
                if event.key ==pygame.K_LEFT:
                    KeyMap[0] = False
                elif event.key == pygame.K_RIGHT:
                    KeyMap[1] = False
                elif event.key == pygame.K_DOWN:
                    KeyMap[2] = False
                elif event.key == pygame.K_UP:
                    KeyMap[3] = False
            

            
        x_change=0
        y_change=0
        if KeyMap[0]: x_change+= -8
        if KeyMap[1]: x_change+= 8
        if KeyMap[2]: y_change+= 8
        if KeyMap[3]: y_change+= -8

        x+=x_change
        y+=y_change
        gameDisplay.fill(blue)

        #stones(stone_x,stone_y,stone_w,stone_h,color)
        stones(stone_start_x,stone_start_y,stone_width,stone_height,brown)
        stone_start_y +=stone_speed

        boat(x,y)
        score(dodged)


        if x > display_width - boat_width or x < 0 or y>display_height-boat_height or y < 0:
            crash()
        if y < stone_start_y+stone_height and y> stone_start_y or y+boat_height > stone_start_y and y+boat_height < stone_start_y+stone_height:
            
            if x > stone_start_x and x < stone_start_x + stone_width or x + boat_width > stone_start_x and x + boat_width < stone_start_x+stone_width:
                crash()
        pygame.display.update() #pygame.dysplay.flip()
        clock.tick(60)
        
        if stone_start_y > display_height:
            
            stone_start_y = -200
            stone_speed = random.randrange((4+dodged),(6+dodged))*((dodged+3)/3)
            stone_width = int(random.randrange(boat_width,200))
            stone_height = int(random.randrange(boat_height,200))
            stone_start_x = int(random.randrange(0,display_width))
            dodged+=1

game_loop()
pygame.quit()

quit()
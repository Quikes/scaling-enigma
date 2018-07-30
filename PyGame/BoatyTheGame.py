import pygame
import time
import random
import os

pygame.init()

display_width = 800
display_height = 800
black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
red_2 = (255,0,0)
blue = (0,0,255)
green = (0,150,0)
green_2 = (0 ,255, 0)
brown = (218,165,32)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Boaty Mc BoatFace')
clock=pygame.time.Clock() 
#boatIMG= pygame.image.load(os.path.join(os.getcwd(),'boaty.png')).conve‌​rt()


pause = False
crash = False

boatIMG=pygame.transform.scale(pygame.image.load('boaty.png'),(60,80))
boatIMG2=pygame.transform.scale(pygame.image.load('boaty.png'),(250,300))
boat_width=60
boat_height=80
def QQuit():
    pygame.quit
    quit()
def boat(x,y):
    gameDisplay.blit(boatIMG,(x,y))
def stones(stone_x,stone_y,stone_w,stone_h,color):
    pygame.draw.rect(gameDisplay,color,[stone_x,stone_y,stone_w,stone_h])

def score(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged:"+str(count),True,white)
    gameDisplay.blit(text,(0,0))
def rectan_button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        #print(mouse)
    a = (x+w > mouse[0] and x < mouse[0] and y+h>mouse[1] and y < mouse[1])
    if a: 
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        
        if click[0]==1 and action!=None:
            action()
        
            
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
        
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect = text_objects(msg,smallText,black)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textsurf,textrect)



def text_objects(text,font,color):
    textsurface = font.render(text,True, color, None)    
    return textsurface, textsurface.get_rect() 
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf', 60)
    textsurf, textrect = text_objects(text,largeText,green)
    textrect.center = ((display_width*0.5),(display_height*0.4))
    gameDisplay.blit(textsurf,textrect)

    pygame.display.update()
    time.sleep(2)

    game_intro()

def crashed():
    #message_display('Oops! You Crashed!')
    crash = True
    while crash :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText=pygame.font.Font('freesansbold.ttf', 60)
        textsurf, textrect = text_objects('Oops! You crashed!',largeText,red)
        textrect.center = ((display_width*0.5),(display_height*0.5))
        gameDisplay.blit(textsurf,textrect)
        rectan_button('Play Again',150,550,200,100,green,green_2,game_loop)
        rectan_button('Back to Menu',450,550,200,100,red,red_2,game_intro)
        time.sleep(0.005)
        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)
        largeText=pygame.font.Font('freesansbold.ttf', 60)
        textsurf, textrect = text_objects('Boaty Mc BoatFace',largeText,red)
        textrect.center = ((display_width*0.5),(display_height*0.5))
        gameDisplay.blit(textsurf,textrect)
       
        gameDisplay.blit(boatIMG2,(display_width*0.4,display_height*(0.05)))
        rectan_button('Start',250,450,300,100,green,green_2,game_loop)
        rectan_button('X',700,50,30,30,red,red_2,QQuit)
        
       

        pygame.display.update()
        clock.tick(15)
def unpause():
    global pause
    pause = False
def paused():
    
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        
        largeText=pygame.font.Font('freesansbold.ttf', 30)
        textsurf, textrect = text_objects('Game Paused',largeText,red)
        textrect.center = ((display_width*0.5),(display_height*0.5))
        gameDisplay.blit(textsurf,textrect)
        
        rectan_button('Continue',250,450,300,100,green,green_2,unpause)
        rectan_button('X',700,50,30,30,red,red_2,QQuit)
        
            

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    global crash



    x = (display_width * 0.45)
    y = (display_height * 0.5)


    stone_start_x = int(random.randrange(0,display_width))
    stone_start_y = -200
    stone_speed = 7
    stone_width = int(random.randrange(boat_width,200))
    stone_height = int(random.randrange(boat_height,200))


    GameExit = False
    KeyMap = [False,False,False,False,False]
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
                elif event.key == pygame.K_p:
                    pause = True
                    paused()


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
        
           
            
        gameDisplay.fill(blue)

        x+=x_change
        y+=y_change
        

        #stones(stone_x,stone_y,stone_w,stone_h,color)
        stones(stone_start_x,stone_start_y,stone_width,stone_height,brown)
        stone_start_y +=stone_speed

        
        largeText=pygame.font.Font('freesansbold.ttf', 20)
        textsurf, textrect = text_objects('Press "p" to pause.',largeText,white)
        textrect.center = ((display_width*0.85),(display_height*0.03))
        gameDisplay.blit(textsurf,textrect) 
        boat(x,y)


        score(dodged)


        if x > display_width - boat_width or x < 0 or y>display_height-boat_height or y < 0:
            crashed()
        if y < stone_start_y+stone_height and y> stone_start_y or y+boat_height > stone_start_y and y+boat_height < stone_start_y+stone_height:
            
            if x > stone_start_x and x < stone_start_x + stone_width or x + boat_width > stone_start_x and x + boat_width < stone_start_x+stone_width:
                crash=True
                crashed()
        pygame.display.update() #pygame.dysplay.flip()
        clock.tick(60)
        
        if stone_start_y > display_height:
            
            stone_start_y = -200
            stone_speed = min(random.randrange(5,7)*((dodged+3)/5),12)
            stone_width = int(random.randrange(boat_width*2,200+(dodged*2)))
            stone_height = int(random.randrange(boat_height*2,300+(dodged*3)))
            stone_start_x = int(random.randrange(0,display_width))
            dodged+=1
game_intro()
game_loop()
pygame.quit()

quit()
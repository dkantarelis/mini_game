import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 1000



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dodge THIS!")


black = (0, 0, 0)
grey = (30, 30, 30)
white = (255, 255, 255)
red = (255, 0, 0)

total_score = 0

clock = pygame.time.Clock()
crashed = False
#--------IMAGES-------#
carIMG = pygame.image.load('RaceCar.png')
YellowCIMG = pygame.image.load('YellowCar.png')
GreenCIMG = pygame.image.load('GreenCar.png')
oilIMG = pygame.image.load('oil.png')
treeIMG = pygame.image.load('tree.png')
treeIMG = pygame.image.load('tree.png')
background_IMG = pygame.image.load('background2.png').convert()
Intro_IMG = pygame.image.load('intro_screen.png').convert()
road_fxs = pygame.image.load('road_paint.png')
road_fxs2 = pygame.image.load('road_yellow_paint.png')
#--------ICON---------#
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#-------SOUND---------#
crash_sound = pygame.mixer.Sound('Crash_Sound.ogg')
oil_sound = pygame.mixer.Sound('Tires_Squealing.ogg')
menu_sound = pygame.mixer.Sound('main_menu.ogg')
car_sound = pygame.mixer.Sound('car_sound.ogg')




def Score(count,x,y,megethos):
    font = pygame.font.SysFont(None, megethos)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(x,y))

def End_Score(s):
    score=0    
    score += s
    return score    

def text_objects(txt,font):
    textSurface = font.render(txt, True, red)
    return textSurface,textSurface.get_rect()

def roadFXs1(rx1, ry1):
    gameDisplay.blit(road_fxs, (rx1, ry1))
def roadFXs2(rx2, ry2):
    gameDisplay.blit(road_fxs, (rx2, ry2))
def roadFXs3(rx3, ry3):
    gameDisplay.blit(road_fxs2, (rx3, ry3))
def roadFXs4(rx4, ry4):
    gameDisplay.blit(road_fxs2, (rx4, ry4))
    
def crash(sc):
    car_sound.stop()
    crash_sound.play()
    retry(sc)

def car(x, y):
    gameDisplay.blit(carIMG, (x, y))

def YCar(ycarx, ycary):
    gameDisplay.blit(YellowCIMG, (ycarx, ycary))

def Gcar(gcarx, gcary):
    gameDisplay.blit(GreenCIMG, (gcarx, gcary))
    
def Oil(oilx,oily):
    gameDisplay.blit(oilIMG,(oilx, oily))

def Tree(treex,treey):
    gameDisplay.blit(treeIMG, (treex, treey))
    
def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah

def retry(sc):
    retry = True
    d_width = 1000
    d_height = 750
    
    gameDisplay = pygame.display.set_mode((d_width, d_height))
    while retry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(white)
        text = pygame.font.Font('freesansbold.ttf',78)
        textSurf, textRect = text_objects("Crashed!",text)
        textRect.center =((display_width/2),(display_height/4))
        gameDisplay.blit(textSurf,textRect)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 150+200 > mouse[0] > 150 and 500+100 > mouse[1]>500:
            pygame.draw.rect(gameDisplay, grey,(150,500,200,100))
            if click[0]==1:
                gameLoop()
        else:
            pygame.draw.rect(gameDisplay, black,(150,500,200,100))
        if 650+200 > mouse[0] > 650 and 500+100 > mouse[1]>500:  
            pygame.draw.rect(gameDisplay, grey,(650,500,200,100))
            if click[0]==1:
                pygame.quit()
        else:
            pygame.draw.rect(gameDisplay, black,(650,500,200,100))
         
        itxt = pygame.font.Font('freesansbold.ttf',45)
        textSurf, textRect = text_objects('Retry',itxt)
        textRect.center = ((150+(200/2)),(500+(100/2)))
        gameDisplay.blit(textSurf, textRect)
        
        itxt1 = pygame.font.Font('freesansbold.ttf',45)
        textSurf, textRect = text_objects('Quit',itxt1)
        textRect.center = ((650+(200/2)),(500+(100/2)))
        gameDisplay.blit(textSurf, textRect)
        
        Score(End_Score(sc),450,d_height/2,45)
        
        pygame.display.update()
        clock.tick(15)

def intro():
    intro = True
    menu_sound.play(2)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(white)
        gameDisplay.blit(Intro_IMG,(0,0))
        text = pygame.font.Font('freesansbold.ttf',64)
        textSurf, textRect = text_objects("Dodge THIS!",text)
        textRect.center =((display_width/2),(display_height/4))
        gameDisplay.blit(textSurf,textRect)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 150+200 > mouse[0] > 150 and 750+100 > mouse[1]>750:
            pygame.draw.rect(gameDisplay, grey,(150,750,200,100))
            if click[0]==1:
                gameLoop()
        else:
            pygame.draw.rect(gameDisplay, black,(150,750,200,100))
        if 650+200 > mouse[0] > 650 and 750+100 > mouse[1]>750:  
            pygame.draw.rect(gameDisplay, grey,(650,750,200,100))
            if click[0]==1:
                pygame.quit()
        else:
            pygame.draw.rect(gameDisplay, black,(650,750,200,100))
         
        itxt = pygame.font.Font('freesansbold.ttf',45)
        textSurf, textRect = text_objects('Start',itxt)
        textRect.center = ((150+(200/2)),(750+(100/2)))
        gameDisplay.blit(textSurf, textRect)
        
        itxt1 = pygame.font.Font('freesansbold.ttf',45)
        textSurf, textRect = text_objects('Quit',itxt1)
        textRect.center = ((650+(200/2)),(750+(100/2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)
        
    
def gameLoop():
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    FPS=30
    x = (display_width * 0.45)
    y = (display_height * 0.7)
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    crashed = False
    yCar_startx = random.randrange(0, display_width-129)
    yCar_starty = -300
    yCar_speed = 10
    gCar_startx = random.randrange(0, display_width-129)
    gCar_starty = -300
    gCar_speed = 13
    oil_startx = random.randrange(164, display_width-150)
    oil_starty = -500    
    oil_speed = 5
    yoil = 13
    score=0
    
    #-------EFECTS--------#
    tree_startx = 48
    tree_starty = -100
    tree_speed = 70
    
    road_startx = 345
    road_starty = 0
    roadfxs_speed = 200
    
    road_startx1 = 654
    road_starty1 = 0
    roadfxs_speed1 = 200
    
    road_startx2 = 190
    road_starty2 = 0
    roadfxs_speed2 = 200
    
    road_startx3 = 814
    road_starty3 = 0
    roadfxs_speed3 = 200
    #-------EFECTS--------# 
    lvl = 0
    
    menu_sound.stop()
    car_sound.play(10)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x1 = 0
                    
                if event.key == pygame.K_RIGHT:
                    x2 = 0
                    
                if event.key == pygame.K_UP:
                    y1 = 0
                if event.key == pygame.K_DOWN:
                    y2 = 0
                if event.key == pygame.K_SPACE:
                   y1 = 0
                   x1 = 0
                   x2 = 0
                   y2 = 0 
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 = -5                
                if event.key == pygame.K_RIGHT:
                    x2 = 5
                if event.key == pygame.K_UP:
                    y1 = -5
                if event.key == pygame.K_DOWN:
                    y2 = 5
                if event.key == pygame.K_SPACE:
                    y2 = 9 
     
        x += x1 + x2
        y += y1 + y2
        
        gameDisplay.blit(background_IMG,(0,0))
        roadFXs1(road_startx, road_starty)
        road_starty += roadfxs_speed      
        roadFXs2(road_startx1, road_starty1)
        road_starty1 += roadfxs_speed1
        roadFXs3(road_startx2, road_starty2)
        road_starty2 += roadfxs_speed2
        roadFXs4(road_startx3, road_starty3)
        road_starty3 += roadfxs_speed3
        
        car(x,y)
        Tree(tree_startx,tree_starty)        
        tree_starty += tree_speed         
         
        YCar(yCar_startx,yCar_starty)        
        yCar_starty += yCar_speed
        
        Oil(oil_startx,oil_starty)
        oil_starty += oil_speed      
        
        Score(score,1,1,25)
        
        if x > display_width-127 or x < 0:
            crash()
        
        if road_starty > display_height:
            road_starty = 0
            road_startx = 345
        if road_starty1 > display_height:
            road_starty1 = 0
            road_startx1 = 654
        if road_starty2 > display_height:
            road_starty2 = 0
            road_startx2 = 190
        if road_starty3 > display_height:
            road_starty3 = 0
            road_startx3 = 814
        
        if yCar_starty > display_height:
            yCar_starty = -150
            yCar_startx = random.randrange(0, display_width-129)
            lvl += 1
            score += 1
            End_Score(score)
            
        if gCar_starty > display_height:
            gCar_starty = -150
            gCar_startx = random.randrange(0, display_width-129)
            lvl += 1
            score += 1
            End_Score(score)
            
        if oil_starty > display_height:
            oil_starty = -20
            oil_startx = random.randrange(0, display_width-150)
            
        if tree_starty > display_height:
            tree_starty = -150
            tree_pos = random.randrange(1, 100)
            if tree_pos > 50:
                tree_startx = 48
            if tree_pos < 50:
                tree_startx = 875
            
            
        #collision(x, y, car_width, car_height, thing_startx, thing_starty, thing_width, thing_height)
        if collision(x, y, 126, 258, yCar_startx, yCar_starty, 128, 258):
            crash(score)
            
        if collision(x, y, 126, 258, gCar_startx, gCar_starty, 128, 258):
            crash(score)

        if collision(x, y, 126, 258, oil_startx, oil_starty, 150, 115):
            x += yoil
            oil_sound.play()
            
        if collision(yCar_startx, yCar_starty, 126, 259, oil_startx, oil_starty, 150, 115):
            yCar_startx += yoil
            oil_sound.play()
            
        if collision(gCar_startx, gCar_starty, 126, 259, oil_startx, oil_starty, 150, 115):
            gCar_startx -= yoil
            oil_sound.play()
        
        if collision(x, y, 126, 258, tree_startx, tree_starty, 99, 180):
            crash(score)           
            
        if lvl>=5:
            yCar_speed += 2
            gCar_speed += 2
            lvl -= 5
            
        if score >=10:
            Gcar(gCar_startx,gCar_starty)
            gCar_starty += gCar_speed
        
        
        pygame.display.update()
        clock.tick(FPS)

intro()
pygame.quit()

#message_code
#def message(mes):
    #text = pygame.font.Font('freesansbold.ttf',64)
    #textSurf, textRect = text_objects(mes,text)
    #textRect.center =((display_width/2),(display_height/2))
    #gameDisplay.blit(textSurf,textRect)
    
    #pygame.display.update()
    
    #time.sleep(2)
    #gameLoop()

    
    
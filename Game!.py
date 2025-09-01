# menu.py

from pygame import *
from random import *
import pygame
pygame.init()
init()
GREEN=0,255,0



#########################
wid=1000
height=700
screen = display.set_mode((wid, height))
running = True
x,y = 0,0
OUTLINE = (150,50,30)

        
#Loading all the images needed for the game
runPics=[image.load("pics/Run" + str(i) + ".png") for i in range(12)]
idlePics=[image.load("pics/Idle" + str(i) + ".png") for i in range(10)]
jumpPics=[image.load("pics/Jump" + str(i) + ".png") for i in range(3)]
enemyPics=[image.load("pics/Enemy" + str(i) + ".png") for i in range(12)]
coinPics=[image.load("pics/Coin" + str(i) + ".png") for i in range(4)]
doorPics=[image.load("pics/Door" + str(i) + ".png") for i in range(2)]
healthPics=[image.load("pics/Health" + str(i) + ".png") for i in range(3)]
treasurePic=image.load("pics/Treasure0.png") #2440x210
winPic=image.load("pics/winScreen.png") #2440x210
menuPics=[image.load("pics/menu" + str(i) + ".png") for i in range(2)]
overPic=image.load("pics/Dead.png") #2440x210
instructPic=image.load("pics/Instructions.png")
backMainPic=image.load("pics/backMain.png")
backPic=image.load("pics/untitled.png") #2440x210
backPic2=image.load("pics/2bg.png")
BLACK=(0,0,0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GROUND = height

jumpSpeed = -25 #how fast the player jumps up
gravity = 1.5 #how fast they fall down 
bottom = GROUND

X=0
Y=1
W=2
H=3
BOT=2
SCREENX=3

  #X #Y BOT
v=[0,0,bottom,200]

lives=3

p=Rect(200,190,40,20) #the player

#Defining the location of the platforms in level 1 and 2         
plats=[Rect(60,450,390,20),Rect(512,322,60,20),Rect(640,195,190,20),Rect(900,195,120,20),Rect(1090,195,190,20),Rect(510,575,835,20),Rect(1475,515,380,20),Rect(1600,260,60,20),Rect(2055,450,180,20),Rect(2435,450,320,20),Rect(2810,325,70,20),Rect(2940,260,70,20),Rect(2945,515,55,20),Rect(3135,195,195,20),Rect(3525,195,60,20),Rect(3265,580,55,20),Rect(3520,515,320,20)]

plats2=[Rect(60,450,330,20),Rect(513,390,70,20),Rect(770,390,195,20),Rect(1090,515,195,20),Rect(1408,450,70,20),Rect(1600,390,70,20),Rect(1725,325,70,20),Rect(1990,325,440,20),Rect(2620,450,70,20),Rect(2820,520,195,20),Rect(3140,450,195,20),Rect(3400,320,330,20)]
        


eV=[1.5,0.6,3,2,0.5,3,2] #enemy speeds in lvl 1
eV2=[1.5,0.6,3,2,0.5,3,2] #^^ lvl2


timerStart=False
invinc=False

def imm():
    global timerStart
    global invinc
    global t
    for e in enemies1:
        enemy=Rect(e[0],e[1],e[2],e[3])
        
        if p.colliderect(enemy): #if you collide with the enemy, make the player invincible
            invinc=True
            t=0
            timerStart=True     #start the timer for the invincibility duration

        if timerStart:
            t+=1
            if t>180: #player can be hit after t>180
                invinc=False

    #invincibility for the player in level two     
    for f in enemies2:
        enemy2=Rect(f[0],f[1],f[2],f[3]) 
                
        if p.colliderect(enemy2):
            invinc=True
            t=0
            timerStart=True

        if timerStart:
            t+=1
            if t>180:
                invinc=False


eImg=[True for i in range(7)] #whether to show the left aninations or the right animations for the enemey
eImg2=[True for i in range(5)]

enemyFrame=0 
enemyFrame2=0
eBorders=[[900,512],[1000,910],[1250,1000],[1850,1480],[2220,2050],[2730,2440],[3310,3130]] #if the enemies hit these points, they move the opposite direction
eBorders2=[[932,732],[1259,1051],[2395,1972],[2972,2813],[3285,3128]]
def enemies():
   # global ev
#    global eImg
   # global enemies1

    
    if page=="lev1":
        if enemies1[0][0]>=eBorders[0][0] or enemies1[0][0]<=eBorders[0][1]:
            eV[0]=-eV[0] #if the enemies hit their borders, they move the opposite direction
            eImg[0]= not eImg[0] #setting the eImg variable to the opposite boolean condition. (True= right enemy images, False = left enemy images)
                    #not eImg is code from stackoverflow
        
        enemies1[0][0]+=eV[0]#increase x pos by enemy speed
        

        if enemies1[1][0]>=eBorders[1][0] or enemies1[1][0]<=eBorders[1][1]:
            eV[1]=-eV[1]
            eImg[1]= not eImg[1]
        enemies1[1][0]+=eV[1]

        if enemies1[2][0]>=eBorders[2][0] or enemies1[2][0]<=eBorders[2][1]:
            eV[2]=-eV[2]
            eImg[2]= not eImg[2]
        enemies1[2][0]+=eV[2]

        if enemies1[3][0]>=eBorders[3][0] or enemies1[3][0]<=eBorders[3][1]:
            eV[3]=-eV[3]
            eImg[3]= not eImg[3]
        enemies1[3][0]+=eV[3]
        
        if enemies1[4][0]>=eBorders[4][0] or enemies1[4][0]<=eBorders[4][1]:
            eV[4]=-eV[4]
            eImg[4]= not eImg[4]
        enemies1[4][0]+=eV[4]

        if enemies1[5][0]>=eBorders[5][0] or enemies1[5][0]<=eBorders[5][1]:
            eV[5]=-eV[5]
            eImg[5]= not eImg[5]
        enemies1[5][0]+=eV[5]
        
        if enemies1[6][0]>eBorders[6][0] or enemies1[6][0]<eBorders[6][1]:
            eV[6]=-eV[6]
            eImg[6]= not eImg[6]
        enemies1[6][0]+=eV[6]
        
      #same enemy mechanics except for level two
    elif page=="lev2":
        if enemies2[0][0]>=eBorders2[0][0] or enemies2[0][0]<=eBorders2[0][1]:
            eV2[0]=-eV2[0]
            eImg2[0]= not eImg2[0]
        
        enemies2[0][0]+=eV2[0]
        
        if enemies2[1][0]>=eBorders2[1][0] or enemies2[1][0]<=eBorders2[1][1]:
            eV2[1]=-eV2[1]
            eImg2[1]= not eImg2[1]
        enemies2[1][0]+=eV2[1]


        if enemies2[2][0]>=eBorders2[2][0] or enemies2[2][0]<=eBorders2[2][1]:
            eV2[3]=-eV2[3]
            eImg2[2]= not eImg2[2]
        enemies2[2][0]+=eV2[3]
        
        if enemies2[3][0]>=eBorders2[3][0] or enemies2[3][0]<=eBorders2[3][1]:
            eV2[4]=-eV2[4]
            eImg2[3]= not eImg2[3]
        enemies2[3][0]+=eV2[4]

        if enemies2[4][0]>=eBorders2[4][0] or enemies2[4][0]<=eBorders2[4][1]:
            eV2[5]=-eV2[5]
            eImg2[4]= not eImg2[4]
        enemies2[4][0]+=eV2[5]
        
def restart():
#resets all important values to the original values if the player goes back to main menu or restarts
    global p
    global coins1
    global coinCount
    global lives
    global v
    for e in enemies1:
        e[4]=1
    for f in enemies2:
        f[4]=1
    
    p=Rect(200,190,40,40)
    v=[0,0,bottom,200]
    lives=3
    coinCount=0
  
    coins1=[[935,525,20,20,1],[1180,145,20,20,1],[2140,400,20,20,1],[3290,530,20,20,1],[3540,145,20,20,1]]
    





    
def checkLives():
  #  global lives
    if lives<=0:
        return "gameOver" #show "game over" when the player dies
        running=False
    

def hitBox():
    if d:
        pCol=Rect(p[X],p[Y]+40,40,5) #used to kill the enemies
    elif a:
        pCol=Rect(p[X]+30,p[Y]+40,40,5) #if the player looks left, add 30 to his bottom hitbox so it is under him, not infront of him
    collision=True
    offset=v[SCREENX]-p[X] #so the entities stay in one spot as the screen moves
    global lives 
    global coinCount
    if page=="lev1":
        for e in enemies1:
            enemy=Rect(e[0],e[1],e[2],e[3])
            if p.colliderect(enemy) and invinc == False and pCol.colliderect(enemy)==False and e[4]!=0: #if the player gets hit while invicibility is FALSE and the player isn't jumping on the enemy
               lives-=1
               checkLives()
            #enemy killling
            if pCol.colliderect(enemy):
                e[4]=0 #making the enemy dissapear

    elif page=="lev2":
        #same logic but for level 2
        for f in enemies2:
            enemy2=Rect(f[0],f[1],f[2],f[3])
            if p.colliderect(enemy2) and invinc == False and pCol.colliderect(enemy2)==False and f[4]!=0:
               lives-=1
               checkLives()
            #enemy kill
            if pCol.colliderect(enemy2):
                f[4]=0


    for c in coins1:
        coins=Rect(c[0],c[1],c[2],c[3])
        if p.colliderect(coins) and c[4]!=0: #if the player touches a coin and it hasn't already been touched yet
           coinCount+=1
           c[4]=0



        
enemies1=[[727,520,40,40,1],[943,150,40,40,1],[1113,530,40,40,1],[1643,470,40,40,1],[2138,407,40,40,1],[2583,407,40,40,1],[3223,152,40,40,1]] #enemy positions lvl 1
enemies2=[[884,350,40,40,1],[1180,475,40,40,1],[2156,285,40,40,1],[2889,480,40,40,1],[3204,410,40,40,1]] #lvl 2


coins1=[[935,525,20,20,1],[1180,145,20,20,1],[2140,400,20,20,1],[3290,530,20,20,1],[3540,145,20,20,1]] #coin positions in level 1

    
coinCount=0
coinFrame=0

def drawScene(screen,p,plats):
##    global eV
## #  global coins
    global enemyFrame
    global enemyFrame2
##    global enemies1
    global coinFrame
##    global facing
    offset=v[SCREENX]-p[X]
    if page=="lev1":
        screen.blit(backPic,(offset,0)) #blits the background
        #blits the hearts on the top left based on the damage taken
        if lives==3:
            screen.blit(healthPics[0],(0,0))
        elif lives==2:
            screen.blit(healthPics[1],(0,0))

        elif lives==1:
            screen.blit(healthPics[2],(0,0))    


            
        for e in enemies1:
            enemy=Rect(e[0],e[1],e[2],e[3]).move(offset,0)
            for i in range(7):
                if enemies1[i][4]==1: #only show if the player hasn't killed the enemy
                    if eImg[i]==True: #show the right moving images
                            screen.blit(enemyPics[6:12][int(enemyFrame)],(enemies1[i][0]+offset-7,enemies1[i][1]+3))#"blit" one frame at a time
                            enemyFrame += 0.003 
                            if enemyFrame >= 4: #if the enemy animation frames have fully cycled, restart them.
                                enemyFrame = 0              
                    else:
                        #show the left moving images
                            screen.blit(enemyPics[0:6][int(enemyFrame2)],(enemies1[i][0]+offset-7,enemies1[i][1]+3))#"blit" one frame at a time
                            enemyFrame2 += 0.003 
                            if enemyFrame2 >= 4:
                                enemyFrame2 = 0
            
            #coins
        for c in coins1:
            coins=Rect(c[0],c[1],c[2],c[3]).move(offset,0)
            for i in range(5):
                if  coins1[i][4]==1: #only show if the player hasn't collected the coin
                    screen.blit(coinPics[int(coinFrame)],(coins1[i][0]+offset-5,coins1[i][1]-10))#"blit" one frame at a time                   
                    coinFrame += 0.005 
                    if coinFrame >= 4:
                        coinFrame = 0        
                                    
            #door
            for i in door:
                i=i.move(offset,0)
            
                if coinCount==5: #if the player collects all the coins needed to pass level 1
                    screen.blit(doorPics[0],(3510+offset,360,100,180)) #show open door
                else:
                    screen.blit(doorPics[1],(3510+offset,310,100,180)) #shows closed door
            
    #same logic as level 1            
    elif page=="lev2":
        screen.blit(backPic2,(offset,0))

        if lives==3:
            screen.blit(healthPics[0],(0,0))
        elif lives==2:
            screen.blit(healthPics[1],(0,0))

        elif lives==1:
            screen.blit(healthPics[2],(0,0))
            

        for f in enemies2:
            enemy2=Rect(f[0],f[1],f[2],f[3]).move(offset,0)
            for i in range(5):
                if enemies2[i][4]==1:
    
                    if eImg2[i]==True:
                            screen.blit(enemyPics[6:12][int(enemyFrame)],(enemies2[i][0]+offset-7,enemies2[i][1]+3))#"blit" one frame at a time
                            enemyFrame += 0.003 
                            if enemyFrame >= 4:
                                enemyFrame = 0              
                    else:
                            screen.blit(enemyPics[0:6][int(enemyFrame2)],(enemies2[i][0]+offset-7,enemies2[i][1]+3))#"blit" one frame at a time
                            enemyFrame2 += 0.003 
                            if enemyFrame2 >= 4:
                                enemyFrame2 = 0

##            for t in treasure:
##                t=t.move(offset,0)
##                draw.rect(screen,RED,t)
            screen.blit(treasurePic,(3500+offset,230))
                



  #  display.flip()
   
    
    
    
door=[Rect(3510,340,200,180)]
treasure=[Rect(3520,230,300,80)]


runFrame=0
runFrame2=0
jumpFrame=0
idleFrame=0

#what key is currently being pressed
d=True
a=False



facing="right"  
def move(p):
    global runFrame
    global runFrame2
    global jumpFrame
    global idleFrame
    global facing
    global a,d
    offset=v[SCREENX]-p[X]

    #global v
    keys = key.get_pressed()


    if keys[K_SPACE] and p[Y] + p[H] == v[BOT] and v[Y] == 0:    
        v[Y] = jumpSpeed           # player must be sitting steady on a platform or the ground in order to jump
        screen.blit(jumpPics[int(jumpFrame)],(v[SCREENX],p[1]-10))#"blit" one frame at a time
        jumpFrame += 0.1 #0.1.......0.9
        if jumpFrame >= 3:
            jumpFrame = 0

        
    if keys[K_a] and p[X]>200:
        facing="left"
        v[X] = -8.5
        screen.blit(runPics[6:12][int(runFrame2)],(v[SCREENX],p[1]-10))
        runFrame2 += 0.1 #0.1.......0.9
        pBot=Rect(p[X]+30+offset,p[Y]+40,40,5)
        d=False #changes to false as "a" key is being pressed
        a=True
     
        
        if runFrame2 >= 6:
            runFrame2 = 0


        if v[SCREENX] > 200:
            v[SCREENX] -= 1.2
    elif keys[K_d] and p[X]<3550:
        facing="right"
        v[X] = 8.5
        screen.blit(runPics[0:6][int(runFrame)],(v[SCREENX],p[1]-10))#"blit" one frame at a time
        runFrame += 0.1 #0.1.......0.9
        pBot=Rect(p[X]+offset,p[Y]+40,40,5)
        d=True
        a=False #changes to false as "d" key is being pressed
    
        if runFrame >= 6:
            runFrame = 0
        if v[SCREENX] <900:
            v[SCREENX] +=1.2 #move the screen if the player is about the reach the end of it

             
    else:
        v[X] = 0
        if facing=="right": #which facing animations the code should blit for the IDLE animation
            screen.blit(idlePics[0:4][int(idleFrame)],(v[SCREENX],p[1]-10))#"blit" right images
        else:
            screen.blit(idlePics[5:10][int(idleFrame)],(v[SCREENX],p[1]-10))#"blit" left images
                
        idleFrame += 0.1 
        if idleFrame >= 4:
            idleFrame = 0
    
  
    p[X] += v[X]
    v[Y] += gravity

  

def check(p,plats):
    global lives
    if page=="lev1":
        for plat in plats:
            if p[X]+p[W]>plat[X] and p[X]<plat[X]+plat[W] and p[Y]+p[H]<=plat[Y] and p[Y]+p[H]+v[Y]>plat[Y]:
                # if player is horizontally within the platform ends, and if it is going to cross the plat (after moving):
                v[BOT] = plat[Y]
                p[Y] = v[BOT] - p[H]
                v[Y] =0
                
    elif page=="lev2":
        for plat in plats2:
            if p[X]+p[W]>plat[X] and p[X]<plat[X]+plat[W] and p[Y]+p[H]<=plat[Y] and p[Y]+p[H]+v[Y]>plat[Y]:
                # if player is horizontally within the platform ends, and if it is going to cross the plat (after moving):
                v[BOT] = plat[Y]
                p[Y] = v[BOT] - p[H]
                v[Y] =0
                
        
    p[Y] += v[Y]
    if p[Y]+p[H] >= GROUND:# if player attempts to fall below the ground
        v[BOT] = GROUND
        p[Y] = GROUND - p[H]
        v[Y] = 0
    
    if p[Y] >600:# if player falls into the water
        lives=0

        checkLives()




def instructions(): #what to do when instruction button is pressed
    running = True
    screen.blit(instructPic,(0,-80)) #blits the instruction picture
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        back=Rect(775,0,250,50)
        screen.blit(backMainPic,(775,0))
   
        display.flip()

        if mb[0]==1:
            if back.collidepoint(mx,my): #if the mouse collides with these buttons
                running = False
    return "menu"

        



lvl2=False
def level1():#what to do when level 1  button is pressed
    global lvl2
    running=True
    while running:#game loop for level 1
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
        #displays/runs all the game code for level 1
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        drawScene(screen,p,plats)
        move(p)
        enemies()
        check(p,plats)
        hitBox()
        imm()
        

        if p.colliderect(door[0]) and coinCount==5: #only allow the player to pass to level 2 if they collected all the coins
            lvl2=True
            running=False
        if lives<=0:
            running=False
            return "gameOver" #shows game over if the player loses all of his lives
        
        back=Rect(775,0,250,50) 
        screen.blit(backMainPic,(775,0))
   
        display.flip()

        if mb[0]==1:
            if back.collidepoint(mx,my): #if the mouse collides with these buttons
                running = False
    return "menu"

    

def level2():
    global lvl2
    running=True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
        #displays/runs all the game code for level 2
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        drawScene(screen,p,plats)
        move(p)
        check(p,plats)
        enemies()
        hitBox()
        imm()
        if p.colliderect(treasure[0]):
            #shows the win screen if the player reaches the end
            running=False
            return "winScreen"
        #shows game over if the player loses all of his lives
        if lives<=0:
            running=False
            return "gameOver"

        back=Rect(775,0,250,50)
        screen.blit(backMainPic,(775,0))
   
        display.flip()

        if mb[0]==1:
            if back.collidepoint(mx,my): #if the mouse collides with these buttons
                running = False
    return "menu"



def winScreen(): #displays the win screen
    running=True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
        screen.fill(0)
        screen.blit(winPic,(0,-100))
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
   
    
        back=Rect(775,0,250,50)
        screen.blit(backMainPic,(775,0))
   
        display.flip()

        if mb[0]==1:
            if back.collidepoint(mx,my): #if the mouse collides with these buttons
                running = False
    return "menu"

 
def gameOver(): #displays the game over screen
    running=True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
                
        screen.fill(0)
        
        screen.blit(overPic,(0,-200))
        back=Rect(775,0,250,50)
        screen.blit(backMainPic,(775,0))
   
        display.flip()

        if mb[0]==1:
            if back.collidepoint(mx,my): #if the mouse collides with these buttons
                running = False
    return "menu"


def menu():
    running = True
    myClock = time.Clock()
    buttons=[Rect(20,125,408,90),Rect(20,415,408,90),Rect(270,600,550,60)]#creating the buttons
    while running:

        for evnt in event.get():            
            if evnt.type == QUIT:
                return "exit"
        if lvl2==False:
            screen.blit(menuPics[0],(0,-100)) #if the player hasn't passed level 1, display an image where level 2 button is greyed out
        else:
            screen.blit(menuPics[1],(0,-100)) #same picture, but level 2 button now has color. (AFTER COMPLETING LEVEL 1)
            
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

  
        if mb[0]==1:
            if buttons[0].collidepoint(mx,my): #if the mouse collides with these buttons
                return "lev1"
            if buttons[1].collidepoint(mx,my) and lvl2==True:
                return "lev2"
            if buttons[2].collidepoint(mx,my):
                return "instructions"
            if p.colliderect(door[0]):
                return "lev2"
                       
        display.flip()

        myClock.tick(60)


# This is the important part of the example.
# The idea is we have a variable (page) that keeps
# track of which page we are one. We give control
# of the program to a function until it is done and
# the program returns the new page it should be on.




page = "menu"
while page != "exit":
    if page == "menu":
        restart()
        v=[0,0,bottom,200]
        page = menu()
    if page == "lev1":
        page = level1()
    if page == "lev2":
        page = level2() 
    if page == "instructions":
        page = instructions()    
    if page == "story":
        page = story()
    if page == "winScreen":
        page = winScreen()
    if page == "gameOver":
        page = gameOver()
  
  
quit()

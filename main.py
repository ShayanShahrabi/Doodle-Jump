import pygame
from pygame.locals import*
import sys
import random
#-----------------------------------------------------------------------------
pygame.init()
w=pygame.display.set_mode((400,650))
t=pygame.time.Clock()
keys=pygame.key.get_pressed()
#-----------------------------------------------------------------------------
platform = pygame.image.load('./resources/platform.png')
doodleImg = pygame.image.load('./resources/doodle.png')
doodleImgleft = pygame.image.load('./resources/doodle_left.png')
#-----------------------------------------------------------------------------
font = pygame.font.SysFont('Comic sans MS', 20)
start_text = font.render('PRESS ENTER TO START!', True, (0, 0, 0))

restart=font.render('PRESS ENTER TO RESTART GAME!', True, (0, 0, 0))
exitgame=font.render('PRESS ESCAPE TO QUIT GAME!', True, (0, 0, 0))
doodleImg = pygame.transform.scale(doodleImg, (70, 70))
doodleImgleft = pygame.transform.scale(doodleImgleft, (70, 70))
platform = pygame.transform.scale(platform, (50, 10))
gameover = False
score = 0
high_score = 0
speed =- 300
j = 0
q = 0
e = 0
d = 0
s = 0
f = 0
game_status = "start"
b = 0
x1 = 50
x2 = 300
x3 = 175
y1 = 400
y2 = 275
y3=75
x=x1
y=200
l=1
#-----------------------------------------------------------------------------
def Start():
    global y,x, b, w
    w.blit(platform,(x1,y1))
    w.blit(platform,(x2,y2))
    w.blit(platform,(x3,y3))
    w.blit( doodleImg, ( x,y ) )
    if y<400 and b==0:
        y=y+1
    if y==400-50:
        b=1
    if b==1:
        y=y-1
    if y==100:
        b=0    
#-----------------------------------------------------------------------------
def maned(xx,yy):
    global x,y,speed    
    for i in range(0,50):
        if x==xx+i and y+60==yy:
            speed=250
            return True
        if x+50==xx+i and y+60==yy:
            speed=250
            return True
#-----------------------------------------------------------------------------
def maneu(xx,yy):
    global x,y,speed
    
    for i in range(0,50):
        if x == xx+i and y+70 == yy:
            s = 1
            f = 0
        if x+50 == xx+i and y+70 == yy:
            s=1
            f=0
#-----------------------------------------------------------------------------
while not gameover :

    scoretext = font.render("Score = "+str(score), True, (0,0,0))
    Hscoretext = font.render("High Score = "+str(high_score), True, (0,0,0))
    w.blit ( scoretext , (20 , 30))  # blitting score in the right place   
    w.blit (Hscoretext , (20 , 60)) 
    for event in pygame.event.get():
        if event.type==QUIT:
            gameover=True
            pygame.quit()
            sys.exit()
    pygame.display.update()
    t.tick(300+q)
    w.fill((255,255,255))
    keys=pygame.key.get_pressed()
    w.blit(platform,(x1,y1))
    w.blit(platform,(x2,y2))
    w.blit(platform,(x3,y3))
    if game_status == "start":
        Start()
        w.blit(start_text,(78,100))
        if keys[K_RETURN]:
            game_status = "play"
            
    elif game_status == "play":

        if speed>0:
            y=y-1
            if l==1:
                w.blit( doodleImg, ( x,y ) )
            else:
                w.blit( doodleImgleft, ( x,y ) )
            speed=speed-1
        elif speed<=0:
            y=y+1
            if l==1:
                w.blit( doodleImg, ( x,y ) )
            else:
                w.blit( doodleImgleft, ( x,y ) )
        maned(x1,y1)
        maned(x2,y2)
        maned(x3,y3)
        maneu(x1,y1)
        maneu(x2,y2)
        maneu(x3,y3)
        if s==1:
            y1=y1+1
            y2=y2+1
            y3=y3+1
            f=f+1
        if f==250:
            s=0
        if maned(x1,y1)==True:
            if y1!=500:
                j=1
                score += 1
        if y1==500:
            j=0
        if maned(x2,y2)==True:
            if y2!=500:
                e=1
                score += 1
        if y2==500:
            e=0
        if maned(x3,y3)==True:
            if y3!=500:
                d=1
                score += 1
        if y3==500:
            d=0
        if j==1:
            y1=y1+1
            y2=y2+1
            y3=y3+1
        if e==1:
            y1=y1+1
            y2=y2+1
            y3=y3+1
        if d==1:
            y1=y1+1
            y2=y2+1
            y3=y3+1
            
        if y1>=600:
            x1=random.randint(0,200)
            y1=50
        if y2>=600:
            x2=random.randint(250,350)
            y2=50
        if y3>=600:
            x3=random.randint(0,400)
            y3=50        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 4
                l=0
            if event.key == pygame.K_RIGHT:
                x = x + 4
                l=1
        if x+70<=0:
            if l==1:
                x=400
            else:
                x=400
        if x+70>=500:
            if l==1:
                x=0
            else:
                x=0
        if y>=600:
            y=600
            print("GAME OVER")
            game_status = "end game"
        q=q+0.009999
    elif game_status == "end game":
        x1=50
        x2=300
        x3=175
        y1=400
        y2=275
        y3=75
        x=x1
        y=200
        Start()
        w.blit(exitgame,(78,100))
        w.blit(restart,(78,150))
        if ( score > high_score):
            high_score = score
        score = 0
        if keys[K_RETURN]:
            game_status = "play"
        if keys[K_ESCAPE]:
            gameover=True
#-----------------------------------------------------------------------------          
print(q//1)           
pygame.quit()
quit()
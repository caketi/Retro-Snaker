import pygame
import sys
import random
pygame.init()
size = width, height = 640, 480 
screen = pygame.display.set_mode(size) 
body = pygame.image.load('body.png')
food=pygame.image.load('food.png')
head=pygame.image.load('head.png')
phead=head.get_rect()
pfood=food.get_rect()
pbody=[]
speed = [0, 0]
clock = pygame.time.Clock()
phead=phead.move(320,224)
score=0
flag=0
mflag=1
while True:
    clock.tick(6)
    temp=body.get_rect()
    temp=temp.move(phead.left,phead.top)
    pbody.insert(0,temp)
    if flag==0:
        flag=1
        while True:
            x=random.randint(0,19)*32
            y=random.randint(0,14)*32
            pfood=pfood.move(x-pfood.left,y-pfood.top)
            if pfood not in pbody:
                break
            elif pfood in pbody:
                print("bug")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if mflag==1:
                if event.key == 119 and speed[1] == 0:
                    speed = [0, -32]
                    mflag=0
                elif event.key == 115 and speed[1] == 0:
                    speed = [0, 32]
                    mflag = 0
                elif event.key == 97 and speed[0] == 0:
                    speed = [-32, 0]
                    mflag = 0
                elif event.key == 100 and speed[0] == 0:
                    speed = [32, 0]
                    mflag = 0
    phead=phead.move(speed)
    mflag=1
    if phead.left==pfood.left and phead.top==pfood.top:
        flag=0
        score=score+1
        pygame.display.set_caption(str(score)+"分")
        if score==9600-1:
            print("You Win")
            break
    else:
        del pbody[len(pbody)-1]

    if phead.left < 0 or phead.right > width or phead.top < 0 or phead.bottom > height:
        print("GameOver")
        break
    screen.fill((0,0,0))
    screen.blit(food, pfood)
    for i in pbody:
        screen.blit(body,i)
    screen.blit(head, phead)
    pygame.display.flip()
    if phead in pbody:
        print("GameOver")
        break
while True:
    clock.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

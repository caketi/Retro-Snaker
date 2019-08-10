import pygame
import sys
import random
pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
body = pygame.image.load('body.png')  # 加载图片
food=pygame.image.load('food.png')
head=pygame.image.load('head.png')
phead=head.get_rect()
pfood=food.get_rect()
pbody=[]
speed = [0, 0]  # 设置移动的X轴、Y轴
clock = pygame.time.Clock()  # 设置时钟
phead=phead.move(320,224)
score=0
flag=0
mflag=1
while True:  # 死循环确保窗口一直显示
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
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
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
        if score==9600-1:
            print("You Win")
            break
    else:
        del pbody[len(pbody)-1]

    if phead.left < 0 or phead.right > width or phead.top < 0 or phead.bottom > height:
        print("GameOver")
        break
    screen.fill((0,0,0))  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(food, pfood)
    for i in pbody:
        screen.blit(body,i)
    screen.blit(head, phead)
    pygame.display.flip()  # 更新全部显示
    if phead in pbody:
        print("GameOver")
        break
while True:
    clock.tick(2)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

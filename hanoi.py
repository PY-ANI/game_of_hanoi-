import pygame
from threading import Thread
from utils import box,button,Solve

pygame.init()

win=pygame.display.set_mode((400,400))
pygame.display.set_caption("tower of hanaoi")

clock=pygame.time.Clock()

n=5
space=100//n
containers={1:[],2:[],3:[]}
selected=None
fps=160

#changing containers of blocks

def change_container(pos):
    global selected

    if(selected != None):
        if len(containers[selected+1])>0:
            if len(containers[pos+1])==0 or (containers[pos+1][-1].get_size() > containers[selected+1][-1].get_size()):
                containers[pos+1].append(containers[selected+1].pop())

# creating instances of box class and allocating values.
 
def allocate():
    containers[1].clear()
    for i in range(n):
        containers[1].append(box(win,(10*i),space))

def Reset():
    containers[1].clear()
    containers[2].clear()
    containers[3].clear()

reset=button(win,"RESET",20,(255,255,255),50,0)
solve=button(win,"SOLVE",20,(255,255,255),150,0)
decrement=button(win,"<<",20,(255,255,255),250,0)
increment=button(win,">>",20,(255,255,255),300,0)

allocate()

run=True
while run:

    mouse_pos=pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(50,351) and mouse_pos[1] >= 30:
            selected=(mouse_pos[0]-50)//100

        if event.type == pygame.MOUSEBUTTONUP and mouse_pos[0] in range(50,351) and mouse_pos[1] >= 30:
            change_container((mouse_pos[0]-50)//100)
            selected=None
        
        if event.type == pygame.MOUSEBUTTONDOWN and reset.button_clicked(mouse_pos):
            Reset()
            allocate()
        
        if event.type == pygame.MOUSEBUTTONDOWN and solve.button_clicked(mouse_pos):
            Thread(target=Solve,args=(n,containers,1,2,3),daemon=True).start()
        
        if event.type == pygame.MOUSEBUTTONDOWN and increment.button_clicked(mouse_pos) and n <= 7:
            Reset()
            n+=1
            allocate()
        
        if event.type == pygame.MOUSEBUTTONDOWN and decrement.button_clicked(mouse_pos) and n > 3:
            Reset()
            n-=1
            allocate()

    win.fill((255,255,255))

    for index,i in enumerate(containers[1]):
        i.draw(0,index)
    for index,i in enumerate(containers[2]):
        i.draw(100,index)
    for index,i in enumerate(containers[3]):
        i.draw(200,index)

    reset.draw_buttons()
    solve.draw_buttons()
    increment.draw_buttons()
    decrement.draw_buttons()

    pygame.draw.rect(win,(0,0,0),(50,30,100,350),1)
    pygame.draw.line(win,(0,0,0),(100,380),(100,100))
    pygame.draw.rect(win,(0,0,0),(150,30,100,350),1)
    pygame.draw.line(win,(0,0,0),(200,380),(200,100))
    pygame.draw.rect(win,(0,0,0),(250,30,100,350),1)
    pygame.draw.line(win,(0,0,0),(300,380),(300,100))

    pygame.display.update()

pygame.quit()
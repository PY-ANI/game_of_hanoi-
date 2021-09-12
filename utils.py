import pygame
import time

class box():
    def __init__(self,win,size,offset) -> None:
        self.win=win
        self.size=size
        self.color=(0,0,200)
        self.offset=offset
    
    def draw(self,x,y):
        pygame.draw.rect(self.win,self.color,(50+x+(self.size/2),370-(self.offset*y),100-self.size,10))

    def get_size(self):
        return 100-self.size


class button():
    def __init__(self,win,name,size,color,x,y) -> None:
        self.win=win
        self.name=name
        self.size=size
        self.color=color
        self.x=x
        self.y=y

    def draw_buttons(self):

        btn_font=pygame.font.SysFont("comicon",self.size)
        btn_surf=btn_font.render(self.name,True,self.color)
        pygame.draw.rect(self.win,(0,0,0),(self.x,self.y,self.size*len(self.name)//2,self.size))
        self.win.blit(btn_surf,(self.x+2,self.y+2))

    def button_clicked(self,pos):
        if pos[1]<=50 and pos[0] <= self.x+(self.size*len(self.name)//2) and pos[0] >= self.x:
            return 1
        return 0


def Solve(n,c,start,through,end):
    if n==1:
        c[end].append(c[start].pop())
        time.sleep(0.10)
    else:
        Solve(n-1,c,start,end,through)
        c[end].append(c[start].pop())
        time.sleep(0.10)
        Solve(n-1,c,through,start,end)
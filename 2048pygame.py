# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 02:00:54 2018

@author: miki1
"""

import pygame
from pygame.locals import Rect
from random import randint
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
L=400
SIZEX=L
SIZEY=L
a=[]

def printmat(mat):
    for i in range(4):
        print(mat[i])
        
def insertrand(mat):
    opt=[]
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                opt.append((i,j))
    if len(opt)!=0:
        pick=opt[randint(0,len(opt)-1)]
        mat[pick[0]][pick[1]]= 2 if randint(0,1)==1 else 4
        return mat
    else:
        return -1

def startgame(mat):
    for i in range(4):
        mat.append([])
        for j in range(4):
            a[i].append(0)
    mat=insertrand(mat)
    mat=insertrand(mat)
    printmat(mat)
    return mat
    
def rotateclock(mat):
    new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            new[j][3-i]=mat[i][j]
    return new

def rotatecounter(mat):
    new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            new[i][j]=mat[j][3-i]
    return new
def slide(row):
    z=[]
    n=[]
    for i in row:
        if i==0:
            z.append(0)
        else:
            n.append(i)
    return z+n
def combine(row):
    i=len(row)-1
    while i>0:
        if row[i]!=0 and row[i]==row[i-1]:
            row[i]=row[i]+row[i-1]
            row[i-1]=0
            i=i-1
        i=i-1
    return row

def checkisfull(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return False
    return True

def checkvictory(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return True
    return False
def getcolor(val):
    if val==2:
        return (255,69,0)
    elif val==4:
        return (255,192,50)
    elif val==8:
        return (255,0,255)
    elif val==16:
        return (0,255,0)
    elif val==32:
        return (255,0,0)
    elif val==64:
        return (192,0,255)
    elif val==128:
        return (0,0,255)
    elif val==256:
        return (255,60,200)
    elif val==256:
        return (0,180,70)
    elif val==512:
        return (0,0,0)
    elif val==1024:
        return (200,40,200)
    elif val==2048:
        return (69,0,150)
    
class Board(object):
    def __init__(self,sx,sy):
        self.x=sx
        self.y=sy
        pygame.init()
        self.rekt=Rect(0,0,sx,sy)
        self.screen=pygame.display.set_mode(self.rekt.size,0)
        self.bg=pygame.Surface(self.rekt.size)
        self.a=startgame(a)
        self.lost=0
        
    def blit(self):
        self.screen.fill((192,192,192))
        for i in range(3):
            pygame.draw.line(self.screen,(0,0,0),(0,100*(i+1)),(400,100*(i+1)))
        for i in range(3):
            pygame.draw.line(self.screen,(0,0,0),(100*(i+1),0),(100*(i+1),400))
        for i in range(4):
            for j in range(4):
                if self.a[i][j]!=0:
                    
                    textsurface = myfont.render(str(self.a[i][j]), False, getcolor(self.a[i][j]))
                    self.screen.blit(textsurface,(40+100*j,30+100*i))
        pygame.display.update()
    def run(self):
        while 1:
            self.blit()
            pygame.time.delay(5)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self._running = False
                    pygame.quit()
                if e.type == pygame.KEYDOWN:
                    prima=self.a
                    if e.key==pygame.K_q:
                        self._running = False
                        pygame.quit()
                    if e.key==pygame.K_RIGHT:
                        for i in range(4):
                            self.a=rotateclock(self.a)
                            self.a=rotatecounter(self.a)
                            self.a[i]=slide(self.a[i])
                            self.a[i]=combine(self.a[i])
                            self.a[i]=slide(self.a[i])
                            
                    if e.key==pygame.K_UP:
                        self.a=rotateclock(self.a)
                        for i in range(4):
                            self.a[i]=slide(self.a[i])
                            self.a[i]=combine(self.a[i])
                            self.a[i]=slide(self.a[i])
                        self.a=rotatecounter(self.a)
                        
                    if e.key==pygame.K_LEFT:
                        self.a=rotateclock(self.a)
                        self.a=rotateclock(self.a)
                        for i in range(4):
                            self.a[i]=slide(self.a[i])
                            self.a[i]=combine(self.a[i])
                            self.a[i]=slide(self.a[i])
                        self.a=rotatecounter(self.a)
                        self.a=rotatecounter(self.a)
                        
                    if e.key==pygame.K_DOWN:
                        self.a=rotateclock(self.a)
                        self.a=rotateclock(self.a)
                        self.a=rotateclock(self.a)
                        for i in range(4):
                            self.a[i]=slide(self.a[i])
                            self.a[i]=combine(self.a[i])
                            self.a[i]=slide(self.a[i])
                        self.a=rotatecounter(self.a)
                        self.a=rotatecounter(self.a)
                        self.a=rotatecounter(self.a)
                        
                    if checkisfull(self.a):
                        self.lost=1
                    else:
                        if prima!=self.a:
                            printmat(prima)
                            printmat(self.a)
                            self.a=insertrand(self.a)
                        
            if self.lost==1:
                textsurface = myfont.render("HAI PERSO!", False, (255, 0, 0))
                self.screen.blit(textsurface,(40,200))
                pygame.display.update()
                pygame.time.delay(5000)
                self._running = False
                pygame.quit()
            elif checkvictory(self.a):
                textsurface = myfont.render("HAI VINTO!", False, (255, 0, 0))
                self.screen.blit(textsurface,(40,200))
                pygame.display.update()
                pygame.time.delay(5000)
                self._running = False
                pygame.quit()

class Splash(object):
    def __init__(self):
        self.x=SIZEX
        self.y=SIZEY
if __name__=="__main__":
    game=Board(SIZEX,SIZEY)
    game.run()


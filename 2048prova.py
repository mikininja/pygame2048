# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 01:21:48 2018

@author: miki1
"""

from random import randint
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

a=startgame(a)
lost=0

while lost==0:
    mossa=input()
    if mossa=='d':
        for i in range(4):
            a[i]=slide(a[i])
            a[i]=combine(a[i])
            a[i]=slide(a[i])
        if checkisfull(a):
            lost=1
        else:
            a=insertrand(a)
        printmat(a)
    elif mossa=='w':
        a=rotateclock(a)
        for i in range(4):
            a[i]=slide(a[i])
            a[i]=combine(a[i])
            a[i]=slide(a[i])
        if checkisfull(a):
            lost=1
        else:
            a=insertrand(a)
        a=rotatecounter(a)
        printmat(a)
    elif mossa=='a':
        a=rotateclock(a)
        a=rotateclock(a)
        for i in range(4):
            a[i]=slide(a[i])
            a[i]=combine(a[i])
            a[i]=slide(a[i])
        if checkisfull(a):
            lost=1
        else:
            a=insertrand(a)
        a=rotatecounter(a)
        a=rotatecounter(a)
        printmat(a)
    elif mossa=='s':
        a=rotateclock(a)
        a=rotateclock(a)
        a=rotateclock(a)
        for i in range(4):
            a[i]=slide(a[i])
            a[i]=combine(a[i])
            a[i]=slide(a[i])
        if checkisfull(a):
            lost=1
        else:
            a=insertrand(a)
        a=rotatecounter(a)
        a=rotatecounter(a)
        a=rotatecounter(a)
        printmat(a)
    elif mossa=='q':
        print("esco dal gioco")
        lost=1
    else:
        print("mossa non valida")
    
print("Hai perso!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
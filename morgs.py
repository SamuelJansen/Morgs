import GameLibrary as gl
import sys
import os
import pygame as pg
import time as now
import numpy as np

###############################################################################
#- Initializing global paths, sizes, etc
###############################################################################
name = 'morgs'
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255),
            'backgroundColor' : (237,201,202,255),
            'red' : (255,0,0)
            }
fps = 60
aps = 30
game = gl.Game(name,fps,aps,colors)
#g1 = gl.Game(name,path,fps,aps,colors,screenSize,osPosition=(screenSize[0]+1,0))

objectSize = [100,70]

objects = {}
"""
objName = 'background'
objects[objName] = gl.Object(objName,g.size,1000,[0,0],1,g)
for index in range(1) :
    objName = 'HellenFrost'
    objects[objName + str(index)] = gl.Object(
        objName,
        objectSize,
        400,
        [g.screenSize[0]*np.random.random_sample(),g.screenSize[1]*np.random.random_sample()],
        2,
        g
    )
#"""
"""
for index in range(1,10) :
    objName = 'HellenFrost'
    objects[objName + str(index)] = gl.Object(
        objName,
        objectSize,
        200,
        [g.screenSize[0]*np.random.random_sample(),g.screenSize[1]*np.random.random_sample()],
        2,
        g
    )

for index in range(10,110) :
    objName = 'HellenFrost'
    objects[objName + str(index)] = gl.Object(
        objName,
        objectSize,
        50,
        [g.screenSize[0]*np.random.random_sample(),g.screenSize[1]*np.random.random_sample()],
        2,
        g
    )
#"""
"""
upSound = gl.getSound('Sounds/Up.wav')
downSound = gl.getSound('Sounds/Down.wav')
leftSound = gl.getSound('Sounds/Left.wav')
#"""
objects['menu'] = gl.Object(
    'menu',
    [200,200],
    100,
    [200,200],
    .5,
    game
)
objects['menu2'] = gl.Object(
    'menu2',
    [200,200],
    100,
    [200,500],
    .5,
    game
)
objects['menu3'] = gl.Object(
    'menu3',
    [200,200],
    10,
    [700,700],
    .5,
    game
)
objects['menu4'] = gl.Object(
    'menu4',
    [200,200],
    10,
    [800,800],
    .5,
    game
)
objects['menu5'] = gl.Object(
    'menu5',
    [200,200],
    10,
    [500,900],
    .5,
    game
)
objects['menu6'] = gl.Object(
    'menu6',
    [200,200],
    10,
    [700,100],
    .5,
    game
)
uxElements = {}
uxElements['menu'] = gl.UXSurface([200,200],[200,200],game)

endGame = False
arrow = gl.ArrowKey()
mouse = gl.Mouse(game)
frame = gl.Frame(now.time(),game)
screen = gl.Screen(objects,game)
move = [np.random.randint(3)-1,np.random.randint(3)-1]

def exitGame(mouse,game) :
    if mouse.position[0]==game.devScreenSize[0]-1 and mouse.position[1]==0 :
        game.playing = False

while game.playing :

    if frame.apfNew :
        #'''
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                game.playing = False
            arrow.events(event)
            mouse.events(event)
            """
            if a.arrows[1]==-1 :
                gl.playSound(upSound)
            if a.arrows[1]==1 :
                gl.playSound(downSound)
            if a.arrows[0]==1 :
                gl.playMusic('Sounds/TakeaWalk.mp3')
            if a.arrows[0]==-1 :
                gl.playSound(leftSound)
            #"""
        exitGame(mouse,game)
        move = arrow.status

        """
        if len(objects)>1 :
            objects['background'].updatePosition(move,objects,g)
        if len(objects)>2 :
            for i in range(1,len(objects)-1) :
                move = [np.random.randint(3)-1,np.random.randint(3)-1]
                objects['HellenFrost' + str(i)].updatePosition(move,objects,g)
        #"""
        #'''
        move = [np.random.randint(3)-1,np.random.randint(3)-1]
        objects['menu3'].updatePosition(move,objects,g)
        move = [np.random.randint(3)-1,np.random.randint(3)-1]
        objects['menu4'].updatePosition(move,objects,g)
        move = [np.random.randint(3)-1,np.random.randint(3)-1]
        objects['menu5'].updatePosition(move,objects,g)
        move = [np.random.randint(3)-1,np.random.randint(3)-1]
        objects['menu6'].updatePosition(move,objects,g)

    frame.update(now.time(),screen,game)
    if frame.new :
        # objects['menu'].rect.move_ip(0,1)
        objects['menu'].updatePosition([0,1],objects,game)
        screen.blit(objects,frame,game)
        # screen.draw(uxElements,frame,game)

pg.quit()
print(gl.imageLibrary)
#sys.exit()

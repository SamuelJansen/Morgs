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
upSound = gl.getSound('Sounds/Up.wav')
downSound = gl.getSound('Sounds/Down.wav')
leftSound = gl.getSound('Sounds/Left.wav')
#"""
objects['thing'] = gl.Object(
    'thing',
    [200,200],
    100,
    [200,200],
    .5,
    game
)
uxElements = {}
uxElements['menu'] = gl.UXSurface([200,200],[200,200],game)

def exitGame(mouse,game) :
    if mouse.position[0]==game.devScreenSize[0]-1 and mouse.position[1]==0 :
        game.playing = False

def itColided(objects,objectName) :
    objectsRectList = [] ###- it needs to come from imput
    for thisObjectName,o in objects.items() :
        objectsRectList.append(o.rect)
    colisionIndexes = objects[objectName].rect.collidelistall(objectsRectList)
    if list(objects.keys()).index(objects[objectName].name) in colisionIndexes :
        return len(colisionIndexes)>1
    return len(colisionIndexes)>0

def dealWithColision(objects,objectName) :
    objectName += str(len(objects)-1)
    if itColided(objects,objectName) :
        print(objectName)
        del objects[objectName]

def newObject():
    if len(objects)<amountOfThings :
        if len(objects)<amountOfThings*percentualBigThings/100 :
            objectProportion = objectBigProportion
        else :
            objectProportion = objectSmallProportion

        objects[objectName + str(len(objects))] = gl.Object(
            objectName + str(len(objects)),
            objectSize,
            objectProportion,
            [game.screenSize[0]*np.random.random_sample(),game.screenSize[1]*np.random.random_sample()],
            objectVelocity,
            game
        )

amountOfThings = 16
percentualBigThings = 90
objectName = 'thing'
objectSize = [200,200]
objectBigProportion = 300
objectSmallProportion = 10
objectVelocity = .5

endGame = False
arrow = gl.ArrowKey()
mouse = gl.Mouse(game)
frame = gl.Frame(now.time(),game)
screen = gl.Screen(objects,game)
move = [np.random.randint(3)-1,np.random.randint(3)-1]
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
        #'''
        newObject()

        dealWithColision(objects,objectName)

        for i in range(1,len(objects)) :
            move = [np.random.randint(3)-1,np.random.randint(3)-1]
            objects['thing'+str(i)].updatePosition(move,objects,game)

    frame.update(now.time(),screen,game)
    if frame.new :
        # objects['menu'].rect.move_ip(0,1)
        objects['thing'].updatePosition([0,1],objects,game)
        screen.blit(objects,frame,game)
        # screen.draw(uxElements,frame,game)

pg.quit()
print(gl.imageLibrary)
#sys.exit()

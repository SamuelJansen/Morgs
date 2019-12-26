#import GameLibrary as gl
import sys
import os
import pygame as pg
import time as now
import numpy as np
from model import Game, Object, ArrowKey, Screen, Mouse, Frame
from model.performance_measurement import PerformanceMeasurement as pm
from function import image

###############################################################################
#- Initializing global paths, sizes, etc
###############################################################################
name = 'morgs'
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255),
            'backgroundColor' : (237,201,202),
            'red' : (255,0,0)
            }
fps = 60
aps = 30
game = Game.Game(name,fps,aps,now.time(),colors)

performanceMeasurement = pm.PerformanceMeasurement(
    game,
    ammountOfThings = 100,
    percentualBigThings = 90,
    objectSize = [2000,200],
    objectSpaceCostSize = [2000,100],
    objectBigProportion = 30,
    objectSmallProportion = 10,
    objectVelocity = .5,
    mustPopulate = True
)

cenario = {}

arrow = ArrowKey.ArrowKey()
mouse = Mouse.Mouse(game)
move = [np.random.randint(3)-1,np.random.randint(3)-1]
while game.playing :

    if game.frame.apfNew :
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
        performanceMeasurement.exitGame(mouse,game)
        performanceMeasurement.populateTheScreen(game)

        game.updateSpaceCostRectList()

        performanceMeasurement.moveObjectsRandomically(game)

    game.update(now.time())

pg.quit()
print(image.imageLibrary)
#sys.exit()

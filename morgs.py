#import GameLibrary as gl
import sys
import os
import pygame as pg
import time as now
import numpy as np
from model import Game, Object, Cenario, ArrowKey, Screen, Mouse, Frame
from model.performance_measurement import PerformanceMeasurement as pm

###############################################################################
#- Initializing global paths, sizes, etc
###############################################################################
name = 'morgs'
gameSection = 'two_mountains/'
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
    gameSection,
    amountOfThings = 200,
    percentualBigThings = 90,
    objectSize = [200,200],
    objectSpaceCostSize = [200,100],
    objectBigProportion = 50,
    objectSmallProportion = 10,
    objectVelocity = .5,
    mustPopulate = True
)

# cenarioName = 'cenario'
# cenarioPosition = [0,0]
# Cenario.BasicCenarioClass(
#     cenarioName,
#     gameSection,
#     cenarioPosition,
#     [200,200],
#     .5,
#     game
# )
# cenarioName = 'cenario'
# cenarioLongitudes = 4
# cenarioLatitudes = 3
# cenarioInitialCoordinate = [0,0]
# cenarioVelocity = .5
# Cenario.Cenario(
#     cenarioName,
#     gameSection,
#     cenarioLongitudes,
#     cenarioLatitudes,
#     cenarioInitialCoordinate,
#     cenarioVelocity,
#     game
# )
Cenario.OneImageCenario('cenario',gameSection,.5,game)

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

        game.updateSpaceCostRectList()

        performanceMeasurement.moveObjectsRandomically(game)

    game.update(now.time())

pg.quit()
#sys.exit()

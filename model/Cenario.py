import pygame as pg
import numpy as np
from model import Game, Object
from function import imageFunction

class OneImageCenario(Object.Object):
    def __init__(self,name,folder,velocity,game):
        cenarioPosition = [0,0]
        Object.Object(
            name,
            folder,
            cenarioPosition,
            game.size,
            game.scaleRange,
            velocity,
            game,
            type=Object.ObjectTypes.CENARIO
        )

class Cenario(Object.Object):
    def __init__(self,name,folder,longitudes,latitudes,initialCoordinate,velocity,game):
        '''
        longitudes = columns
        latitudes = lines
        initialCoordinate = [longitude,latitude]'''
        self.name = name
        self.folder = folder
        self.longitudes = longitudes
        self.latitudes = latitudes
        self.coordinateSize = [game.size[0]//game.longitudesImageOnScreen,game.size[1]//game.latitudesImageOnScreen]
        self.scale = game.scaleRange/game.latitudesImageOnScreen
        self.coordinatesIndex = self.longitudes * self.latitudes
        ###- the variable below needs some work
        initialPosition = [
            initialCoordinate[0],
            initialCoordinate[1]
        ]
        self.imagePath = game.imagePath + self.name + '.png'
        self.size = [
            self.coordinateSize[0]*self.longitudes,
            self.coordinateSize[1]*self.latitudes
        ]
        self.cenarioImage = imageFunction.getImage(self.imagePath,self.size,game)
        self.rect = pg.Rect(0,0,self.size[0],self.size[1])
        self.cenarioImageSurface = imageFunction.newImageSurface(self.cenarioImage,self.size)
        self.coordinatesName = []
        for coordinateIndex in range(self.coordinatesIndex) :
            coordinatePosition = [
                initialPosition[0]+int(np.ceil((coordinateIndex%self.longitudes)*self.coordinateSize[0])),
                initialPosition[1]+int(np.ceil((coordinateIndex%self.latitudes)*self.coordinateSize[1]))
            ]
            cenarioSubImage = self.cenarioImageSurface.subsurface((
                coordinatePosition[0], coordinatePosition[1], self.coordinateSize[0], self.coordinateSize[1]))
            cenarioSubImageName = self.name + str(coordinateIndex)
            cenarioSubImagePath = game.imagePath + self.folder + Object.ObjectTypes.getType(Object.ObjectTypes.CENARIO) + '/' + cenarioSubImageName  + '.png'
            imageFunction.saveImage(cenarioSubImage,cenarioSubImagePath)

            self.coordinatesName.append(Object.Object(
                cenarioSubImageName,
                self.folder,
                coordinatePosition,
                self.coordinateSize,
                self.scale,
                velocity,
                game,
                type=Object.ObjectTypes.CENARIO
            ).name)

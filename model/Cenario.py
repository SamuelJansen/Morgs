import pygame as pg
import numpy as np
from model import Game, Object
from function import image

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
        initialPosition = [
            initialCoordinate[0],
            initialCoordinate[1]
        ]
        self.imagePath = game.imagePath + self.name + '.png'
        self.size = [
            self.coordinateSize[0]*self.longitudes,
            self.coordinateSize[1]*self.latitudes
        ]
        self.cenarioImage = pg.transform.smoothscale(image.getImage(self.imagePath,game),self.size)
        self.cenarioImageSurface = pg.Surface(self.size,pg.HWSURFACE|pg.SRCALPHA)#.convert_alpha().set_alpha(10)
        self.cenarioImageSurface.blit(self.cenarioImage, (0,0))
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
            image.saveImage(cenarioSubImage,cenarioSubImagePath)
            # pg.image.save(cenarioSubImage, game.imagePath + cenarioSubImageName + '.png')

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

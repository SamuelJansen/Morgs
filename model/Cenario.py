import pygame as pg
import numpy as np
from model import Game, Object
from function import imageFunction

class BasicCenarioClass(Object.Object):
    def __init__(self,name,folder,position,size,velocity,game):
        self.size = [game.size[0]//4,game.size[1]//3]
        self.scale = game.scaleRange/3
        self.amountOfColumnPieces = 4
        self.amountOfLinePieces = 3
        self.amountOfPieces = self.amountOfColumnPieces * self.amountOfLinePieces
        self.piecesName = []
        cenarioPiecePosition = []
        for piece in range(self.amountOfPieces) :
            self.piece = piece
            cenarioPiecePosition = [
                position[0]+int(np.ceil((piece%self.amountOfColumnPieces)*self.size[0])),
                position[1]+int(np.ceil((piece%self.amountOfLinePieces)*self.size[1]))
            ]
            self.piecesName.append(Object.Object(
                name+str(self.piece),
                folder,
                cenarioPiecePosition,
                self.size,
                self.scale,
                velocity,
                game,
                type=Object.ObjectTypes.CENARIO
            ).name)

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
        self.cenarioImage = pg.transform.smoothscale(imageFunction.getImage(self.imagePath,game),self.size)
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

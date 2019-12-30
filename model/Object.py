import pygame as pg
import numpy as np
from model import Game
from function import imageFunction

class ObjectTypes:
    CENARIO = '0  cenario'
    STANDARD_OBJECT = '10 standard_object'

    def getType(type):
        return type[3:]

class Object:
    '''
    It's a object'''
    def __init__(self,name,folder,position,size,scale,velocity,game,type=ObjectTypes.STANDARD_OBJECT,spaceCostSize=None):
        '''
        Object()'''
        self.name = name
        self.folder = folder + ObjectTypes.getType(type) + '/'
        self.type = type
        self.size = size.copy()
        self.scale = scale
        self.scaleFactor = (self.scale * game.screenSize[1]) / (game.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.imagePath = game.imagePath + self.folder + self.name + '.png'
        self.image = pg.transform.smoothscale(imageFunction.getImage(self.imagePath,game),self.size)
        self.imageSurface = pg.Surface(self.size,pg.HWSURFACE|pg.SRCALPHA)#.convert_alpha().set_alpha(10)
        self.imageSurface.blit(self.image, (0,0))

        self.rect = pg.Rect(position[0],position[1],self.size[0],self.size[1])

        if spaceCostSize :
            self.spaceCostSize = spaceCostSize.copy()
            self.collides = True
        else :
            self.spaceCostSize = size.copy()
            self.collides = False
        self.spaceCostSize[0] = int(np.ceil(self.spaceCostSize[0] * self.scaleFactor))
        self.spaceCostSize[1] = int(np.ceil(self.spaceCostSize[1] * self.scaleFactor))
        self.spaceCostRect = pg.Rect(
            position[0],
            position[1]+self.size[1]-self.spaceCostSize[1],
            self.spaceCostSize[0],
            self.spaceCostSize[1]
        )

        self.velocity = velocity * game.velocityControl

        game.addNewObject(self)
        ###- print(f'{self.name} created successfully')

    def updatePosition(self,move,game):
        '''
        It updates the object position
        updatePosition(move,game)'''
        originalSpaceCostRect = self.spaceCostRect.copy()
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            xMovement = move[0]/module
            yMovement = move[1]/module
            self.spaceCostRect.move_ip(xMovement,yMovement)
            if self.itColided(game) :
                self.spaceCostRect = originalSpaceCostRect
            else :
                self.rect.move_ip(xMovement,yMovement)

    def itColided(self,game):
        if self.collides :
            colisionIndexes = self.spaceCostRect.collidelistall(game.spaceCostObjectsPositionRectList)
            # try :
            #     if list(game.collidableObjects.keys()).index(self.name) in colisionIndexes :
            #         return len(colisionIndexes)>1
            #     # return len(colisionIndexes)>0
            # except :
            #     pass
            if list(game.collidableObjects.keys()).index(self.name) in colisionIndexes :
                return len(colisionIndexes)>1
            # return len(colisionIndexes)>0
        return False

    def getPosition(self):
        return [self.spaceCostRect[0],self.rect[1]] ###- upper left corner

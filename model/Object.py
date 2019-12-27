import pygame as pg
import numpy as np
from function import image
from model import Game

class ObjectTypes:
    CENARIO = '0 CENARIO'
    STANDARD_OBJECT = '1 STANDARD_OBJECT'

class Object:
    '''
    It's a object'''
    def __init__(self,name,position,size,scale,velocity,game,type=ObjectTypes.STANDARD_OBJECT,spaceCostSize=None):
        '''
        Object()'''
        self.name = name
        self.type = type
        self.size = size.copy()
        self.scale = scale
        self.scaleFactor = (self.scale * game.screenSize[1]) / (game.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.imagePath = game.imagePath + self.name + '.png'
        try :
            self.image = pg.transform.smoothscale(getImage(self.imagePath),self.size)
        except :
            self.image = pg.transform.smoothscale(image.getImage(game.imagePath+'standardImage.png'),self.size)
        self.imgSurface = pg.Surface(self.size,pg.HWSURFACE|pg.SRCALPHA)#.convert_alpha().set_alpha(10)
        self.imgSurface.blit(self.image, (0,0))

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
        ###- print(f'{self.name} created successful')

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
            if list(game.objects.keys()).index(self.name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def getPosition(self):
        return [self.spaceCostRect[0],self.rect[1]] ###- upper left corner

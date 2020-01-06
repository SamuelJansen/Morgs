from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
import pygame as pg
import numpy as np
from model import Game
from function import imageFunction

class ObjectTypes:
    CENARIO = '0 cenario'
    STANDARD_OBJECT = '10 standard_object'
    USER_INTERFACE = '100 user_interface'

    def getType(type):
        return type.split()[1]

class Object:
    '''
    It's a object'''
    def __init__(self,name,folder,position,size,scale,velocity,game,
            type = ObjectTypes.STANDARD_OBJECT,
            spaceCostSize = None,
            imagePath = None,
            soundPath = None,
            father = None
        ):
        '''
        Object()'''
        self.name = name
        if not father :
            self.father = game
            self.type = type
        else :
            self.father = father
            self.type = self.getType(type)
        self.size = size.copy()
        self.scale = scale
        self.scaleFactor = (self.scale * game.size[1]) / (game.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.position = position ###- self.getPosition() #
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

        self.folder = folder + ObjectTypes.getType(type) + '/'
        if not imagePath :
            self.imagePath = game.imagePath + self.folder + self.name + '.png'
        else :
            self.imagePath = imagePath
        self.image = imageFunction.getImage(self.imagePath,self.size,game)
        self.imageSurface = imageFunction.newImageSurface(self.image,self.size)

        self.soundPath = soundPath

        if spaceCostSize :
            self.spaceCostSize = spaceCostSize.copy()
            self.collides = True
        else :
            self.spaceCostSize = size.copy()
            self.collides = False
        self.spaceCostSize[0] = int(np.ceil(self.spaceCostSize[0] * self.scaleFactor))
        self.spaceCostSize[1] = int(np.ceil(self.spaceCostSize[1] * self.scaleFactor))
        self.spaceCostRect = pg.Rect(
            self.position[0],
            self.position[1]+self.size[1]-self.spaceCostSize[1],
            self.spaceCostSize[0],
            self.spaceCostSize[1]
        )

        self.velocity = velocity * game.velocityControl

        self.objects = {}
        self.father.addNewObject(self)
        ###- print(f'{self.name} created successfully')

    def updatePosition(self,move,game):
        '''
        It updates the object position
        updatePosition(move,game)'''
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            xMovement = move[0]/module
            yMovement = move[1]/module
            self.spaceCostRect.move_ip(xMovement,yMovement)
            if self.itColided(game) :
                self.spaceCostRect.move_ip(-xMovement,-yMovement)
                self.position = self.getPosition()
            else :
                self.rect.move_ip(xMovement,yMovement)

    def itColided(self,game):
        if self.collides :
            colisionIndexes = self.spaceCostRect.collidelistall(game.spaceCostObjectsPositionRectList)
            if list(game.collidableObjects.keys()).index(self.name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def getPosition(self):
        return [self.rect[0],self.rect[1]] ###- upper left corner

    def addNewObject(self,object):
        self.objects[object.name] = object

    def getType(self,type):
        type = type.strip().split()
        type[1] = str(int(type[1])+int(self.father.type.strip.split()[0]))
        type = ''.join(type)
        print(f'Object {self.name} has the following type = {type}')
        return type

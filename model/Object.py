import pygame as pg
import numpy as np
from function import image

class Object:
    '''
    It's a object'''
    def __init__(self,name,size,scale,position,velocity,g):
        '''
        Object(name,size,position)'''
        self.name = name
        self.size = size
        self.scaleFactor = (scale * g.screenSize[1]) / (g.scaleRange * self.size[1])
        self.size[0] = int(np.ceil(self.size[0] * self.scaleFactor))
        self.size[1] = int(np.ceil(self.size[1] * self.scaleFactor))

        self.imagePath = g.imagePath + self.name + '.png'
        ###self.img = pg.transform.smoothscale(getImage(self.imagePath),self.size)
        try :
            self.img = pg.transform.smoothscale(getImage(self.imagePath),self.size)
        except :
            self.img = pg.transform.smoothscale(image.getImage(g.imagePath+'standardImage.png'),self.size)
        self.imgSurface = pg.Surface(self.size,pg.HWSURFACE|pg.SRCALPHA)#.convert_alpha()
        self.imgSurface.blit(self.img, (0,0))

        self.position = position
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.velocity = velocity * g.velocityControl
        print(f'{self.name} created successful')

    def updatePosition(self,move,objects,g):
        '''
        It updates the object position
        position(move,g)'''
        originalRect = self.rect.copy()
        if move[0]!=0 or move[1]!=0 :
            module = ( (move[0]**2+move[1]**2)**(1/2) ) / self.velocity
            # objects['menu'].rect.move(0,1)
            self.rect.move_ip(move[0]/module,move[1]/module)
            objectsRectList = [] ###- it needs to come from imput
            for objectName,o in objects.items() :
                objectsRectList.append(o.rect)
            if self.itColided(objects,objectsRectList) :
                ###- print('colision')
                self.rect = originalRect

    def itColided(self,objects,objectsRectList) :
        colisionIndexes = self.rect.collidelistall(objectsRectList)
        if list(objects.keys()).index(self.name) in colisionIndexes :
            return len(colisionIndexes)>1
        return len(colisionIndexes)>0

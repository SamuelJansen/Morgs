import pygame as pg

class Screen():
    '''
    It blits all objects on the screen'''
    def __init__(self,objects,g):
        '''
        It blits all objects on the screen'''
        ###- g.screen.fill(g.color['backgroundColor'])
        self.rectToBlit = pg.Rect(
            0,
            0,
            g.screenSize[0],
            g.screenSize[1]
        )
        listToBlit = []
        for objectName,o in objects.items() :
            print(o)
            if self.rectToBlit.colliderect(o.rect) :
                ###g.screen.blit(o.img,o.rect)
                listToBlit.append((o.imgSurface,o.rect))
        g.screen.blits(listToBlit)

    def blit(self,objects,f,g):
        '''
        It blits all objects on the screen'''

        g.screen.fill(g.color['backgroundColor'])
        self.rectToBlit = pg.Rect(
            0,
            0,
            g.screenSize[0],
            g.screenSize[1]
        )
        listToBlit = []
        for objectName,o in objects.items() :
            if self.rectToBlit.colliderect(o.rect) :
                listToBlit.append((o.imgSurface,o.rect))
        g.screen.blits(listToBlit)

    def draw(self,uxElements,g):
        '''
        It blits all UX Elements on the screen'''
        pg.draw
        g.screen.blits(uxElements)

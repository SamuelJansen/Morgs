import pygame as pg

class Screen():
    '''
    It blits all objects on the screenMode'''
    def __init__(self,game):
        '''
        It blits all objects on the screenMode'''
        game.screenMode.fill(game.color['backgroundColor'])
        self.rectToBlit = pg.Rect(
            0,
            0,
            game.screenSize[0],
            game.screenSize[1]
        )
        self.listToBlit = [
            (object.imgSurface,object.rect)
            for object in game.objects.values()
            if self.rectToBlit.colliderect(object.rect)
        ]
        game.screenMode.blits(self.listToBlit)

    def updateRectToBlit(self,game):
        self.rectToBlit = pg.Rect(
            0,
            0,
            game.screenSize[0],
            game.screenSize[1]
        )

    def updateListToBlit(self,game):
        self.listToBlit = [
            (object.imgSurface,object.rect)
            for object in game.objects.values()
            if self.rectToBlit.colliderect(object.rect)
        ]

    def blit(self,game):
        '''
        It blits all objects on the screenMode'''
        game.screenMode.fill(game.color['backgroundColor'])
        # self.updateRectToBlit(game) ###- precaution
        self.updateListToBlit(game)
        game.screenMode.blits(self.listToBlit)

    def update(self,game):
        self.blit(game)
        pg.display.update(self.rectToBlit)

    # def draw(self,uxElements,game):
    #     '''
    #     It blits all UX Elements on the screenMode'''
    #     pg.draw
    #     game.screenMode.blits(uxElements)

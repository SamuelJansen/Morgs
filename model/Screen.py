import pygame as pg

class Screen():
    '''
    It blits all objects on the screenModule'''
    def __init__(self,game):
        '''
        It blits all objects on the screenModule'''
        game.screenModule.fill(game.color['backgroundColor'])
        self.rectToBlit = pg.Rect(
            0,
            0,
            game.size[0],
            game.size[1]
        )
        self.listToBlit = [
            (object.imageSurface,object.rect)
            for object in game.objects.values()
            if self.rectToBlit.colliderect(object.rect)
        ]
        game.screenModule.blits(self.listToBlit)

    def updateRectToBlit(self,game):
        self.rectToBlit = pg.Rect(
            0,
            0,
            game.size[0],
            game.size[1]
        )

    def updateListToBlit(self,game):
        self.listToBlit = [
            (object.imageSurface,object.rect)
            for object in game.objects.values()
            # if self.rectToBlit.colliderect(object.rect)
        ]

    def blit(self,game):
        '''
        It blits all objects on the screenModule'''
        game.screenModule.fill(game.color['backgroundColor'])
        # self.updateRectToBlit(game) ###- precaution
        self.updateListToBlit(game)
        game.screenModule.blits(self.listToBlit)

    def update(self,game):
        self.blit(game)
        pg.display.update(self.rectToBlit)

    # def draw(self,uxElements,game):
    #     '''
    #     It blits all UX Elements on the screenModule'''
    #     pg.draw
    #     game.screenModule.blits(uxElements)

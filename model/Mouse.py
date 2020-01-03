import pygame as pg

class Mouse():
    def __init__(self,game):
        '''
        Mouse.position is pondered by dev screen size'''
        self.position = [0,0]
        self.devResize = game.devResize

    def getPosition(self):
        ###- It needs some work
        self.position = list(pg.mouse.get_pos())
        self.position[0] = int(self.position[0]*self.devResize[0])
        self.position[1] = int(self.position[1]*self.devResize[1])

    def events(self,event):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.getPosition()
            print(f'Mouse.position = {self.position[0]}x{self.position[1]}x',end='')
        if event.type == pg.MOUSEBUTTONUP :
            self.getPosition()
            print(f'{self.position[0]}x{self.position[1]}')

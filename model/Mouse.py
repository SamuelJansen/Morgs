import pygame as pg

class Mouse():
    def __init__(self,game):
        '''
        Mouse.position is pondered by dev screen size'''
        self.position = [0,0]
        self.devResize = game.devResize

    def getPosition(self):
        self.position = list(pg.mouse.get_pos())
        self.position[0] = (self.position[0]*self.devResize[0])//1
        self.position[1] = (self.position[1]*self.devResize[1])//1

    def events(self,event):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.getPosition()
            print(f'Mouse.position = ({self.position[0]},{self.position[1]})',end='')
        if event.type == pg.MOUSEBUTTONUP :
            self.getPosition()
            print(f'[{self.position[0]},{self.position[1]}]')

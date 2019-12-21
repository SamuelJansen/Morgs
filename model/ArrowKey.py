import pygame as pg

class ArrowKey:
    '''
    It stores any current event until it's over'''
    def __init__(self):
        '''--> Move()'''
        self.status = [0,0]

    def events(self,event):
        '''
        This function is responsible for the
        horizontal and vertical movement of the objects
        ArrowKey.events(event)'''
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_LEFT :
                self.status[0] = -1
            elif event.key==pg.K_RIGHT :
                self.status[0] = 1
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_UP :
                self.status[1] = -1
            elif event.key==pg.K_DOWN :
                self.status[1] = 1
        if event.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = -1
            elif pg.key.get_pressed()[pg.K_RIGHT] and not pg.key.get_pressed()[pg.K_LEFT] :
                self.status[0] = 1
            elif not pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.status[0] = 0
        if event.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = -1
            elif pg.key.get_pressed()[pg.K_DOWN] and not pg.key.get_pressed()[pg.K_UP] :
                self.status[1] = 1
            elif not pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.status[1] = 0

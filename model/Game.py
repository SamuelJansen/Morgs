import pygame as pg
import os
import ctypes
from function import setting

class Game:
    '''
    It defines the game characteristics'''
    def __init__(self,name,fps,aps,colors,osPosition=(0,0),scaleRange=1000):
        '''
        Game(name,screenSize,colors,fps,apf)
        name    --> It's the game's name
        size    --> It's the screen size
        colors  --> It's a dictionary with color's names as keys
        fps     --> frames per second
        apf     --> actions per frame'''
        self.name = name
        self.imagePath = 'resourses/images/'
        self.soundPath = 'resourses/souds/'
        self.color = colors

        self.scaleRange = scaleRange
        self.fps = fps
        self.aps = aps

        self.settings = setting.getSettings(self.name)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % osPosition
        SetWindowPos = ctypes.windll.user32.SetWindowPos
        pg.mixer.pre_init(44100,16,32,0)
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(self.name)

        if self.settings['screenSize']==[0,0] :
            self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN|pg.HWSURFACE|pg.DOUBLEBUF,32)
            screenSizeX, screenSizeY = self.screen.get_size()
            self.screenSize = [screenSizeX, screenSizeY]
            self.size = self.screenSize
        else :
            self.screenSize = self.settings['screenSize']
            self.size = self.screenSize
            self.screen = pg.display.set_mode(self.screenSize,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF)

        SetWindowPos(
            pg.display.get_wm_info()['window'],
            -1,
            0, ###- x
            0, ###- y
            0,
            0,
            0x0001 )
        self.velocityControl = (100 * self.screenSize[0]) / (self.aps * 1920)

        self.devScreenSize = (1000,564)
        self.devResize = [self.devScreenSize[0]/self.screenSize[0],self.devScreenSize[1]/self.screenSize[1]]
        print(f'screenSize = {self.screenSize}, devScreenSize = {self.devScreenSize}, devResize = {self.devResize}')

        self.screen.fill(self.color['backgroundColor'])

        self.playing = True
        pg.display.update()

import pygame as pg
from model import Screen, Frame
import os
import ctypes
from function import setting
from operator import attrgetter

class Game:
    '''
    It defines the game characteristics'''
    def __init__(self,name,fps,aps,timeNow,colors,osPosition=(0,0),scaleRange=1000):
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
            self.screenMode = pg.display.set_mode((0,0),pg.FULLSCREEN|pg.HWSURFACE|pg.DOUBLEBUF,32)#.convert_alpha()
            screenSizeX, screenSizeY = self.screenMode.get_size()
            self.screenSize = [screenSizeX, screenSizeY]
            self.size = self.screenSize
        else :
            self.screenSize = self.settings['screenSize']
            self.size = self.screenSize
            self.screenMode = pg.display.set_mode(self.screenSize,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF)

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

        self.objects = {}
        self.collidableObjects = {}
        self.spaceCostObjectsPositionRectList = []

        self.screen = Screen.Screen(self)

        self.frame = Frame.Frame(timeNow,self)

        self.playing = True

    def updateSpaceCostRectList(self):
        ###- https://www.pygame.org/docs/ref/rect.html
        ###- self.objects = {object.name:object for object in (sorted(self.objects.values(), key=attrgetter('spaceCostRect.top')))}
        self.objects = {object.name:object for object in (sorted(self.objects.values(), key=self.renderOrder))}
        self.collidableObjects = {object.name:object for object in self.objects.values() if object.collides}
        self.spaceCostObjectsPositionRectList = [object.spaceCostRect for object in self.collidableObjects.values()]

    def updateScreen(self):
        '''
        It updates the screen image in the right order.
        Cenario at the background, objects and characteres respecting its places'''
        self.screen.update(self)

    def updateFrame(self,timeNow):
        self.frame.update(timeNow,self)
        if self.frame.new :
            self.updateScreen()

    def update(self,timeNow):
        self.updateFrame(timeNow)

    def renderOrder(self,object):
        return object.type,object.spaceCostRect.bottom
        # return object.spaceCostRect.bottom

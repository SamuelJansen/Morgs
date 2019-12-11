import sys
import os
import pygame as pg
import time as now
import numpy as np
import math
import ctypes
import subprocess

print('GameLibrary imported successfully')

imageLibrary = {}
def getImage(path) :
    '''
    It picks the image contained in the path
    and store it in a library.
    It also returns the     image.
    It works on mac and windows
    getImage(path)'''
    global imageLibrary
    image = imageLibrary.get(path)
    if image==None :
        canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
        image = pg.image.load(canonicalizedPath)#.convert_alpha()
    imageLibrary[path] = image
    return image

soundLibrary = {}
def getSound(path) :
    '''
    It picks the sound contained in the path
    and store it in a library.
    It also returns the sound.
    It works on mac and windows
    getSound(path)'''
    global soundLibrary
    sound = soundLibrary.get(path)
    if sound == None:
        canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pg.mixer.Sound(canonicalizedPath)
        soundLibrary[path] = sound
    return sound

def playSound(sound) :
    '''
    It plays a sound'''
    if sound != None:
        sound.play()

def playMusic(path) :
    '''
    It plays a music that is in the path
    It still needs a check if there is a music already playing'''
    canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
    pg.mixer.music.load(canonicalizedPath)
    pg.mixer.music.play()

def getSettings(name) :
    '''
    It gets overal Game Settings'''
    settings = {}
    with open(name+'.ht','r',encoding='utf-8') as settingsFile :
        allSettings = settingsFile.readlines()
    for line,setting in enumerate(allSettings) :
        ###- print(f'setting = {setting}, line = {line}')
        if setting.startswith('screenSize') :
            screenSize = setting.split()[1].rstrip().split('x')
            screenSize = [int(screenSize[0]),int(screenSize[1])]
            settings['screenSize'] = screenSize
        #elif setting.startswith('*') :
        #    settings.append(Setting(setting.rstrip()[2:].split()))
    return settings


def getObjects(separator=' ') :
    objects = []
    objectsFile = open(name+'.ht','r')
    allObjects = objectsFile.readlines()
    for line,object in enumerate(allObjects) :
        if object.startswith('*') :
            parameters = setting.rstrip()[2:].split(separator)
            ###- name,size,scale,position,velocity,g
            objects.append(
                Object(
                    parameters[0], # name
                    [int(parameters[1].split('x')[0]),int(parameters[1].split('x')[0])], # size - list
                    int(parameters[2]), # scale
                    [int(parameters[1].split('x')[0]),int(parameters[1].split('x')[0])], # position - list
                    int(parameters[4]), # velocity
                    parameters[5] # g
                )
            )
    objectsFile.close()
    return objects


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

        self.settings = getSettings(self.name)

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


class Setting():
    def __init__(self,lineScript):
        self.setting = lineScript
        self.done = False


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
            self.img = pg.transform.smoothscale(getImage(g.imagePath+'standardImage.png'),self.size)
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
                print('colision')
                self.rect = originalRect

    def itColided(self,objects,objectsRectList) :
        colisionIndexes = self.rect.collidelistall(objectsRectList)
        if list(objects.keys()).index(self.name) in colisionIndexes :
            return len(colisionIndexes)>1
        return len(colisionIndexes)>0





class Animation:
    '''
    It stores an animation'''
    def __init__(self,type,timeLenght,delay,frames,o):
        '''
        Animation(name,type,timeLenght,timeDelay,resize,fames,path)'''
        self.type = type
        self.timeLenght = timeLenght
        self.timeDelay = timeDelay
        self.frames = frames
        for i in self.frames :
            self.imagePath = g.imagePath + o.name + type + str(i) + '.png'
            self.img.append(pg.transform.smoothscale(getImage(self.imagePath),self.imgSize))


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


class TimeError:
    '''
    It calculates unexpected time errors'''
    def __init__(self,timeNow) :
        '''
        TimeErrors(timeNow)'''
        self.now = timeNow
        self.before = timeNow
        self.innerLoops = 0

    def checkTimeError(self,timeNow,f):
        '''
        It checks any time erros once each f.fps frames
        TimeError.checkErrors(timeNow,Frame)'''
        self.innerLoops += 1
        if f.newSecond :
            f.timeOveralError = 0
            self.before = self.now
            self.now = timeNow
            f.timeOveralError += f.correctionFactor * ( self.now - self.before - 1 - f.timeOveralError )
            if f.timeOveralError<0 :
                f.timeOveralError = 0
            #"""
            print(f'''      Main loop -- It should be 1: {self.now-self.before}
            timeNow = {timeNow}, f.timeNext = {f.timeNext}
            f.timeError         = {f.timeError}
            f.timeOveralError   = {f.timeOveralError}
            f.apfTimeError      = {f.apfTimeError}
            f.apsCounter = {f.apsCounter}
            innerLoops = {self.innerLoops}''')
            #"""
            self.innerLoops = 0


class Frame:
    '''
    It's a class to control time'''
    def __init__(self,timeNow,g):
        '''
        Frame(timeNow,g)'''
        self.newSecond = True
        #- Frame stuffs
        self.counter = 0
        self.new = True
        self.width = 1 / g.fps
        self.timeNext = timeNow + self.width
        #- Frame stuffs
        self.apsCounter = 0
        #- Actions per frame. It was much simpler to implement
        self.apf = g.aps/g.fps
        self.apfWidth = self.width / self.apf
        self.apfCounter = 0
        self.apfNew = True
        self.apfTimeNext = timeNow + self.apfWidth
        #- Time issues
        self.timeError = 0
        self.apfTimeError = 0
        self.timeOveralError = 0
        self.correctionFactor = .6
        #- External time corrector
        self.correction = TimeError(timeNow)

    def update(self,timeNow,b,g):
        '''
        It aims to mantain the fps and aps constant
        Frame.update(timeNow,g)'''
        #- dealling with frame control
        self.new = False
        self.newSecond = False
        if timeNow>self.timeNext :
            pg.display.update(
                b.rectToBlit
            )
            self.new = True
            self.timeError += self.correctionFactor * ( timeNow - self.timeNext - self.timeError )
            if self.timeError<0 :
                self.timeError = 0
            if self.counter<g.fps-1 :
                self.counter += 1
            else :
                self.newSecond = True
                self.counter = 0
            error = self.timeOveralError * self.width + self.timeError
            self.timeNext = timeNow + self.width - error
        #- Dealling with apf's time erros
        if timeNow>self.apfTimeNext :
            self.apfNew = True
            self.apsCounter += 1
            self.apfTimeError += self.correctionFactor * (timeNow - self.apfTimeNext - self.apfTimeError)
            if self.apfTimeError<0 :
                self.apfTimeError = 0
            if self.apfCounter<self.apf-1 :
                self.apfCounter += 1
            else :
                self.apfCounter = 0
            self.apfTimeNext = timeNow + self.apfWidth - self.apfTimeError
        else :
            self.apfNew = False
        #- Dealling with time erros
        self.correction.checkTimeError(timeNow,self)
        if self.newSecond :
            self.apsCounter = 0


class Mouse():
    def __init__(self,g):
        '''self.foward and self.backwards are already
pondered by course.resize'''
        self.position = [0,0]
        self.devResize = g.devResize

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

#- Animations
class UXSurface :
    def __init__(self,size,position,g):
        self.size = size
        self.position = position
        self.imgSurface = pg.Surface(tuple(size))
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.imgSurface.fill(g.color['red'])

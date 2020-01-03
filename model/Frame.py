import pygame as pg
from model import TimeErrorControl

class Frame:
    '''
    It's a class to control time'''
    def __init__(self,timeNow,game):
        '''
        Frame(timeNow,game)'''
        self.newSecond = True
        #- Frame stuffs
        self.counter = 0
        self.new = True
        self.width = 1 / game.fps
        self.timeNext = timeNow + self.width
        #- Frame stuffs
        self.fpsCounter = 0
        self.apsCounter = 0
        #- Actions per frame. It was much simpler to implement
        self.apf = game.aps/game.fps
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
        self.correction = TimeErrorControl.TimeErrorControl(timeNow)

    def update(self,timeNow,game):
        '''
        It aims to mantain the fps and aps constant
        Frame.update(timeNow,game)'''
        #- dealling with frame control
        self.new = False
        self.newSecond = False
        if timeNow>self.timeNext :
            self.new = True
            self.timeError += self.correctionFactor * (timeNow - self.timeNext - self.timeError)
            if self.timeError<0 :
                self.timeError = 0
            elif self.timeError > 1 :
                self.timeError = .95
            if self.counter<game.fps-1 :
                self.counter += 1
            else :
                self.newSecond = True
                self.counter = 0
            error = self.timeOveralError * self.width + self.timeError
            self.timeNext = timeNow + self.width - error
            self.fpsCounter += 1
        #- Dealling with apf's time erros
        if timeNow>self.apfTimeNext :
            self.apfNew = True
            self.apsCounter += 1
            self.apfTimeError += self.correctionFactor * (timeNow - self.apfTimeNext - self.apfTimeError)
            if self.apfTimeError<0 :
                self.apfTimeError = 0
            elif self.apfTimeError > 1 :
                self.apfTimeError = .95
            if self.apfCounter<self.apf-1 :
                self.apfCounter += 1
            else :
                self.apfCounter = 0
            self.apfTimeNext = timeNow + self.apfWidth - self.apfTimeError
        else :
            self.apfNew = False
        #- Dealling with time erros
        self.correction.checkTimeError(timeNow,self,mustPrint=False)
        if self.newSecond :
            self.fpsCounter = 0
            self.apsCounter = 0

import sys
import os
import pygame as pg
import time as now
import numpy as np
import math
import ctypes
import subprocess

print('GameLibrary imported successfully')

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


class Setting():
    def __init__(self,lineScript):
        self.setting = lineScript
        self.done = False


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

#- Animations
class UXSurface :
    def __init__(self,size,position,g):
        self.size = size
        self.position = position
        self.imgSurface = pg.Surface(tuple(size))
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.imgSurface.fill(g.color['red'])

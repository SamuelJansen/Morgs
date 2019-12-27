import pygame as pg
import os

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
        image = pg.image.load(canonicalizedPath)#.convert_alpha()#.convert()#.set_alpha(100)#
        # image = pg.image.load(canonicalizedPath).convert_alpha()#.convert()#.set_alpha(100)#
        # image = pg.image.load(canonicalizedPath).convert_alpha().set_alpha(100)
    imageLibrary[path] = image
    return image

import pygame as pg
import os

imageLibrary = {}
def getImage(path,game) :
    '''
    It picks the image contained in the path
    and store it in a library.
    It also returns the     image.
    It works on mac and windows
    getImage(path)'''
    global imageLibrary
    image = imageLibrary.get(path)
    if image==None :
        try :
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            print(canonicalizedPath)
            image = pg.image.load(canonicalizedPath).convert()
            #image = pg.image.load(canonicalizedPath)#.convert_alpha()#.convert()#.set_alpha(100)#
            # image = pg.image.load(canonicalizedPath).convert_alpha()#.convert()#.set_alpha(100)#
            # image = pg.image.load(canonicalizedPath).convert_alpha().set_alpha(100)
        except :
            path = game.imagePath+'standardImage.png'
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            image = pg.image.load(canonicalizedPath).convert()
    imageLibrary[path] = image
    return image

def saveImage(image,path) :
    global imageLibrary
    pg.image.save(image, path)
    imageLibrary[path] = image

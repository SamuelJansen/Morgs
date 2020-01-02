import pygame as pg
import os

imageLibrary = {}
def getImage(path,size,game) :
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
            image = pg.image.load(canonicalizedPath)#.convert_alpha()
        except :
            path = game.imagePath+'standard_image.png'
            print(game.imagePath)
            # path = game.imagePath+'character_token.png'
            # path = game.imagePath+'bola.png'
            canonicalizedPath = path.replace('/',os.sep).replace('\\',os.sep)
            image = pg.image.load(canonicalizedPath)#.convert_alpha()
        image = pg.transform.smoothscale(image,size)#.convert_alpha()
    imageLibrary[path] = image
    print('new image')
    return image

def saveImage(image,path) :
    global imageLibrary
    pg.image.save(image, path)
    imageLibrary[path] = image

def newImageSurface(image,size) :
    imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
    # threshold = (40,40,40)
    # image = colorFilter(threshold,image)

    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.SRCALPHA,32)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.SRCALPHA)
    # imageSurface = pg.Surface(size,pg.HWSURFACE|pg.DOUBLEBUF).convert_alpha()
    # imageSurface = pg.Surface(size,pg.HWSURFACE)
    # imageSurface = pg.Surface(size,pg.DOUBLEBUF)
    # imageSurface = pg.Surface(size)

    imageSurface.blit(image,(0,0))
    return imageSurface

def colorFilter(threshold,image) :
    colorThreshold = threshold
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            color = image.get_at((x, y))
            # print(color)
            if ( color.r > colorThreshold[0] and color.g > colorThreshold[1] and color.b > colorThreshold[2] ):
                image.set_at((x, y), (0, 0, 0, 0))
    return image

import numpy as np
from model import Game, Object, Cenario

class PerformanceMeasurement():
    def __init__(self,game,folder,amountOfThings,percentualBigThings,
            objectSize,objectSpaceCostSize,objectBigProportion,
            objectSmallProportion,objectVelocity,mustPopulate=False
        ):
        self.mustPopulate = mustPopulate
        self.populated = False
        self.amountOfThings = amountOfThings
        self.percentualBigThings = percentualBigThings
        self.objectName = 'performance_measurement_object'
        self.objectSize = objectSize
        self.objectSpaceCostSize = objectSpaceCostSize
        self.objectBigProportion = objectBigProportion
        self.objectSmallProportion = objectSmallProportion
        self.objectVelocity = objectVelocity

        bigObjectSpaceCostSize = [200,100]
        bigObjectSpaceCostSize = None
        if self.mustPopulate :
            # game.objects[self.objectName] = Object.Object(
            Object.Object(
                self.objectName,
                folder,
                [200,200],
                [200,200],
                100,
                .5,
                game,
                spaceCostSize=bigObjectSpaceCostSize
            )

            while not self.populated :
                self.populateTheScreen(folder,game)

    def exitGame(self,mouse,game) :
        if mouse.position[0]==game.devScreenSize[0]-1 and mouse.position[1]==0 :
            game.playing = False

    def itColided(self,objectName,game) :
        if game.objects[objectName].collides :
            objectsRectList = [] ###- it needs to come from imput
            for o in game.objects.values() :
                if o.spaceCostSize :
                    objectsRectList.append(o.spaceCostRect)
            colisionIndexes = game.objects[objectName].spaceCostRect.collidelistall(objectsRectList)
            if list(game.objects.keys()).index(game.objects[objectName].name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def dealWithColision(self,game) :
        objectName = self.objectName + str(len(game.objects)-1)
        if self.itColided(objectName,game) :
            # print(f'{game.objects[self.objectName + str(len(game.objects)-1)].name} or {objectName} objected deleted from the game')
            del game.objects[objectName]
            self.populated = False

    def newObject(self,folder,game):
        if len(game.objects)<self.amountOfThings :
            if len(game.objects)<self.amountOfThings*self.percentualBigThings/100 :
                objectProportion = self.objectBigProportion
            else :
                objectProportion = self.objectSmallProportion

            # game.objects[self.objectName + str(len(game.objects))] = Object.Object(
            Object.Object(
                self.objectName + str(len(game.objects)),
                folder,
                [game.screenSize[0]*np.random.random_sample(),game.screenSize[1]*np.random.random_sample()],
                self.objectSize,
                objectProportion,
                self.objectVelocity,
                game,
                spaceCostSize = self.objectSpaceCostSize
            )
            # print(f'{game.objects[self.objectName + str(len(game.objects)-1)].name} object added to the game')
        else :
            self.populated = True
            print('PerformanceMeasurement is populated')

    def moveObjectsRandomically(self,game):
        if self.mustPopulate :
            game.objects[self.objectName].updatePosition([0,1],game)
            for i in range(1,self.amountOfThings) :
                move = [np.random.randint(3)-1,np.random.randint(3)-1]
                game.objects[self.objectName+str(i)].updatePosition(move,game)

    def populateTheScreen(self,folder,game):
        if self.mustPopulate :
            self.newObject(folder,game)
            self.dealWithColision(game)

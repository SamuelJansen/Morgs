from model import Game, Object

class Cenario(Object.Object):
    def __init__(self,name,position,size,velocity,game):
        self.size = [game.size[0]//4,game.size[1]//3]
        self.scale = game.scaleRange/3
        self.piece = ''
        super().__init__(name+str(self.piece),position,self.size,self.scale,velocity,game,type=Object.ObjectTypes.CENARIO)
        pass
    pass

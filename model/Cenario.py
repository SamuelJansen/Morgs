import numpy as np
from model import Game, Object

class Cenario(Object.Object):
    def __init__(self,name,position,size,velocity,game):
        self.size = [game.size[0]//4,game.size[1]//3]
        self.scale = game.scaleRange/3
        self.amountOfColumnPieces = 4
        self.amountOfLinePieces = 3
        self.amountOfPieces = self.amountOfColumnPieces * self.amountOfLinePieces
        self.piecesName = []
        cenarioPiecePosition = []
        for piece in range(self.amountOfPieces) :
            self.piece = piece
            cenarioPiecePosition = [
                position[0]+int(np.ceil((piece%self.amountOfColumnPieces)*self.size[0])),
                position[1]+int(np.ceil((piece%self.amountOfLinePieces)*self.size[1]))
            ]
            self.piecesName.append(Object.Object(
                name+str(self.piece),
                cenarioPiecePosition,
                self.size,
                self.scale,
                velocity,
                game,
                type=Object.ObjectTypes.CENARIO
            ).name)
            # print(f'{newCenarioPiece.name} created')
            # print(f'   {game.objects[newCenarioPiece.name].getPosition()} created')

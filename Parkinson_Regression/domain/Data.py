from repo.Normalizator import Normalizator
import numpy as np

class Data(object):
    def __init__(self, X, independentVar):
        self.X = X
        self.independentVar = independentVar
        
        self.norm = Normalizator(self.X)


        self.Y = np.array(self.norm.getX()[:, self.independentVar - 1])
        #delete the row of y from x
        self.X = np.delete(self.norm.getX(), self.independentVar - 1, 1)

        ones = np.full((len(X), 1), 1)
        self.X = np.append(self.X, ones, axis = 1)
           
        print("X=", self.X)
        print("\nY=", self.Y)

    def getX(self):
           return self.X

    def getY(self):
           return self.Y

    def setY(self, Y):
        self.Y = Y

    def getDenormalizedY(self):
        return self.norm.denormalizeY(self.Y)
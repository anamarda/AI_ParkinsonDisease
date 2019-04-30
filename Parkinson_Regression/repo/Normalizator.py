import numpy as np

class Normalizator():
       def __init__(self, X):
           '''
                input: X - fields with data
           '''
           #np.set_printoptions(suppress=True)
           #np.set_printoptions(precision=15)
           self.X = X
           self.noRows = len(self.X)
           self.meanX = np.zeros(self.X.shape[1])
           self.mean() 
           self.devX = self.devStd()
           self.normalize()

       def setX(self, X):
           self.X = X

       def getX(self):
           return self.X

       def mean(self):
           self.meanX = np.sum(self.X, axis = 0)
           div = np.full((1, self.X.shape[1]), self.noRows)[0]
           self.meanX = self.meanX / div

       def devStd(self):
           rez = self.X - self.meanX
           rez = np.power(rez, 2)
           rez2 =  np.sum(rez, axis = 0)
           rez2 = rez2 / (self.noRows - 1)
           rez2 = np.sqrt(rez2)
           return rez2

       def normalize(self):
           '''
                Normalizes the given matrix.
                Returns: normalized matrix
           '''
           dev = self.devStd()
           rez = self.X - self.meanX
           self.X = rez / dev
           print("---> Got normalized.\n")

       def denormalizeY(self, y_norm):
           '''
                y_norm - the array that has to be denormalized
           '''
           noColumn = len(self.X[1, :]) - 1
           y = y_norm

           y = y * self.devX[noColumn]
           y = y + self.meanX[noColumn]

           return y

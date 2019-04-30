import numpy as np
from numpy.linalg import inv

def linearRegression(dataTrain, dataTest):
    '''
        dataTrain - the object which contains each X and Y for the TRAIN session
        dataTest - the object which contains each X and Y for the TEST session

        This representation is for the normalizator of the object.
    '''

    print("---> Least Square Method:")

    X = dataTrain.getX()
    Y = dataTrain.getY()

    noVariables = len(X[1, :])
    B = np.random.rand(1, noVariables)[0]

    XTy = np.dot(X.transpose(), Y)
    XTX = np.dot(X.transpose(), X)

    B = np.dot(inv(XTX), XTy)

    #print("B:", B)
    
    return predict(dataTest, B)

def predict(dataTest, B):
    print("---> Predict:")

    #extract the data
    X = dataTest.getX()
    Y = dataTest.getY()

    #predict the data
    Ypredict = np.dot(X, B.transpose())

    #denormalize the prediction and the real results
    Y_den = np.array(dataTest.getDenormalizedY())
    dataTest.setY(Ypredict)
    Ypredict_den = dataTest.getDenormalizedY()

    #print some results
    for i in range(len(X)):
        print("Ypredict = ", Ypredict_den[i], " Yreal = ", Y_den[i])

    #calculate the Loss
    calc = np.array(Y_den - Ypredict_den)
    calc = np.power(calc, 2)
    Loss = np.sum(calc) / len(Y_den)

    print("\nLoss=", Loss)
    
    return Loss
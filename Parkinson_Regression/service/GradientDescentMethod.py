import numpy as np

def update(X, Y, B, learning_rate):
       Y_predict = predict(X, B)
       
       for i in range(len(B)):
           grad = 0
           for j in range(len(X)):
               grad = grad + (Y_predict[j] - Y[j]) * X[j][i] 
#           error = Y_predict[j] - Y[j]
#           calc = error * X[:,i]
#           grad = np.sum(calc)
           deltaB = learning_rate * grad
           B[i] -= deltaB
       return B


def predict(X, B):
    Y_pred = np.dot(X, B.transpose())
    return Y_pred

def solve(dataTrain, dataTest, noGen, learning_rate):
    '''
        dataTrain - the object which contains each X and Y for the TRAIN session
        dataTest - the object which contains each X and Y for the TEST session
        learning_rate
        noGen - number of generations

        This representation is for the normalizator of the object.
    '''

    print("---> Gradient Descent Method:")

    X_train = dataTrain.getX()
    Y_train = dataTrain.getY()

    noVariables = len(X_train[1, :])
    #B = np.random.rand(1, noVariables)[0]
    B = np.full((1, noVariables), 0.0)[0]

    for i in range(noGen):
        print("Generation: ", i)
        print("B(",i,")=",B)
        B = update(X_train, Y_train, B, learning_rate)
    
    X_test = dataTest.getX()
    Y_test = dataTest.getY()

    Y_predict = predict(X_test, B)

    #denormalize the prediction and the real results
    Y_den = np.array(dataTest.getDenormalizedY())
    dataTest.setY(Y_predict)
    Ypredict_den = dataTest.getDenormalizedY()

    #print some results
    for i in range(len(X_test)):
        print("Ypredict = ", Ypredict_den[i], "| Yreal = ", Y_den[i], "| err = ", Ypredict_den[i] - Y_den[i])
        

    #calculate the Loss
    calc = np.array(Y_den - Ypredict_den)
    
    calc = np.power(calc, 2)

    Loss = np.sum(calc) / len(Y_den)

    print("\nLoss=", Loss)
    print("B=", B)
    
    return Loss
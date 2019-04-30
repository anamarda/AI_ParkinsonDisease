import math
import random
import numpy as np

def predict(x, coef):
    y = 0;
    for i in range(len(x)):
        y += (x[i] * coef[i])
    return y

def update(coef, learning_rate, x, y):
    y_computed = []
    for i in range(len(x)):
        y_computed.append(predict(x[i], coef))
    for i in range(len(coef)):
        gradient = 0
        for j in range(len(x)):
            err = y_computed[i] - y[i]
            #print("Err: y_computed[",i,"] - y[",i,"]=", err)
            gradient = gradient - (err * x[j][i])
        coef -= (learning_rate * gradient)

def solve(x, y, noAges, learning_rate):
    np.set_printoptions(precision=15)
    coef = np.random.rand(1, len(x[0]))[0]

    noData = len(x)
    cutPoint = (noData * 4) // 5 

    x_train = np.array(x[0:cutPoint])
    y_train = np.array(y[0:cutPoint])
    
    x_test = np.array(x[cutPoint + 1:noData])
    y_test = np.array(y[cutPoint + 1:noData])
    
    for age in range(noAges):        
        print("Age: ", age)
        update(coef, learning_rate, x_train, y_train)
        if(age%2 == 0):
            y_predict = []
            for i in range(len(x_test)):
                y_predict.append(predict(x_test[i], coef))

            print("Yp - Yr = ", y_predict[0] - y_test[0])

    print("Final:")
    y_predict = []
    for i in range(len(x_test)):
         y_predict.append(predict(x_test[i], coef))
    
    data = {
        'y_test' : y_test,
        'y_predict': y_predict
        }
    return data

from sklearn import linear_model

def tool(x, y, noAges):
    
    
    clas = linear_model.LinearRegression()
    clas.max_iter = noAges
    clas.fit(x, y)
    #acc = sum(y == clas.predict(x)) / len(y)

    x_predict = clas.predict(x)
    for i in range(len(y)):
        print("y_real:", y[i], "y_predict:", x_predict[i], "error: ", y[i] - x_predict[i])
    #print("Accuracy:", acc)
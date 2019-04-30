import numpy as np
from domain.Data import Data

class Repo():

       def createFile(self, startPoint, endPoint, fileType):
           '''
                creates a CSV file with data 
                input:
                    startPoint - the start line from the matrix
                    endPoint - the end line from the matrix
                    fileType - "train" or "test"
                output: the created CSV file
           '''
           text = ""
           with open('data/DB/parkinsons_updrs_'+ fileType +'.txt', "w+") as f:
               noVariables = len(self.x[0])
               text+=str(noVariables)+'\n'
               text+=str(endPoint-startPoint-1)+'\n'

               for i in range(startPoint, endPoint):
                   line = ""
                   for j in range(len(self.x[0])-1):
                       line += str(self.x[i][j])+","

                   line+= str(self.x[i][len(self.x[0])-1])+'\n'
                   text+=line
               f.write(text)

       def ReadFromFile(self):
           if(self.fileName == 'data/DB/parkinsons_updrs.data'):
               self.createFromDB()
               self.fileName = 'data/DB/parkinsons_updrs_train.txt'

           with open(self.fileName, "r") as f:
                #number of independent variables
                self.independentVar = int(f.readline().strip())
                #number of data rows
                f.readline()

                line = f.readline().strip().split(",")
                self.x = np.array(line).astype(np.float)

                for line in f.readlines():
                    line = line.strip()

                    if(len(line) > 0):
                        data = line.split(",")
                        a = self.x
                        b = np.array(data).astype(np.float)
                        self.x = np.vstack((a, b))     
               
       def createFromDB(self):
           
           with open(self.fileName, "r") as f:
                   self.independentVar = int(f.readline().strip())
                   f.readline()

                   line = f.readline().strip().split(",")
                   self.x = np.array(line).astype(np.float)

                   for line in f.readlines():
                       line = line.strip()

                       if(len(line) > 0):
                           data = line.split(",")
                           a = self.x
                           b = np.array(data).astype(np.float)
                           self.x = np.vstack((a, b))

           y = np.array(self.x[:, 4]).reshape((len(self.x), 1))
           #delete the row of #subject and motorUPDRS from x
           self.x = np.delete(self.x, 0, 1)
           self.x = np.delete(self.x, 4, 1)
           self.x = np.append(self.x, y, axis = 1)

           cuttingPoint = (len(self.x) * 9) // 10
           self.createFile(0, cuttingPoint, "train")
           self.createFile(cuttingPoint, len(self.x), "test")
               
       def __init__(self, fileName):           
           self.fileName = fileName
           self.independentVar = 0
           self.x = []
           self.ReadFromFile()

           print("---> Initialized Repo.\n")

       def getDataInstance(self):
           d = Data(self.x, self.independentVar)
           return d
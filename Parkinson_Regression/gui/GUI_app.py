from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from repo.Repo import Repo
from service.LeastSquareMethod import linearRegression
from service.GradientDescentMethod import solve


class App():

    def validateLS(self):
        msg = self.validateData()

        if(len(msg) > 0):
            messagebox.showerror("Error", msg)



    def validateGD(self):
        msg = self.validateData()

        if(self.getTextGenerations() == '' or self.getTextLearningRate() == ''):
            msg += "You forgot to type the number of generations and/or the learning rate.\n"

        if(len(msg) > 0):
            messagebox.showerror("Error", msg)
            self.clearData()


    def validateData(self):
        msg = ""

        try:
            if(self.dataTrain or self.dataTest):
                pass
        except AttributeError as ae:
            msg += "There is no data for the training/test.\n"

        return msg



    def clearData(self):
        self.combo = ttk.Combobox(self.window, 
                                values=[
                                        "Easy training",
                                        "Hard training",
                                        ])
        self.combo.grid(row=2, column=0, sticky=E, padx=10)

      


    def setFileData(self, event):
         dict = {
             "Easy" : ["data/parkinson/example_parkinson_01_train.txt", "data/parkinson/example_parkinson_01_test.txt"],
             "Hard" : ["data/DB/parkinsons_updrs_train.txt", "data/DB/parkinsons_updrs_test.txt"],
             "Create files for the hard one" : ["data/DB/parkinsons_updrs.data", "data/DB/parkinsons_updrs_test.txt"]
             }
         self.fileName_train = dict[self.combo.get()][0]
         self.fileName_test = dict[self.combo.get()][1]

   

    def LeastSquareMethod(self):
        #self.validateLS()

        self.repoTrain = Repo(self.fileName_train)
        self.repoTest = Repo(self.fileName_test)
               
        self.dataTrain = self.repoTrain.getDataInstance()
        self.dataTest = self.repoTest.getDataInstance()
        
        result = linearRegression(self.dataTrain, self.dataTest)
        strRes = str(result)
        self.labelLSM = Label(self.panel, text=strRes, bg="grey90", font="none 10 bold") .grid(row=2, column=2,sticky=W, padx=10)



    def GradientDescentMethod(self):
        #self.validateGD()

        self.repoTrain = Repo(self.fileName_train)
        self.repoTest = Repo(self.fileName_test)
               
        self.dataTrain = self.repoTrain.getDataInstance()
        self.dataTest = self.repoTest.getDataInstance()

        result = solve(self.dataTrain, self.dataTest, int(self.getTextGenerations()), float(self.getTextLearningRate()))
        strRes = str(result)

        self.labelGDM = Label(self.panel, text="", bg="grey90", font="none 10 bold")
        self.labelGDM .grid(row=3, column=2,sticky=W, padx=10)

        self.labelGDM = Label(self.panel, text=strRes, bg="grey90", font="none 10 bold") .grid(row=3, column=2,sticky=W, padx=10)



    
    def __init__(self, window, noGenerationsDefault, learningRateDefault):
        self.fileName_train = ""
        self.window = window
        self.noGen = noGenerationsDefault
        self.learningRate = learningRateDefault
      
        #the source of the data for the training label + comboBox
        Label(self.window, text="Data source:", bg="white", font="none 10 bold") .grid(row=2, column=0, sticky=W, padx=10)
        
        #https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-combobox/
        self.combo = ttk.Combobox(self.window, 
                                values=[
                                        "Easy",
                                        "Hard",
                                        "Create files for the hard one"
                                        ])
        self.combo.grid(row=2, column=0, sticky=E, padx=10)
        self.combo.bind("<<ComboboxSelected>>", self.setFileData)

        
        #number of generation label + text
        Label(self.window, text="Number of generations: ", bg="white", font="none 10 bold") .grid(row=3, column=0, sticky=W, padx=10)
        self.textGenerations = Entry(self.window, width=20) 
        self.textGenerations .grid(row=3, column=0, sticky=E, padx=10, pady=10)


        #learning rate label + text
        Label(self.window, text="Learning rate: ", bg="white", font="none 10 bold") .grid(row=4, column=0, sticky=W, padx=10)
        self.textLearningRate = Entry(self.window, width=20) 
        self.textLearningRate.grid(row=4, column=0, sticky=E, padx=10, pady=10)



        #the buttons for the two methods
        self.button1 = Button(self.window, text="LEAST SQUARE METHOD", width=25, command=self.LeastSquareMethod) 
        self.button1.grid(row=5, column=0, sticky=E, padx=10, pady=10)
        self.button2 = Button(self.window, text="GRADIENT DESCENT METHOD", width=25, command=self.GradientDescentMethod) 
        self.button2.grid(row=5, column=0, sticky=W, padx=10, pady=10)


        #results of the training data
        #http://effbot.org/tkinterbook/panedwindow.htm
        self.panel = PanedWindow(orient=VERTICAL) 
        self.panel.configure(background="grey90") #https://stackoverflow.com/questions/51298489/attributeerror-nonetype-object-has-no-attribute-config?noredirect=1&lq=1
        self.panel.grid(row=5, column=1, columnspan = 2, sticky=W, padx=(10, 50), pady=10)

        Label(self.panel, text="Least Square method:", bg="grey90", font="none 10 bold") .grid(row=2, column=1, sticky=W, padx=10)
        self.labelLSM = Label(self.panel, text="N/A", bg="grey90", font="none 10 bold") 
        self.labelLSM.grid(row=2, column=2,sticky=W, padx=60)

        Label(self.panel, text="Gradient Descent method:", bg="grey90", font="none 10 bold") .grid(row=3, column=1, sticky=W, padx=10)
        self.labelGDM = Label(self.panel, text="N/A", bg="grey90", font="none 10 bold") 
        self.labelGDM.grid(row=3, column=2,sticky=W, padx=60)
    
        
    def getTextGenerations(self):
        return self.textGenerations.get()

    
    def getTextLearningRate(self):
        return self.textLearningRate.get()

class GUIException(Exception):
    pass
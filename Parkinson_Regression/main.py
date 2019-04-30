from repo.Repo import Repo
from repo.Normalizator import *
from service.withTool import tool
from service.withoutTool import solve
from gui.GUI_app import *


import math

window = Tk()
window.title("Don't worry - you have Parkinson.")
window.configure(background="white")
photo = PhotoImage(file="data/ParkinsonPhoto2.png")
Label(window, image=photo, bg="white") .grid(row=0, column=0, rowspan=2, sticky=E+W, padx=50, pady=10)

noGenerations = 2000
learningRate = 0.0005

try:
    app = App(window, noGenerations, learningRate)
except GUIException as ex:
    print("----1")
    
    print("----2")

window.mainloop()
import Model.ParseInput as prs

from View.View import View
from Model.JSONEncoder import Write, Read
from Model.Model import dlnet

Yh = []

view = View()

def Debug():
    x, y = prs.Parse("training")
    nn = dlnet(x, y)
    nn.gd(x, y, iter=1)
    Write(nn)

def Release():
    x, y = prs.Parse("check")

    nn = dlnet(x, y)
    Read(nn)
    Yh = nn.forward()
    view = View()



info = input()
if(info == "0"):
    Debug()
elif(info == "1"):
    Release()









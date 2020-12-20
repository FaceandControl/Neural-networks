import Model.ParseInput as prs

from View.View import View
from Model.JSONEncoder import Write, Read
from Model.Model import dlnet

Yh = []


def Debug():
    x, y, path = prs.Parse("training")
    nn = dlnet(x, y)
    nn.gd(x, y, iter=10000)
    Write(nn)

def Release():
    x, y, path = prs.Parse("check")

    nn = dlnet(x, y)
    Read(nn)
    Yh = nn.forward()
    Yh *= 100
    view = View(Yh, path)



info = input("Debug - 0 or Release - 1:")
if(info == "0"):
    Debug()
if(info == "1"):
    Release()









import Model.ParseInput as prs

#from View.View import View
from Model.JSONEncoder import Write, Read
from Model.Model import dlnet

def Debug():
    x, y = prs.Parse()
    print("before init")
    nn = dlnet(x, y)
    print("after init")
    nn.gd(x, y, iter=0)
    print("after train")
    Write(nn)

def Release():
    x = prs.Parse()
    nn = dlnet(x, x)
    Read(nn)
    Yh = nn.forward()

#view = View()

info = input()
if(info == "0"):
    Debug()
elif(info == "1"):
    Release()









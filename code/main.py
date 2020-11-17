import Model.ParseInput as prs
import numpy as np
#from View.View import View
from Model.Model import dlnet

#view = View()

x, y = prs.Parse()
print(np.array(x).shape)
nn = dlnet(x, y)


nn.gd(x, y, iter=20)
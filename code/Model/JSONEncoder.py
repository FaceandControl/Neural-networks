import json
import numpy as np
from Model.Model import dlnet
#from main import nn


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def Read(nn):
    f = open("preparation_data.json", "r")
    parsed_json = json.loads(f.read())
    nn.X = parsed_json["X"]
    nn.Y = parsed_json["Y"]
    nn.Yh = parsed_json["Yh"]
    nn.L = parsed_json["L"]
    nn.dims = parsed_json["dims"]
    nn.param = parsed_json["param"]
    nn.ch = parsed_json["ch"]
    nn.grad = parsed_json["grad"]
    nn.loss = parsed_json["loss"]
    nn.lr = parsed_json["lr"]
    nn.sam = parsed_json["sam"]

def Write(nn):
    json_object = json.dumps(nn.__dict__, cls=NumpyEncoder)
    with open('preparation_data.json', 'w') as outfile:
        outfile.write(json_object)
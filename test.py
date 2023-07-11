import torch
from numbercode import NumberCode
from dataset import NumberCodeDataSet
from model import NumberCodeModel
from torch import linalg as LA
from torch.utils.data import DataLoader


dataset = NumberCodeDataSet(100)
loader = DataLoader(dataset, batch_size = 1)


for sample in loader:
    input = sample["input"]
    result = sample["result"]
    print("Input = "+str(input)+", result = "+str(result))

"""model = NumberCodeModel(hiddenLayerOrder=4)
model.init_origin()
print("Absolute: "+str(model.all_params(from_origin=False))+", Norm = "+str(model.params_norm(from_origin=False)))
print("Relative: "+str(model.all_params(from_origin=True))+", Norm = "+str(model.params_norm(from_origin=True)))"""

